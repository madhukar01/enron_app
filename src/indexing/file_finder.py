import os
from typing import List


def find_email_files(root_dir: str) -> List[str]:
    """
    Finds all files in a directory and returns them as a list.

    Args:
        root_dir: root directory to search.

    Returns:
        A list of paths to all files found.
    """
    file_paths = []
    for root, _, files in os.walk(root_dir):
        for file in files:
            file_paths.append(os.path.join(root, file))
    return file_paths
