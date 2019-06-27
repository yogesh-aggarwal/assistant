"""
Jarvis AI project.
    * Automates the tasks command by the user through speech.
    * Uses connectivity to work properly.

    Features-
        1) Send E-Mails.
        2) Plays music.
        3) Opens location.
        -- 4) Give terminal commands.
"""

import datetime

import speech_recognition as sr
from win32com.client import Dispatch

from tools import toolLib


def exit_assist():
    """
    This function helps in quitting the program even if it is the "keep asking" state or not.
    """
    speak("Bye! See you again.")
    quit()

def keep_asking(method="voice"):
    """
    This function makes the assistant keep asking the user commands i.e. not terminates after the given task is compeleted.
    """
    while True:
        take_command(method=method)


def speak(audio):
    """
    Speaks the string provided.
    """
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(audio)


def wish():
    """
    Wishes the user according to the time.
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    # speak("I am Jarvis! Chip number 227O4CB, Memory one Terabytes. How can I help you?")
    speak("I am Jarvis! How can I help you?")


def take_command(method="voice"):
    """
    It takes voice input from user and returns string version of it.
    """
    if method == "voice":
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening...")
            r.pause_threshold = 1
            r.energy_threshold = 100
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

    else:
        query = input("Enter the query ---> ").lower()

    try:
        analysis = toolLib.Analyse(query)
        analysis.classify()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    # speak("I am Jarvis! How can I help you?")
    # wish()

    take_command(method="console")
    # keep_asking(method="console")

    # take_command()
    # keep_asking()
