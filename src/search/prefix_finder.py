import bisect
from typing import List, Dict

InvertedIndex = Dict[str, List[str]]


def find_keys_with_prefix(sorted_keys: List[str], prefix: str) -> List[str]:
    """
    Finds all keys in a sorted list that start with a given prefix.

    Args:
        sorted_keys: sorted list of keys.
        prefix: prefix to match.

    Returns:
        List of keys that start with the prefix.

    In a production app, we should cache frequently searched terms and results.
    """
    if not prefix:
        return []

    lower_prefix = prefix.lower()

    # find the first match using binary search
    start_index = bisect.bisect_left(sorted_keys, lower_prefix)

    # iterate from start_index to find all keys with the prefix
    matching_keys = []
    for i in range(start_index, len(sorted_keys)):
        key = sorted_keys[i]
        if key.startswith(lower_prefix):
            matching_keys.append(key)
        else:
            break

    return matching_keys
