import pytest
from nlp.speech_to_text import stt
from nlp.text_processing import process_text
from pathlib import Path

def test_combined():
    base_path = Path('tests/nlp_tests/audio')
    assert process_text(stt(base_path / 'test_audio_one.wav')) == "cat sat windowsill watching birds outside"
    assert process_text(stt(base_path / 'test_audio_two.wav')) == "test longer sentence"
    assert process_text(stt(base_path / 'test_audio_three.wav')) == "meeting rescheduled next thursday"
    assert process_text(stt(base_path / 'test_audio_four.wav')) == "enjoys reading books ancient history"
    assert process_text(stt(base_path / 'test_audio_five.wav')) == "sunset painted sky shades orange pink"
    assert process_text(stt(base_path / 'test_audio_six.wav')) == "help find nearest coffee shop"
    assert process_text(stt(base_path / 'test_audio_seven.wav')) == "weather forecast predicts rain later afternoon"
    assert process_text(stt(base_path / 'test_audio_eight.wav')) == "quickly finished homework going play"
    assert process_text(stt(base_path / 'test_audio_nine.wav')) == "chef prepared delicious meal guests"
    assert process_text(stt(base_path / 'test_audio_ten.wav')) == "decided take road trip across country"
