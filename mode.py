"""
implementation of mode in plain python
"""

from typing import List

# Sample Data for testing
# values: List[int | float] = [1, 2, 2, 2, 4, 5, 6, 6, 3.4, 5.6]


def mode(args: List[int | float]) -> List[int | float]:
    dict_values = {i: args.count(i) for i in args}
    max_list = [k for k, v in dict_values.items() if v ==
                max(dict_values.values())]
    return max_list
