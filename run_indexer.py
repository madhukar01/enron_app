from src.indexing.create_index import build_index
from src.indexing.index_io import save_index

# root directory for the email data.
DATA_DIR = "data/sample"

# path for storing output index file.
INDEX_FILE = "index.json"


def main() -> None:
    """
    Main function to run the indexing process and save the index.
    """
    print(f"Starting indexing process for directory: {DATA_DIR}")

    inverted_index = build_index(DATA_DIR)

    if inverted_index:
        print(f"Saving index to {INDEX_FILE}...")
        save_index(inverted_index, INDEX_FILE)
        print("Index saved successfully.")
    else:
        print("Index creation failed or created empty index.")


if __name__ == "__main__":
    main()
