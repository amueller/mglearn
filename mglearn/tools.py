import numpy as np
from sklearn.datasets import make_blobs
from sklearn.tree import export_graphviz
import matplotlib.pyplot as plt
from .plot_2d_separator import (plot_2d_separator, plot_2d_classification,
                                plot_2d_scores)
from .plot_helpers import cm2 as cm, discrete_scatter


def visualize_coefficients(coefficients, feature_names, n_top_features=25):
    """Visualize coefficients of a linear model.

    Parameters
    ----------
    coefficients : nd-array, shape (n_features,)
        Model coefficients.

    feature_names : list or nd-array of strings, shape (n_features,)
        Feature names for labeling the coefficients.

    n_top_features : int, default=25
        How many features to show. The function will show the largest (most
        positive) and smallest (most negative)  n_top_features coefficients,
        for a total of 2 * n_top_features coefficients.
    """
    coefficients = coefficients.squeeze()
    if coefficients.ndim > 1:
        # this is not a row or column vector
        raise ValueError("coeffients must be 1d array or column vector, got"
                         " shape {}".format(coefficients.shape))
    coefficients = coefficients.ravel()

    if len(coefficients) != len(feature_names):
        raise ValueError("Number of coefficients {} doesn't match number of"
                         "feature names {}.".format(len(coefficients),
                                                    len(feature_names)))
    # get coefficients with large absolute values
    coef = coefficients.ravel()
    positive_coefficients = np.argsort(coef)[-n_top_features:]
    negative_coefficients = np.argsort(coef)[:n_top_features]
    interesting_coefficients = np.hstack([negative_coefficients,
                                          positive_coefficients])
    # plot them
    plt.figure(figsize=(15, 5))
    colors = [cm(1) if c < 0 else cm(0)
              for c in coef[interesting_coefficients]]
    plt.bar(np.arange(2 * n_top_features), coef[interesting_coefficients],
            color=colors)
    feature_names = np.array(feature_names)
    plt.subplots_adjust(bottom=0.3)
    plt.xticks(np.arange(1, 1 + 2 * n_top_features),
               feature_names[interesting_coefficients], rotation=60,
               ha="right")
    plt.ylabel("Coefficient magnitude")
    plt.xlabel("Feature")


def heatmap(values, xlabel, ylabel, xticklabels, yticklabels, cmap=None,
            vmin=None, vmax=None, ax=None, fmt="%0.2f"):
    if ax is None:
        ax = plt.gca()
    # plot the mean cross-validation scores
    img = ax.pcolor(values, cmap=cmap, vmin=vmin, vmax=vmax)
    img.update_scalarmappable()
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_xticks(np.arange(len(xticklabels)) + .5)
    ax.set_yticks(np.arange(len(yticklabels)) + .5)
    ax.set_xticklabels(xticklabels)
    ax.set_yticklabels(yticklabels)
    ax.set_aspect(1)

    for p, color, value in zip(img.get_paths(), img.get_facecolors(),
                               img.get_array()):
        x, y = p.vertices[:-2, :].mean(0)
        if np.mean(color[:3]) > 0.5:
            c = 'k'
        else:
            c = 'w'
        ax.text(x, y, fmt % value, color=c, ha="center", va="center")
    return img


def make_handcrafted_dataset():
    # a carefully hand-designed dataset lol
    X, y = make_blobs(centers=2, random_state=4, n_samples=30)
    y[np.array([7, 27])] = 0
    mask = np.ones(len(X), dtype=np.bool)
    mask[np.array([0, 1, 5, 26])] = 0
    X, y = X[mask], y[mask]
    return X, y


def print_topics(topics, feature_names, sorting, topics_per_chunk=6,
                 n_words=20):
    for i in range(0, len(topics), topics_per_chunk):
        # for each chunk:
        these_topics = topics[i: i + topics_per_chunk]
        # maybe we have less than topics_per_chunk left
        len_this_chunk = len(these_topics)
        #generate list of sorted features and their lengths
        row = []
        for i in range(n_words):
            row.append(feature_names[sorting[these_topics, i]])
        topic_words = np.array(row).T
        #get max feature length for each topic
        max_feat_len = []
        for t in topic_words:
            max_feat_len.append(len(max(t, key = len)))
        #generate space between strings equal to 1+len(longest string in topic)
        result = [None]*len(these_topics)*2
        result[::2] = these_topics
        nums = np.array([(x - 5) for x in max_feat_len])
        nums[nums < 0] = 0 #prevents spaces of negative length
        result[1::2] = [str(x) for x in nums]
        print(("topic {:<{}} " * len_this_chunk).format(*result))
        
        #generate space between strings equal to 1+len(longest string in topic)
        result = [None]*len(these_topics)*2
        result[::2] = ['']*len(these_topics)
        nums = np.array([(x - 8) for x in max_feat_len])
        nums[nums < 0] = 0 #prevents spaces of negative length
        result[1::2] = [str(x) for x in nums]
        print(("-------- {:<{}} " * len_this_chunk).format(*result))
        
        # print top n_words frequent words
        for i in range(n_words):
            #generate space between strings 
            result = [None]*len(these_topics)*2
            result[::2] = feature_names[sorting[these_topics, i]]
            result[1::2] = [str(x+2) for x in max_feat_len]
            try:
                print(("{:<{}}" * len_this_chunk).format(*result))
            except:
                pass
        print("\n")

        
def get_tree(tree, **kwargs):
    try:
        # python3
        from io import StringIO
    except ImportError:
        # python2
        from StringIO import StringIO
    f = StringIO()
    export_graphviz(tree, f, **kwargs)
    import graphviz
    return graphviz.Source(f.getvalue())

__all__ = ['plot_2d_separator', 'plot_2d_classification', 'plot_2d_scores',
           'cm', 'visualize_coefficients', 'print_topics', 'heatmap',
           'discrete_scatter']
