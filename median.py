"""
implementation of median in plain python
"""

from typing import List

# Sample Data for testing
# values: List[int | float] = [1, 2, 1, 2, 2, 3, 4, 7, 6, 6, 3.4, 5.6, 4, 4]


def median(values: List[int | float]) -> int | float:
    values = sorted(values)
    halfLenght = int(len(values) / 2)
    if len(values) % 2 != 0:
        return (values[halfLenght] + values[halfLenght + 1]) / 2
    return values[halfLenght]
