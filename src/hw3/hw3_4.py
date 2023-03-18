"""
Write a function that takes K lists as arguments and returns all possible
lists of K items where the first element is from the first list,
the second is from the second and so one.
You may assume that that every list contain at least one element
Example:
assert combinations([1, 2], [3, 4]) == [
    [1, 3],
    [1, 4],
    [2, 3],
    [2, 4],
]
"""
from typing import Any, List


def combinations(*args: List[Any]) -> List[List]:
    all_combination = []
    count_list = len(args)
    if count_list == 2:
        for i in args[0]:
            for j in args[1]:
                combination = [i, j]
                all_combination.append(combination)
    if count_list == 3:
        for i in args[0]:
            for j in args[1]:
                for k in args[2]:
                    combination = [i, j, k]
                    all_combination.append(combination)
    return all_combination
