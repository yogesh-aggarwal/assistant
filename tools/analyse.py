import os
import random
import webbrowser

from api import chatbot, games, search
from api.play import apiMusic, apiVideo

from exception import QueryError
from tools.behaviour import terminate

from . import synthesis as syn
from . import toolLib as tools_lib
from . import web as web_tools
from .constants import dbAttributes, greetKeywords, webDomains
from .mongo_client import linux_install_programs, win32_install_programs
from .toolLib import String

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
            Search.classify(query)

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
        # FIXME: Temporary, get the question keywords from database
        elif query.split(" ")[0].upper() in ["What"]:
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
        query = query.strip().capitalize()

        # // Windows
        if self.platform == "windows":
            # Getting the program
            properties = win32_install_programs.find_one({"names": query})
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

        # // Linux
        elif self.platform == "linux":
            # Getting the program
            properties = linux_install_programs.find_one({"names": query})
            if not properties:
                syn.speak(
                    "Sorry to say your requested program is not found in my experience."
                )
                return False
            # Launching by command
            os.system(properties["command"])

        # // Platform Not Supported
        else:
            syn.speak(
                "The operating system is not supported for such type of operations"
            )
            return False

        return True

    @staticmethod
    def playClassify(query):
        """
        Classifies the query containing "play" keyword.
        """
        wordList = query.split(" ")
        service = None
        query = String.spaceToCamelcase(query)

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
        # // Online Service
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

        # // Offline Service
        else:
            videoDir, musicDir = ["", ""]
            videoFiles = os.listdir(videoDir)
            musicFiles = os.listdir(musicDir)

            # TODO: SEARCH HERE FOR MORE RELEVANT RESULTS
            os.startfile(os.path.join(videoDir, random.choice(videoFiles)))
