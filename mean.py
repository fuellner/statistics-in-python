"""
implementation of arithmetic and weighted arithmetic mean in plain python
"""
from typing import List

# Sample Data for testing
# values: List[int | float] = [1, 2, 2, 2, 4, 5, 6, 6, 3.4, 5.6]
# weights: List[int | float] = [2, 3, 4, 2, 3, 4, 2, 3, 4, 2]


def arithmetic_mean(valueList: List[int | float]) -> float:
    return sum(valueList) / len(valueList)


def weighted_mean(valueList: List[int | float], weights: List[int | float]) -> int | float | None:
    if len(valueList) != len(weights):
        print("Values and weights are not even in count")
        return None
    return sum([valueList[x] * weights[x]
                for x in range(len(valueList))]) / sum(weights)
