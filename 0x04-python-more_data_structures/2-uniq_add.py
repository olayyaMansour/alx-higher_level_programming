#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Add all unique integers in a list."""
    unique_set = set(my_list)
    result = sum(unique_set)
    return result
