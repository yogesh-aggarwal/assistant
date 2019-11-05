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
import platform
from tools import synthesis as syn

from sql_tools import sqlite
from tools_lib import bprint
from tools.behaviour import terminate
from tools.toolLib import Analyse


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
    # syn.speak("I am Jarvis! Chip number 227O4CB, Memory one Terabytes. How can I help you?")
    syn.speak("I am Jarvis! How can I help you?")


def main(method="voice", welcome=False, keep_asking=False):
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
                query = input("Query: ")
            try:
                analysis = Analyse(query, platform=platform.system())
                analysis.parse()

                if "test" not in query:
                    solved = input("Solved? ")
                    if not solved:
                        solved = "true"
                    else:
                        solved = "false"

                    sqlite.execute(
                        f"INSERT INTO HISTORY VALUES('{query}', '{solved}')",
                        databPath=r"data/database/history.db",
                    )
            except Exception as e:
                if "test" not in query:
                    sqlite.execute(
                        f"INSERT INTO HISTORY VALUES('{query}', 'false')",
                        databPath=r"data/database/history.db",
                    )
                    # print(sqlite.execute("SELECT * FROM HISTORY", databPath=r"data/database/history.db")[0])
                    print(
                        sqlite.execute(
                            "SELECT * FROM HISTORY WHERE solved='false'",
                            databPath=r"data/database/history.db",
                        )[0]
                    )
                raise e

            terminate()
            if not keep_asking:
                break
    except Exception as e:
        bprint(e)
        # syn.speak("\nBye! See you again")


if __name__ == "__main__":
    main(method="console", welcome=False, keep_asking=False)
