import pytest
from nlp.speech_to_text import stt_tester
from pathlib import Path

def test_stt_use_cases():
    base_path = Path('tests/nlp_tests/audio')
    assert stt_tester(base_path / 'test_volume_down.wav') == "volume down"
    assert stt_tester(base_path / 'test_volume_up.wav') == "volume up"

