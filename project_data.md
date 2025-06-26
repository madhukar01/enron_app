## Summary of challenge

### Goal

- Enron company is being sued for accounting fraud.
- Email corpus available publically
- We need tosearch through emails to reference material

### Restrictions

- Can’t load entire dataset to RAM
- Corpus remains on device not connected to internet
    - Can preprocess data before storing on device - Static once it is stored
- Search should be substring matching - case insensitive
- Search method called on each keystroke - search(”string”)
- Don’t use libraries for search - ex: lucene

### Evaluation

- Does it work end-to-end?
- Document trade-offs made (comments or readme)
- System design, data structures and algorithms used
- Code readability
- Test cases

## Initial thoughts

- So the data is uploaded to server for pre-processing and then stored on device for on-device search?
- We need a form of indexing + search capability for the data
- Text pre-processing:
    - convert to lower case
    - handle whitespaces, special characters etc that get attached to words
    - stemming?

# Indexing and Search

## Vector embedding / search

- Not an option because of low memory and compute

## KV store - dictionary

- Build a bag of all unique words and sort the word list
- Store word - email mapping in-memory
- Emails are stored on disk
- Upon searching:
    - binary search for the word in the list
    - load relevant emails from memory and show the results
    - con: multiple disk loads as each key is typed / search is called
        - Need caching
    - con: can only do prefix-search

Other option: We can also use a Trie tree dictionary format instead of binary search

- Search is easier
- con: Size of the tree can be huge in comparison to dictionary

Other option: We can use a B-tree indexing for the dictionary for searching

- used in databases and proven
- cons: re-implementing B-tree zzzzz

Other option: n-gram indexing

- very popular for string matching and search
- we can perform substring search!!!
- cons: index size becomes huge as “n” grows - becomes more compute intensive

### Option picked: KV-store dictionary

### Can we solve substring search?

- We can do a normal scan of all unique words for the substring
- build n-grams of the keys and perform a search

We will worry about this once KV methods are implemented and tested.

For now stick to prefix search.
