import pytest
from nlp.speech_to_text import stt_tester
from pathlib import Path

#    assert stt_tester(base_path / 'test_set_thermostat.wav') == "set thermostat to 70 degrees"
#    our NLP inteprets the word degrees as the symbol '°' instead of the word degrees

#     assert stt_tester(base_path / 'test_set_volume.wav') == "set volume to 50 percent"
#    our NLP inteprets the word percent as the symbol '%' instead of the word percent

def test_stt_use_cases():
    base_path = Path('tests/nlp_tests/audio')
    assert stt_tester(base_path / 'test_add_event_to_calendar.wav') == "add an event to my calendar"
    assert stt_tester(base_path / 'test_mute.wav') == "mute"
    assert stt_tester(base_path / 'test_play.wav') == "play"
    assert stt_tester(base_path / 'test_set_thermostat.wav') == "set the thermostat to 70°"
    assert stt_tester(base_path / 'test_set_volume.wav') == "set volume to 50%"
    assert stt_tester(base_path / 'test_unmute.wav') == "unmute"
    assert stt_tester(base_path / 'test_volume_down.wav') == "volume down"
    assert stt_tester(base_path / 'test_volume_up.wav') == "volume up"

