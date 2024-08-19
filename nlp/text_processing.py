import re

from .constants import STOP_WORDS
from nltk.stem import PorterStemmer

# Used for stemming later on
stemmer = PorterStemmer()

# Function to normalize text by converting it to lowercase
# And remove non whitespace and alphabetic characters
def normalize(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

# Function to tokenize the text, splitting it into individual words or tokens
def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+|[^\w\s]', text)

# Function to remove common stop words from a list of tokens
# (e.g., "and", "the", "is", etc.)
def remove_stop_words(tokens: list[str]) -> list[str]:
    return [token for token in tokens if token not in STOP_WORDS]

# Function to stem tokens, reducing words to a stemmed form
def stem(tokens: list[str]) -> list[str]:
    return [stemmer.stem(token) for token in tokens]

# Function to process a text by applying a series of text processing steps
def process_text(text: str) -> list[str]:
    text = normalize(text)
    text = tokenize(text)
    text = remove_stop_words(text)
    text = stem(text)
    return text