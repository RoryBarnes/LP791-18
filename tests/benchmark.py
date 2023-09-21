import functools
import inspect
import os

import astropy.units as u
import numpy as np
import pytest

import vplanet


def recursive_getattr(obj, attr, *args):
    _getattr = lambda obj, attr: getattr(obj, attr, *args)
    return functools.reduce(_getattr, [obj] + attr.split("."))


class Benchmark:
    def test_benchmark(self, vplanet_output, param, value, unit, param_options):
        # The value returned by vplanet
        output_value = recursive_getattr(vplanet_output, param)

        # Are we comparing a specific index of an array?
        index = param_options.pop("index", None)
        if index is not None:
            output_value = output_value[index]

        # The expected value
        benchmark_value = value * unit

        # Check
        if np.allclose(output_value, benchmark_value, **param_options) == 0:
            print(
                "Standard: " + repr(benchmark_value) + ", Trial: " + repr(output_value)
            )
            assert False


def benchmark(args_dict):
    args = []
    for param, v in args_dict.items():
        value = v.pop("value", 0.0)
        unit = v.pop("unit", u.Unit(""))
        marks = v.pop("marks", None)
        if marks is not None:
            args.append(pytest.param(param, value, unit, v, marks=marks))
        else:
            args.append(pytest.param(param, value, unit, v))
    return pytest.mark.parametrize("param,value,unit,param_options", args)
