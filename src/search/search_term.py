from typing import List, Dict

from src.search.prefix_finder import find_keys_with_prefix
from src.search.content_reader import read_files

InvertedIndex = Dict[str, List[str]]


def search_term(
    index: InvertedIndex,
    sorted_keys: List[str],
    term: str,
    limit: int = 10,
    offset: int = 0,
) -> List[str]:
    """
    Searches the index for a term and returns paginated email content.

    Args:
        index: inverted index to search.
        sorted_keys: sorted list of keys from the index.
        term: search term or prefix.
        limit: maximum number of results to return.
        offset: starting offset for the results.

    Returns:
        List of full email contents that match the search criteria.

    In a production app, we should cache frequently searched terms and results.
    """
    # clean the term
    term = term.strip().lower()

    matching_keys = find_keys_with_prefix(sorted_keys, term)
    if not matching_keys:
        return []

    # aggregate file paths for matching keys
    all_file_paths = []
    for key in matching_keys:
        all_file_paths.extend(index[key])

    # remove duplicates
    unique_file_paths = list(dict.fromkeys(all_file_paths))

    # apply pagination
    paginated_paths = unique_file_paths[offset : offset + limit]

    # read the content of the final files
    return read_files(paginated_paths)
