#!/usr/bin/python3
"""Weighted Average"""


def weight_average(my_list=[]):
    """Calculates the weighted average of a list of tuples"""
    if not my_list or len(my_list) == 0:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight


if __name__ == "__main__":
    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))
