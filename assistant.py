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

import pyttsx3
import speech_recognition as sr

from tools import toolLib

# from gtts import gTTS
# from playsound import playsound


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

    def keep_asking(self, method="voice"):
        """
        This function makes the assistant keep asking the user commands i.e. not terminates after the given task is compeleted.
        """
        while True:
            take_command(method=method)

    def play_video(self, file_name):
        pass

    def terminal_command(self, command):
        pass

    def current_time(self):
        pass


features = Features()


def speak(audio):
    """
    Speaks the string provided.
    """
    # tts = gTTS(text=audio, lang='en')
    # tts.save("assistant.mp3")
    # playsound("assistant.mp3")

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
    speak("I am Jarvis! How can I help you?")
    # wish()

    take_command(method="console")
    # features.keep_asking(method="console")

    # take_command()
    # features.keep_asking()
