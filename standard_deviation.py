"""
implementation of sample variance, population variance and standard deviation functions in plain python
"""
from typing import List
from statistics import mean
from math import sqrt

# Sample Data for testing
# values: List[int | float] = [1, 2, 2, 2, 3, 4, 5, 6, 6, 3.4, 5.6]


def population_variance(values: List[int | float]) -> int | float:
    result: int | float = 0
    n: int = len(values)
    mw: int | float = mean(values)

    for x in values:
        result += pow(x - mw, 2)

    return result / n


def sample_variance(values: List[int | float]) -> int | float:
    result: int | float = 0
    n: int = len(values)
    mw: int | float = mean(values)

    for x in values:
        result += pow(x - mw, 2)

    return result / (n - 1)


def standard_deviation(values: List[int | float]) -> int | float:
    return sqrt(sample_variance(values))
