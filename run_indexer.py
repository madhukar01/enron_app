from src.indexing.create_index import build_index

# root directory for the email data.
DATA_DIR = "data/maildir"

# path for the output index file.
INDEX_FILE = "index.json"


def main() -> None:
    """
    Main function to run the indexing process.
    """
    print(f"Starting indexing process for directory: {DATA_DIR}")
    print(f"Index will be saved to: {INDEX_FILE}")

    build_index(DATA_DIR, INDEX_FILE, chunk_size=2000)


if __name__ == "__main__":
    main()
