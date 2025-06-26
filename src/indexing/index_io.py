import json
import os
from typing import Dict, List

InvertedIndex = Dict[str, List[str]]


def save_index(index: InvertedIndex, file_path: str) -> None:
    """
    Save inverted index to a file in JSON format.

    Making it atomic - by writing to a temporary file first, then renaming it
    This is needed to run search.py and indexer.py in parallel.

    Args:
        index: The inverted index to save.
        file_path: The path to the output file.
    """
    temp_path = file_path + ".tmp"
    try:
        with open(temp_path, "w", encoding="utf-8") as f:
            json.dump(index, f)
        os.replace(temp_path, file_path)
    except IOError as e:
        print(f"Error saving index to {file_path}: {e}")
    finally:
        # cleanp temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)


def load_index(file_path: str) -> InvertedIndex:
    """
    Loads an inverted index from a JSON file.

    Args:
        file_path: path to index file.

    Returns:
        Loaded inverted index.
    """
    if not os.path.exists(file_path):
        return {}

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, dict):
                return data
            return {}
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error loading index from {file_path}: {e}")
        return {}
