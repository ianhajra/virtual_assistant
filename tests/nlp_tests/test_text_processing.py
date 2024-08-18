import pytest
from nlp.text_processing import normalize, tokenize, remove_stop_words, lemmatize, process_command

def test_normalize():
    normalize("Hello, World!") == "hello, world!"

def test_tokenize():
    tokenize("Hello, World!") == ["hello", "world"]

def test_remove_stop_words():
    remove_stop_words(["hello", "and", "world"]) == ["hello", "world"]

def test_lemmatize():
    lemmatize(["running", "jumps"]) == ["run", "jump"]

def test_process_command():
    process_command("Hello, World!") == ["hello", "world"]


# pytest output
assert test_normalize() == True

assert test_tokenize() == True

assert test_remove_stop_words() == True

assert test_lemmatize() == True

assert test_process_command() == True


  
  
