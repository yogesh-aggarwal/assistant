"""
Jycore AI project

Description:
    Jycore AI is the project opened for everyone to experience the power
    of Artitfial Intelligence. This project is based on Python Programming
    Language. To power machine learning & work properly, it uses internet
    connection. This project is created keeping in mind that the end-user
    should get a very nice experience & not face any problem in using it.

    This project is open-source as of now. If anybody wants to contribute
    to it, he/she is most welcome. Feel free to open any relevant issue
    (in case of feedback) or pull request.

    You can generalize your daily works with Jycore Assistant Project.

For more information read the docs...
"""

import datetime
import time

from colorama import init as ansi

from sql_tools import sqlite
from tools import synthesis as syn
from tools.analyse import Analyse
from tools.behaviour import init, terminate


ansi()


class Assistant:
    def __init__(self, method="voice", welcome=False, keep_asking=False, test_query=""):
        self.method = method
        self.welcome = welcome
        self.keep_asking = keep_asking
        self.test_query = test_query

        self.wish() if welcome else False

        self.start()

    def start(self):
        while self.keep_asking or self.test_query:
            # / Start tracking session
            init()
            # / Analyse query
            Analyse(self.query).parse()
            # / Terminate tracking session
            terminate()

    @staticmethod
    def wish():
        """
        Wishes the user according to the time.
        """
        hour = int(datetime.datetime.now().hour)
        if hour >= 0 and hour < 12:
            syn.speak("Good Morning!")
        elif hour >= 12 and hour < 18:
            syn.speak("Good Afternoon!")
        else:
            syn.speak("Good Evening!")
        # syn.speak("I am Jycore! Chip number 227O4CB, Memory one Terabytes. How can I help you?")
        syn.speak("I am Jycore! How can I help you?")

    def takeQuery(self):
        if self.method == "voice":
            return syn.listen()
        elif self.test_query:
            return self.test_query
        else:
            return input("Query: ")


if __name__ == "__main__":
    startTime = time.time()
    Assistant(
        method="console", welcome=False, keep_asking=True, test_query="open settings",
    )
    stopTime = time.time()
    print(f"[INFO] Elapsed time: {stopTime-startTime}s")
