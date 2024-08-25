from nlp.speech_to_text import stt
from nlp.text_processing import process_text

# This will call stt and process_text in one function
def nlp_handler() -> list[str]:
    user_command = stt()
    return process_text(user_command)