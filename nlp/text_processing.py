# Function to normalize text by converting it to lowercase
def normalize(text: str) -> str:
    return text.lower()

# Function to tokenize the text, splitting it into individual words or tokens
def tokenize(text: str) -> list[str]:
    pass

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