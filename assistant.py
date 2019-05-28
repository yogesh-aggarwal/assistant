"""
Jarvis AI project.
    Automates the tasks command by the user through speech.
    Uses connectivity to work properly.
    
    Features-
        1) Send E-Mails.
        2) Plays music.
        3) Opens location.
        -- 4) Give terminal commands.
"""

import datetime
import os
import random
import re
import webbrowser

import numpy as np
import pyttsx3
# import sqlite3  # For storing user preferences.
import requests
import speech_recognition as sr
import wikipedia

from tools import toolLib

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


class Features:
    """
    Class containing the features of the assistant. Can be used for accessing different features using its instants.
    """

    def __init__(self):
        pass

    def exit_assist(self):
        """
        This function helps in quitting the program even if it is the "keep asking" state or not.
        """
        speak("Bye! See you again.")
        quit()

    def keep_asking(self):
        """
        This function makes the assistant keep asking the user commands i.e. not terminates after the given task is compeleted.
        """
        while True:
            take_command()

    def send_email(self, email_address):
        pass

    def play_music(self, baseDir):
        files = os.listdir(baseDir)
        file = random.choice(files)
        print(f"baseDir ---> {baseDir}")
        print(f"file ---> {file}")
        os.startfile(os.path.join(baseDir, file))
        pass

    def play_video(self, file_name):
        pass

    def terminal_command(self, command):
        pass

    def current_time(self):
        pass

    def search_wiki(self, query):
        results = wikipedia.wikipedia.summary(query, sentences=2)
        print(results)
        speak(f"According to Wikipedia - {results}")

    def open_webpage(self, address):
        print(f"Opened ---> {address}")
        # for i in domains:
        #     try:
        #         address.replace(i, "")
        #     except:
        #         pass

        if ("http" not in address):
            webbrowser.open(f"http://{address}", new=2)
        else:
            webbrowser.open(address, new=2)


    def open_soft(self, soft_name):
        pass

features = Features()

def speak(audio):
    """
    Speaks the string provided.
    """
    engine.say(audio)
    engine.runAndWait()

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
    speak("I am Jarvis! Chip number 227O4CB, Memory one Terabytes. How can I help you?")
    # speak("I am Jarvis! How can I help you?")


def take_command():
    """
    It takes voice input from user and returns string version of it.
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User said: {query}.")
    except Exception as e:
        print(e)
        print("Sorry! could not recognise that. Say that again please.")
        # speak("Sorry! could not recognise that. Say that again please.")
        return None

    # analyse(query.lower())


if __name__ == "__main__":
    # wish()
    # take_command()
    # features.keep_asking()
    query = input("Enter the query ---> ").lower()

    analysis = toolLib.Analyse(query)
    analysis.classify()
    
    # analyse("play")