"""
Synthesis extention for Jarvis AI project.
"""

# import os
import pyttsx3
import speech_recognition as sr
import platform


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def listen():
    r = sr.Recognizer()
    r.pause_threshold = 1
    r.energy_threshold = 100
    with sr.Microphone() as source:
        print("\nListening...")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    query = None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}.")
        # return query
    except Exception as e:
        print(f"EXCEPTION (assistant.py) ---> {e}")
        if e:
            speak("Sorry about that, I didn't hear anything.")

    return query


def speak(s):
    """
    Speaks the string provided.
    """
    if platform.system() == "Windows":
        engine.say(s)
        engine.runAndWait()
    elif platform.system() == "Linux":
        print(s)
        # os.system(f"espeak '{s}'")
    else:
        print("Platform not supported")
