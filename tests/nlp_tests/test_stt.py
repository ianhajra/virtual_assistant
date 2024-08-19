import pytest
from nlp.speech_to_text import stt

# TODO: create audio files for testing
def test_stt():
    assert stt('audio/path_one.wav') == "Hello world"
    assert stt('audio/path_two.wav') == "This is a test of a longer sentence"

