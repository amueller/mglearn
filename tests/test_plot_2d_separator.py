import pytest

import numpy as np
from sklearn.datasets import make_blobs
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

from mglearn.plot_2d_separator import plot_2d_separator, plot_2d_classification, plot_2d_scores
import matplotlib.pyplot as plt

@pytest.mark.parametrize("fill", [True, False])
@pytest.mark.parametrize("clf", [LogisticRegression(), DecisionTreeClassifier()])
def test_plot_2d_separator(clf, fill):
    # Generate random data
    X, y = make_blobs(centers=2, random_state=42)

    clf.fit(X, y)
    # Smoketest the plot_2d_separator function
    ax = plot_2d_separator(clf, X, fill=fill)


@pytest.mark.parametrize("clf", [LogisticRegression(), DecisionTreeClassifier()])
def test_plot_2d_classification(clf):
    # Generate random data
    X, y = make_blobs(centers=2, random_state=42)

    clf.fit(X, y)
    # Smoketest the plot_2d_separator function
    ax = plot_2d_classification(clf, X, fill=True)

@pytest.mark.parametrize("clf", [LogisticRegression(), DecisionTreeClassifier()])
def test_plot_2d_scores(clf):
    # Generate random data
    X, y = make_blobs(centers=2, random_state=42)

    # Train a logistic regression model
    clf.fit(X, y)
    # Smoketest the plot_2d_separator function
    ax = plot_2d_scores(clf, X)