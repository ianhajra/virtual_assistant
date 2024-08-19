import pytest
from nlp.speech_to_text import stt
from pathlib import Path

def test_stt():
    base_path = Path('tests/nlp_tests/audio')
    assert stt(base_path / 'test_audio_one.wav') == "the cat sat on the windowsill watching the birds outside"
    assert stt(base_path / 'test_audio_two.wav') == "this is a test of a longer sentence"
    assert stt(base_path / 'test_audio_three.wav') == "the meeting has been rescheduled for next Thursday"
    assert stt(base_path / 'test_audio_four.wav') == "she enjoys reading books about ancient history"
    assert stt(base_path / 'test_audio_five.wav') == "the sunset painted the sky with shades of orange and pink"
    assert stt(base_path / 'test_audio_six.wav') == "can you help me find the nearest coffee shop"
    assert stt(base_path / 'test_audio_seven.wav') == "the weather forecast predicts rain later this afternoon"
    assert stt(base_path / 'test_audio_eight.wav') == "he quickly finished his homework before going out to play"
    assert stt(base_path / 'test_audio_nine.wav') == "the chef prepared a delicious meal for the guests"
    assert stt(base_path / 'test_audio_ten.wav') == "they decided to take a road trip across the country"