from collections import defaultdict
from typing import Dict, List

from src.indexing.email_parser import parse_email
from src.indexing.file_finder import find_email_files
from src.indexing.text_processor import normalize_text

InvertedIndex = Dict[str, List[str]]


def build_index(root_dir: str) -> InvertedIndex:
    """
    Builds an inverted index from all emails in a directory.

    Args:
        root_dir: root directory containing email files.

    Returns:
        Inverted index mapping words to a list of file paths.
    """
    index: InvertedIndex = defaultdict(list)
    file_count = 0

    for file_path in find_email_files(root_dir):
        file_count += 1
        if file_count % 100 == 0:
            print(f"Processing file {file_count}...")

        content = parse_email(file_path)
        if not content:
            continue

        tokens = normalize_text(content)
        for token in tokens:
            # don't duplicate file paths for the same token
            if file_path not in index[token]:
                index[token].append(file_path)

    print(f"Indexing complete. Processed {file_count} files.")

    # return regular dict to store in json
    return dict(index)
