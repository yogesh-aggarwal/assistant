import os
import random
import webbrowser

from api import chatbot, games, search
from api.play import apiMusic, apiVideo

from exception import QueryError
from sql_tools import sqlite
from tools.behaviour import terminate

from . import synthesis as syn
from . import toolLib as tools_lib
from . import web as web_tools
from .constants import dbAttributes, dbProgramInstallData, greetKeywords, webDomains

Tools = tools_lib.Tools()
Web = web_tools.Web()
Search = tools_lib.Search()


class Analyse:
    """
    Class that contains analysis tools for the query provided.
    """

    def __init__(self, query, platform):
        self.query = query
        self.platform = platform.lower()

    def parse(self):
        query = self.query

        # For words at start
        words = ("hey", "jycore", "please", "can", "may", "you")
        for word in words:
            if Tools.reOperation(query.lower(), word, "at start"):
                query = query.lower().replace(word, "", 1).strip()

        # For words at start
        words = (
            "please",
            "for me",
            "for us",
            "for friends",
            "for my friends",
            "for our friends",
            "for family",
            "for my family",
            "for our family",
            "for family",
            "for my family",
            "for our family",
            "for family members",
            "for my family members",
            "for our family members",
            "",
        )
        for word in words:
            if Tools.reOperation(query.lower(), word, "at end"):
                query = query.lower().replace(word, "", 1).strip()

        del words
        self.query = query
        self.classify()

    @staticmethod
    def test():
        # from api.calendar import Calendar
        pass

    def classify(self, webDomains=webDomains):
        """
        Classifies the string provided to different categories.
        """
        query = self.query

        # Open program
        if Tools.reOperation(query, "open", "at start"):
            self.openClassify(query.replace("open ", "", 1))

        # Play content
        elif Tools.reOperation(query, "play", "at start"):
            self.playClassify(query.replace("play ", ""))

        # Search content
        elif Tools.reOperation(query, "search", "at start"):
            var = Search()
            var.classify(query)

        # Open web
        elif Tools.reOperation(query, "go to", "at start"):
            query = (
                query.replace("go to", "", 1)
                .replace("https://", "", 1)
                .replace("http://", "", 1)
                .replace(" ", "")
            )
            domain = Web.findDomain(query)
            if domain != "err_no_connection":
                if domain != "Webpage does not exists":
                    webbrowser.open_new_tab("https://" + query + domain)

            else:
                syn.speak("You don't have internet connection")

        # Other search for questions on Google
        elif query.split(" ")[0].upper() in Tools.strTolst(
            sqlite.execute(db=dbAttributes, command="SELECT * FROM KEYWORDS;").get[0][
                0
            ][0][1]
        ):
            # SCRAP GOOGLE TO GET RESULTS
            result = chatbot.Question().checkQuestion(query)
            syn.speak(result) if result else syn.speak(search.Web().google(query))

        # Game
        elif "game" in query:
            games.init()

        # Exiting
        elif query == "exit":
            terminate()  # Terminating tracking session
            syn.speak("See you again.")
            quit(1)

        # Testing query
        elif "test" in query:
            query = query.replace("test", "", 1).lower().strip()
            self.playClassify(query.replace("open", "", 1))

        else:
            # Not understood
            syn.speak(
                "I am not able to understand your query at the moment. Please try after future updates."
            )

    def openClassify(self, query):
        """
        Classifies the query containing "open" keyword.
        """
        if self.platform == "windows":
            # Try whether the application is present on machine or not.
            try:
                query = query.lower().strip().capitalize()
                # Getting the location of the program
                ls = (
                    "name",
                    "shortName1",
                    "shortName2",
                    "shortName3",
                    "shortName4",
                    "shortName5",
                    "shortName6",
                    "shortName7",
                    "shortName8",
                    "shortName9",
                )
                opened = False
                for count, i in enumerate(ls):
                    try:
                        (
                            applicationName,
                            location,
                            locationMethod,
                            openMethod,
                        ) = sqlite.execute(
                            db=dbProgramInstallData,
                            command=f'SELECT fileName, location, locationMethod, openMethod FROM PROGRAMS_DATA_WIN32 WHERE {i}="{query}"',
                            err=False,
                        ).get[
                            0
                        ][
                            0
                        ]
                        if (
                            not applicationName
                            or not location
                            or not locationMethod
                            or not openMethod
                        ):
                            continue

                        if locationMethod == "user":
                            # Application is dependent of user home path
                            if openMethod == "exe":
                                # Application is executable
                                os.startfile(
                                    f"{Tools.getUserPath}\\{location}\\{applicationName}"
                                )
                                syn.speak(random.choice(greetKeywords))
                            else:
                                # Application will open with system command
                                os.system(applicationName)

                        else:
                            # Application is independent of user home path
                            if openMethod == "exe":
                                # Application is executable
                                os.startfile(f"{location}\\{applicationName}")
                                syn.speak(random.choice(greetKeywords))
                            else:
                                # Application will open with system command
                                os.system(applicationName)

                        opened = True
                        break

                    except Exception as e:
                        if count == len(ls) - 1:
                            if (
                                str(e)
                                != "index 0 is out of bounds for axis 0 with size 0"
                            ):
                                raise FileNotFoundError("Application doesn't exists")

                if not opened:
                    raise FileNotFoundError

            # Checking for webpage
            except Exception:
                if Tools.reOperation(query, "Webpage", "at start"):
                    if Web(query).checkConnection():
                        if Web(query).checkWebExists():
                            print("Open webpage")
                    else:
                        print("Webpage does not exists")

                else:
                    query = (
                        query.replace("go to", "", 1)
                        .replace("https://", "", 1)
                        .replace("http://", "", 1)
                        .replace(" ", "")
                    )
                    domain = Web.findDomain(query)
                    for i in webDomains:
                        query = query.replace(i, "")

                    if domain:
                        webbrowser.open_new_tab(f"https://{query}{domain}")
                    else:
                        syn.speak("You don't have internet connection")

        elif self.platform == "linux":
            query = query.lower().strip().capitalize()
            ls = (
                "name",
                "shortName1",
                "shortName2",
                "shortName3",
                "shortName4",
                "shortName5",
            )

            data = None
            for i in ls:
                result = sqlite.execute(
                    f"SELECT command FROM PROGRAMS_DATA_LINUX WHERE {i}='{query.capitalize()}'",
                    db="data/database/programInstallData.db",
                    err=False,
                ).get
                if result:
                    data = result
                    del result
                    break

            if data:
                command = data[0][0][0]
                os.system(command)
            else:
                syn.speak("The program you have demanded is not found on your device")

        else:
            syn.speak(
                "The operating system is not supported for such type of operations"
            )

    @staticmethod
    def playClassify(query):
        """
        Classifies the query containing "play" keyword.
        """
        wordList = query.split(" ")
        service = None

        query = " ".join(wordList)

        try:
            query = query.replace("youtube music", "youtubeMusic")
        except Exception:
            pass

        wordList = query.split(" ")

        for i in [" on", " in", " at", " with"]:
            if Tools.reOperation(" ".join(wordList[: len(wordList) - 1]), i, "at end"):
                service = wordList[-1]
                query = query.replace(i, "", -1).replace(service, "", -1)
                break

        services = {
            # Video services
            "youtube": apiVideo().youtube,
            # Music services
            "gaana": apiMusic().gaana,
            "spotify": apiMusic().spotify,
            "youtubeMusic": apiMusic().youtubeMusic,
        }

        # Redirecting to service
        if Web.checkConnection():
            try:
                services[service](query)
            except QueryError:
                if service is not None:
                    syn.speak(
                        f"No result found for your query so I am opening it on YouTube"
                    )
                services["youtube"](query, openLink=True)
                syn.speak(random.choice(greetKeywords))
            except Exception:
                if service is not None:
                    syn.speak(
                        f"{service} is not supported yet so I am opening it on YouTube"
                    )
                services["youtube"](query, openLink=True)
                syn.speak(random.choice(greetKeywords))

        else:
            videoDir, musicDir = sqlite.execute(
                "SELECT value FROM USER_ATTRIBUTES WHERE name IN ('musicDirectory', 'videoDirectory')",
                db=dbAttributes,
            ).get.T[0][0]
            videoFiles = os.listdir(videoDir)
            musicFiles = os.listdir(musicDir)

            # TODO SEARCH HERE FOR MORE RELEVANT RESULTS
            os.startfile(os.path.join(videoDir, random.choice(videoFiles)))
