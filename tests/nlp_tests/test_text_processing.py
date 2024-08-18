import pytest
from nlp.text_processing import normalize, tokenize, remove_stop_words, lemmatize, process_command

# normalize text by converting it to lowercase
def test_normalize():
    if(normalize("Hello, World!") != "hello, world!"):
        return False
    
    return True
    
# tokenize the text, splitting it into individual words or tokens
def test_tokenize():
    if(tokenize("Hello, World!") != ["hello", "world"]):
        return False

    return True

# remove common stop words from a list of tokens
# (e.g., "and", "the", "is", etc.)
def test_remove_stop_words():
    if(remove_stop_words(["hello", "and", "world"]) != ["hello", "world"])
        return False
    
    return True

# lemmatize tokens, reducing words to their base or root form
# (e.g., "running" to "run", "jumps" to "jump")
def test_lemmatize():
    if(lemmatize(["running", "jumps"]) != ["run", "jump"])
        return False

    return True


# PYTEST OUTPUT
assert test_normalize() == True

assert test_tokenize() == True

assert test_remove_stop_words() == True

assert test_lemmatize() == True


  
  
