import numpy as np
import pandas as pd
from mglearn.datasets import make_forge, make_wave, load_extended_boston, load_citibike, make_signals


def test_make_forge():
    X, y = make_forge()
    assert X.shape == (26, 2)
    assert y.shape == (26,)
    assert np.sum(y == 0) == 13
    assert np.sum(y == 1) == 13


def test_make_wave():
    X, y = make_wave(n_samples=100)
    assert X.shape == (100, 1)
    assert y.shape == (100,)


def test_load_extended_boston():
    X, y = load_extended_boston()
    assert X.shape == (506, 104)
    assert y.shape == (506,)


def test_load_citibike():
    data = load_citibike()
    assert isinstance(data, pd.Series)
    assert data.index[0].__class__.__name__ == 'Timestamp'


def test_make_signals():
    S = make_signals()
    assert S.shape == (2000, 3)
    assert np.allclose(S.std(axis=0), np.array([1., 1., 1.]), atol=0.2)
    assert np.allclose(S.min(), 0, atol=0.2)
