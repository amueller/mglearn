from mglearn import plots
import types
import matplotlib.pyplot as plt
import pytest

plotting_functions = [getattr(plots, name) for name in plots.__all__
                      if isinstance(getattr(plots, name), types.FunctionType)
                        and getattr(plots, name).__code__.co_argcount == 0]
@pytest.mark.parametrize("plot_func", plotting_functions)
def test_smoke_test_all_plots(plot_func):
    plot_func()
    plt.close('all')