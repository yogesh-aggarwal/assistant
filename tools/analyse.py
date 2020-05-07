import os
import platform
import random
import webbrowser

from api import chatbot, games, search
from api.play import apiMusic, apiVideo

from exception import QueryError
from tools.behaviour import terminate

from . import synthesis as syn
from . import toolLib as tools_lib
from . import web as web_tools
from .constants import greetKeywords, webDomains
from .mongo_client import linux_install_programs, win32_install_programs

Tools = tools_lib.Tools()
Web = web_tools.Web()
Search = tools_lib.Search()

PLATFORM = platform.system().lower()


class Analyse:
    """
    Class that contains analysis tools for the query provided.
    """

    def __init__(self, query):
        self.query = query

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

        # / Open program
        if Tools.reOperation(query, "open", "at start"):
            OpenClassify(query.replace("open ", "", 1)).classify()

        # / Play content
        elif Tools.reOperation(query, "play", "at start"):
            PlayClassify(query.replace("play ", "")).classify()

        # / Search content
        elif Tools.reOperation(query, "search", "at start"):
            Search.classify(query)

        # / Open web
        elif Tools.reOperation(query, "go to", "at start"):
            query = query.replace("go to", "", 1)
            # TODO: From here, Scrape google to get website URL

        # / Game
        elif "game" in query:
            games.init()

        # / EXTRA COMMANDS
        # Exiting
        elif query == "exit":
            terminate()  # Terminating tracking session
            syn.speak("See you again.")
            quit(1)

        # Testing query
        elif "test" in query:
            query = query.replace("test", "", 1).lower().strip()
            self.playClassify(query.replace("open", "", 1))

        # Other search for questions on Google
        else:
            # SCRAP GOOGLE TO GET RESULTS
            result = chatbot.Question().checkQuestion(query)
            syn.speak(result) if result else syn.speak(search.Web().google(query))


class OpenClassify:
    """
    Classifies the query containing "open" keyword.
    """

    def __init__(self, query):
        self.query = query.strip().capitalize()

    def classify(self):
        if PLATFORM == "windows":
            self.openWin32Program()
        elif PLATFORM == "linux":
            self.openLinuxProgram()
        else:
            syn.speak(
                "The operating system is not supported for such type of operations"
            )
            return False

    def openWin32Program(self):
        # Getting the program
        properties = win32_install_programs.find_one({"names": self.query})
        if not properties:
            syn.speak(
                "Sorry to say your requested program is not found in my experience."
            )
            return False

        OPEN_METHOD = properties["openMethod"]
        FILE_NAME = properties["fileName"]
        LOCATION_METHOD = properties["locationMethod"]

        if OPEN_METHOD == "exe":
            # Extracting only if the program is opened by exe not command
            LOCATION = properties["defaultInstallLocation"]
            # Application is dependent of user home path
            if LOCATION_METHOD == "user":
                # Application is executable
                os.startfile(f"{Tools.getUserPath}\\{LOCATION}\\{FILE_NAME}")
                syn.speak(random.choice(greetKeywords))
            else:
                # Application is independent of user home path
                os.startfile(f"{LOCATION}\\{FILE_NAME}")
                syn.speak(random.choice(greetKeywords))

        else:
            # Application is executable
            os.system(FILE_NAME)

    def openLinuxProgram(self):
        # Getting the program
        properties = linux_install_programs.find_one({"names": self.query})
        if not properties:
            syn.speak(
                "Sorry to say your requested program is not found in my experience."
            )
            return False
        # Launching by command
        os.system(properties["command"])


class PlayClassify:
    """
    Classifies the query containing "play" keyword.
    """

    def __init__(self, query):
        self.query = query
        self.service = None
        self.services = {
            # Video services
            "youtube": apiVideo().youtube,
            # Music services
            "gaana": apiMusic().gaana,
            "spotify": apiMusic().spotify,
            "youtubeMusic": apiMusic().youtubeMusic,
        }

    def classify(self):
        # Handling queries with service name having spaces
        self.normalizeQueryForServices()
        wordList = self.query.split(" ")

        for i in [" on", " in", " at", " with"]:
            if Tools.reOperation(" ".join(wordList[: len(wordList) - 1]), i, "at end"):
                self.service = wordList[-1]
                self.query = self.query.replace(i, "", -1).replace(self.service, "", -1)
                break

        if Web.checkConnection():
            self.playOnlineServices()
        else:
            self.playOfflineServices()

    def normalizeQueryForServices(self) -> None:
        services = {"youtube music": "youtubeMusic"}
        for service in services:
            self.query.replace(service, services[service])

    def playOnlineServices(self) -> bool:
        try:
            self.services[self.service](self.query)
        except QueryError:
            if self.service is not None:
                syn.speak(f"No result found for your so I am opening it on YouTube")
            self.services["youtube"](self.query, openLink=True)
            syn.speak(random.choice(greetKeywords))
        except Exception:
            if self.service is not None:
                syn.speak(
                    f"{self.service} is not supported yet so I am opening it on YouTube"
                )
            self.services["youtube"](self.query, openLink=True)
            syn.speak(random.choice(greetKeywords))

    def playOfflineServices(self) -> bool:
        videoDir, musicDir = ["", ""]
        videoFiles = os.listdir(videoDir)
        musicFiles = os.listdir(musicDir)

        # TODO: SEARCH HERE FOR MORE RELEVANT RESULTS
        os.startfile(os.path.join(videoDir, random.choice(videoFiles)))
        os.startfile(os.path.join(musicDir, random.choice(musicFiles)))
