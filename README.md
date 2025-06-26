# Enron Email Search

My detailed thought process is available in [thought_process.md](thought_process.md).

## Setup and Execution

### 1. Prerequisites
- Python 3.11+
- [Poetry](https://python-poetry.org/docs/#installation) for dependency management.

### 2. Installation
1.  **Download the Data:**
    - Download the Enron email dataset.
    - Extract the `maildir` directory and place it inside the `data/` folder at the root of this project. The final path should be `data/maildir`.

2.  **Install Dependencies:**
    ```bash
    poetry install
    ```

### 3. Running the Application

The application consists of two main components: an indexer that processes the emails and a search script that queries the generated index.

**Step 1: Run the Indexer**

This script will process all emails in `data/maildir` and create a searchable `index.json` file. This is a one-time setup process that is computationally intensive.

```bash
poetry run python run_indexer.py
```

*Note: You can run the search script in a separate terminal while the indexer is still running. The search results will become more comprehensive as the indexer progresses.*

**Step 2: Perform a Search**

To search the indexed emails, run the following command. You can modify the `search_term_str` variable inside `run_search.py` to change your query.

```bash
poetry run python run_search.py
```
