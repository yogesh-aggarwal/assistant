"""
Synthesis extention for Jarvis AI project.
"""

# import os

import speech_recognition as sr


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold = 1
        r.energy_threshold = 100
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
    # os.system(f"espeak '{s}'")
    print(s)
