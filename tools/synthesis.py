"""
Synthesis extention for Jycore AI project.
"""

# import os
import speech_recognition as sr
from google_speech import Speech
from .constants import language


def listen():
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.energy_threshold = 100
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    query = None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}.")
        # return query
    except Exception as e:
        print(f"EXCEPTION (tools.synthesis) ---> {e}")
        if e:
            speak("Sorry about that, I didn't hear anything.")

    return query


def speak(line):
    """
    Speaks the string provided.
    """
    try:
        speech = Speech(line, language)
        soxEffects = ("speed", "1.1")
        speech.play(soxEffects)
    except Exception:
        print("Error while speaking!")
