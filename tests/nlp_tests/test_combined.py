import pytest
from nlp.speech_to_text import stt
from nlp.text_processing import process_text
from pathlib import Path

def test_combined():
    base_path = Path('tests/nlp_tests/audio')
    assert process_text(stt(base_path / 'test_audio_one.wav')) == ['cat', 'sat', 'windowsil', 'watch', 'bird', 'outsid']
    assert process_text(stt(base_path / 'test_audio_two.wav')) == ['test', 'longer', 'sentenc']
    assert process_text(stt(base_path / 'test_audio_three.wav')) == ['meet', 'reschedul', 'next', 'thursday']
    assert process_text(stt(base_path / 'test_audio_four.wav')) == ['enjoy', 'read', 'book', 'ancient', 'histori']
    assert process_text(stt(base_path / 'test_audio_five.wav')) == ['sunset', 'paint', 'sky', 'shade', 'orang', 'pink']
    assert process_text(stt(base_path / 'test_audio_six.wav')) == ['help', 'find', 'nearest', 'coffe', 'shop']
    assert process_text(stt(base_path / 'test_audio_seven.wav')) == ['weather', 'forecast', 'predict', 'rain', 'later', 'afternoon']
    assert process_text(stt(base_path / 'test_audio_eight.wav')) == ['quickli', 'finish', 'homework', 'go', 'play']
    assert process_text(stt(base_path / 'test_audio_nine.wav')) == ['chef', 'prepar', 'delici', 'meal', 'guest']
    assert process_text(stt(base_path / 'test_audio_ten.wav')) == ['decid', 'take', 'road', 'trip', 'across', 'countri']
