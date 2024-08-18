import re

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
    pass

# Function to lemmatize tokens, reducing words to their base or root form
# (e.g., "running" to "run", "jumps" to "jump")
def lemmatize(tokens: list[str]) -> list[str]:
    pass

# Function to process a command by applying a series of text processing steps
def process_command(text: str) -> list[str]:
    pass