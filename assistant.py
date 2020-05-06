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
import platform
from tools import synthesis as syn
from colorama import init as ansi

from sql_tools import sqlite
from tools.behaviour import init, terminate
from tools.toolLib import Analyse


ansi()


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


def askIfDesiredResult(q, ask=True):
    if ask:
        solved = input("Solved? ")
        if not solved:
            solved = "true"
        else:
            solved = "false"

        sqlite.execute(
            f"INSERT INTO HISTORY VALUES('{q}', '{solved}')",
            db=r"data/database/history.db",
        )
    else:
        sqlite.execute(
            f"INSERT INTO HISTORY VALUES('{q}', 'false')",
            db=r"data/database/history.db",
        )
        print(
            sqlite.execute(
                "SELECT * FROM HISTORY WHERE solved='false'",
                db=r"data/database/history.db",
            ).get[0]
        )

    return True


def main(method="voice", welcome=False, keep_asking=False, test_query=""):
    """
    Main block assistant assistant
    """
    try:
        if welcome:
            wish()

        while True:
            if method == "voice":
                query = syn.listen()
            else:
                if not test_query:
                    query = input("Query: ")
                else:
                    query = test_query

            init()  # Starting tracking session

            try:
                analysis = Analyse(query, platform=platform.system())
                analysis.parse()
                # askIfDesiredResult(query, t=True)
            except Exception as e:
                # askIfDesiredResult(query, f=True)
                raise e

            terminate()  # Terminating tracking session

            if not keep_asking or test_query:
                break
    except Exception as e:
        raise e
        syn.speak("\nBye! See you again")


if __name__ == "__main__":
    main(method="console", welcome=False, keep_asking=True, test_query="play slowly slowly")
    # Analyse.test()
