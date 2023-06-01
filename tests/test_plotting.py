from mglearn import plots
import types
import matplotlib.pyplot as plt
import pytest

import inspect
from mglearn import plots
import types
import matplotlib.pyplot as plt
import pytest

def callable_without_arguments(func):
    for arg in inspect.signature(func).parameters:
        if inspect.signature(func).parameters[arg].default is inspect.Parameter.empty:
            return False
    return True

plotting_functions = [getattr(plots, name) for name in plots.__all__
                      if isinstance(getattr(plots, name), types.FunctionType) and callable_without_arguments(getattr(plots, name))]

@pytest.mark.parametrize("plot_func", plotting_functions)
def test_smoke_test_all_plots(plot_func):
    plot_func()
    plt.close('all')
