from src.indexing.index_io import load_index
from src.search.search_term import search_term

INDEX_FILE = "index.json"


def main() -> None:
    """
    Main function to load index and perform search.
    """
    # in a production app - the index should be stored in memory
    # to avoid disk I/O
    print(f"Loading index from {INDEX_FILE}...")
    index = load_index(INDEX_FILE)

    if not index:
        print("Could not load index. Exiting.")
        return

    # index on disk may be unsorted if the indexer is running.
    # sort the keys here to ensure binary search works.
    # in a production app - we should pre-sort the index on disk
    sorted_keys = sorted(index.keys())
    print("Index loaded successfully.")

    # --- Example Search ---
    search_term_str = "che"
    print(f"\nSearching for term: '{search_term_str}'")

    results = search_term(index, sorted_keys, search_term_str, limit=5)

    if not results:
        print("No results found.")
    else:
        print(f"Found {len(results)} results:")
        for i, email_content in enumerate(results):
            print(f"\n--- Result {i + 1} ---")
            print(email_content)
            print("--------------------")


if __name__ == "__main__":
    main()
