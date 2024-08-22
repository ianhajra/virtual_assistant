from pathlib import Path
import speech_recognition as sr

def stt_tester(filepath: Path) -> str:
    r = sr.Recognizer()
    with sr.AudioFile(str(filepath)) as source:
        audio = r.record(source)

    # this uses google speech recognition, there are a bunch of other models available in this library
    try:
        speech = r.recognize_google(audio)
    except sr.UnknownValueError:
        speech = "Could not understand the audio"
    except sr.RequestError:
        speech = "Could not request results from the speech recognition service"

    return speech




