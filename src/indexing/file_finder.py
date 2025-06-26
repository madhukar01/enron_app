import os
from typing import Generator


def find_email_files(root_dir: str) -> Generator[str, None, None]:
    """
    Finds all files in a directory and its subdirectories.

    Args:
        root_dir: The root directory to search.

    Yields:
        The path to each file found.
    """
    for root, _, files in os.walk(root_dir):
        for file in files:
            yield os.path.join(root, file)
