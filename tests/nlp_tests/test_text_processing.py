import pytest
from nlp.text_processing import normalize, tokenize, remove_stop_words, lemmatize, process_command

# normalize text by converting it to lowercase
def test_normalize():
    assert normalize("Hello, World!") == "hello, world!"
    assert normalize("weIrD InPUt") == "weird input"
    assert normalize("ALL CAPS INPUT") == "all caps input"
    assert normalize("all lowercase input") == "all lowercase input"
    assert normalize("572983758923789327") == "572983758923789327"
    assert normalize("@%^&^$#") == "@%^&^$#"

# tokenize the text, splitting it into individual words or tokens
def test_tokenize():
    assert tokenize("Hello, World!") == ["hello", "world"]

# remove common stop words from a list of tokens
# (e.g., "and", "the", "is", etc.)
def test_remove_stop_words():
    assert remove_stop_words(["hello", "and", "world"]) == ["hello", "world"]

# lemmatize tokens, reducing words to their base or root form
# (e.g., "running" to "run", "jumps" to "jump")
def test_lemmatize():
    assert lemmatize(["running", "jumps"]) == ["run", "jump"]