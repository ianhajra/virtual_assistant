import pytest
from nlp.speech_to_text import stt

def test_stt():
    assert stt('audio/path_one.wav') == "The cat sat on the windowsill, watching the birds outside."
    assert stt('audio/path_two.wav') == "This is a test of a longer sentence"
    assert stt('audio/path_three.wav') == "The meeting has been rescheduled for next Thursday."
    assert stt('audio/path_three.wav') == "She enjoys reading books about ancient history."
    assert stt('audio/path_three.wav') == "The sunset painted the sky with shades of orange and pink."
    assert stt('audio/path_three.wav') == "Can you help me find the nearest coffee shop?"
    assert stt('audio/path_three.wav') == "The weather forecast predicts rain later this afternoon."
    assert stt('audio/path_three.wav') == "He quickly finished his homework before going out to play."
    assert stt('audio/path_three.wav') == "The chef prepared a delicious meal for the guests."
    assert stt('audio/path_three.wav') == "They decided to take a road trip across the country."





