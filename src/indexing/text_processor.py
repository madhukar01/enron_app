import re
from typing import List, Set

# a few English stop words to remove
# in a production app, we should use NLTK or spaCy to remove stop words
STOP_WORDS: Set[str] = {
    "a",
    "an",
    "and",
    "are",
    "as",
    "at",
    "be",
    "by",
    "for",
    "from",
    "has",
    "he",
    "in",
    "is",
    "it",
    "its",
    "of",
    "on",
    "that",
    "the",
    "to",
    "was",
    "were",
    "will",
    "with",
}


def normalize_text(text: str) -> List[str]:
    """
    Normalizes a string of text for searching.

    This function performs:
    1. Converts text to lowercase.
    2. Tokenizes text into words using a regex - alphanumeric only.
    3. Removes stop words.

    Args:
        text: input string to normalize.

    Returns:
        A list of normalized word tokens.
    """
    text = text.lower()
    words = re.findall(r"\b\w+\b", text)
    return [word for word in words if word not in STOP_WORDS]
