import pytest
from nlp.speech_to_text import stt

def test_stt():
    assert stt('audio/test_audio_one') == "The cat sat on the windowsill, watching the birds outside."
    assert stt('audio/test_audio_two') == "This is a test of a longer sentence"
    assert stt('audio/test_audio_three') == "The meeting has been rescheduled for next Thursday."
    assert stt('audio/test_audio_four') == "She enjoys reading books about ancient history."
    assert stt('audio/test_audio_five') == "The sunset painted the sky with shades of orange and pink."
    assert stt('audio/test_audio_six') == "Can you help me find the nearest coffee shop?"
    assert stt('audio/test_audio_seven') == "The weather forecast predicts rain later this afternoon."
    assert stt('audio/test_audio_eight') == "He quickly finished his homework before going out to play."
    assert stt('audio/test_audio_nine') == "The chef prepared a delicious meal for the guests."
    assert stt('audio/test_audio_ten') == "They decided to take a road trip across the country."





