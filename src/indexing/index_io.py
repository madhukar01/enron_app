import json
from typing import Dict, List

InvertedIndex = Dict[str, List[str]]


def save_index(index: InvertedIndex, file_path: str) -> None:
    """
    Saves inverted index to a file in JSON format.

    Args:
        index: inverted index to save.
        file_path: path to output file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(index, f, indent=4)
    except IOError as e:
        print(f"Error saving index to {file_path}: {e}")


def load_index(file_path: str) -> InvertedIndex:
    """
    Loads an inverted index from a JSON file.

    Args:
        file_path: path to index file.

    Returns:
        Loaded inverted index.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading index from {file_path}: {e}")
        return {}
