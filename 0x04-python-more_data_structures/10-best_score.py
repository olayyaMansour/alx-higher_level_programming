#!/usr/bin/python3
def best_score(a_dictionary):
    """Return a key with the biggest integer value."""
    if a_dictionary:
        best_key = max(a_dictionary, key=a_dictionary.get)
        return best_key
    else:
        return None
