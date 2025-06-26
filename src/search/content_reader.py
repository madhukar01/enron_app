from typing import List


def read_files(file_paths: List[str]) -> List[str]:
    """
    Reads content of multiple files.

    Args:
        file_paths: list of paths to the files to read.

    Returns:
        List of strings that correspond to content of files.
        If a file cannot be read, it is removed from output.

    """
    contents = []
    for file_path in file_paths:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                contents.append(f.read())
        except IOError:
            # we should log these errors
            pass
    return contents
