from collections import defaultdict
from typing import Dict, List, Tuple
from concurrent.futures import ProcessPoolExecutor, as_completed
import os

from src.indexing.email_parser import parse_email
from src.indexing.file_finder import find_email_files
from src.indexing.index_io import save_index
from src.indexing.text_processor import normalize_text

InvertedIndex = Dict[str, List[str]]


def _process_file(file_path: str) -> Tuple[str, List[str]]:
    """
    Worker function to process a single file.
    Parses email and normalizes its content into tokens.
    """
    content = parse_email(file_path)
    if not content:
        return file_path, []

    tokens = normalize_text(content)
    return file_path, tokens


def _chunked_files(files: List[str], chunk_size: int):
    """Yields n-sized chunks from a list of files."""
    for i in range(0, len(files), chunk_size):
        yield files[i : i + chunk_size]


def build_index(
    root_dir: str, index_file_path: str, chunk_size: int = 1000
) -> None:
    """
    Builds an inverted index and saves it periodically.

    Args:
        root_dir: root directory containing email files.
        index_file_path: path to save the index file.
        chunk_size: number of files to process in each batch.
    """
    index: InvertedIndex = defaultdict(list)

    print("Finding all email files...")
    all_files = find_email_files(root_dir)
    file_count = len(all_files)
    print(
        f"Found {file_count} files. Starting parallel processing in batches of {chunk_size}..."
    )

    max_workers = os.cpu_count()
    processed_count = 0
    with ProcessPoolExecutor(max_workers=max_workers) as executor:
        # process files in chunks to avoid freezing
        for file_chunk in _chunked_files(all_files, chunk_size):
            futures = [
                executor.submit(_process_file, path) for path in file_chunk
            ]

            for future in as_completed(futures):
                processed_count += 1
                if processed_count % 1000 == 0:
                    print(f"Processed {processed_count}/{file_count} files...")

                try:
                    file_path, tokens = future.result()
                    for token in tokens:
                        if file_path not in index[token]:
                            index[token].append(file_path)
                except Exception as e:
                    print(f"Error processing file: {e}")

            processed_count += len(file_chunk)
            print(
                f"Processed {processed_count}/{file_count} files. Saving intermediate index..."
            )
            save_index(dict(index), index_file_path)

    print("Indexing complete. Sorting and saving...")
    sorted_items = sorted(index.items())
    save_index(dict(sorted_items), index_file_path)
    print("Final sorted index saved.")
