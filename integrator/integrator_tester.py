from nlp.speech_to_text import stt_tester
from nlp.text_processing import process_text
from pathlib import Path

def nlp_handler_tester(filepath: Path) -> list[str]:
    user_command = stt_tester(filepath)
    return process_text(user_command)
    