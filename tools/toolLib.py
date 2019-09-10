"""
An integrative library that contains the tools required to work the assistant.
    * Integrated with Assistant
    * Inbuilt feature of Jarvis AI Poject.
"""

import os
import random
import re
import webbrowser

import bs4
import requests

import chatbot as bot
from api.apiPlay import apiMusic, apiVideo
from sql_tools import sqlite

from . import behaviour as bh
from . import synthesis as syn
from .constants import (dbAttributes, dbProgramInstallData, dbServices,
                        greetKeywords, webDomains)


class Web:
    """
    Class that contains tools for the web operations.
    """

    def __init__(self, query=""):
        self.query = query
        self.__domain_presence = False

    @staticmethod
    def checkConnection(web_page=""):
        """
        Checks whether there is internet connection available or not. Returns boolean value as per the outcome.
        """
        try:
            if web_page:
                if "http://" in web_page:
                    web_page = web_page.replace.replace("https://", "").replace(
                        "http://", ""
                    )
                else:
                    web_page = "http://" + web_page

                request = requests.get(web_page)
                if request.status_code == 200:
                    return True
                else:
                    return False

            else:
                web_page = "https://google.com"
                request = requests.get(web_page)
                if request.status_code == 200:
                    return True
                else:
                    return False

            del web_page
        except Exception:
            return False

    def checkWebExists(self, query=""):
        """
        Checks the existance of the address provided.

        If there is connection return problem return "err_no_connection", else return True or False.

        Exists = True,
        Not exists = False
        """
        exist = False
        if not query:
            query = self.query.replace("webpage ", "")

        for domain in webDomains:
            domain = domain[0]
            if domain not in query:
                self.__domain_presence = False
            else:
                self.__domain_presence = True
                break

        for domain in webDomains:
            domain = domain[0]
            if not self.__domain_presence:
                try:
                    if self.checkConnection(query + domain):
                        query += domain
                        self.__domain_presence = True
                        exist = True
                        break
                    else:
                        self.__domain_presence = False
                except Exception:
                    pass
            else:
                if self.checkConnection(query):
                    exist = True
                    break
        if exist:
            return True
        else:
            return False

    def findDomain(self, query=""):
        """
        Finds the web domain of the name provided.

        If there is connection return problem return "err_no_connection", else return True or False.
        """
        for domain in webDomains:
            domain = domain[0]
            if Tools().reOperation(query, domain, "at end"):
                if Web().checkWebExists(query=query + domain) == True:
                    return domain
                elif Web().checkWebExists(query=query + domain) == False:
                    return False
                else:
                    return False
        else:
            return False


class Search:
    """
    Class that contains the search operation methods to perform various kinds of searching work efficiently.
    """

    def __init__(self):
        pass

    def classify(self, query=""):
        """
        Classfies the type of search query provided.
        """
        engines = sqlite.execute(
            "SELECT name FROM ENGINES",
            databPath=dbServices,
            matrix=False,
            inlineData=True,
            splitByColumns=True,
        )[0][0]

        query = query.lower().replace("search", "", 1).strip()
        wordList = query.split(" ")
        engine = None

        for i in range(len(wordList)):
            try:
                if wordList[0] in ["for", "at", "on"]:
                    wordList.pop(0)
            except Exception:
                pass

        for __engine in engines:
            if (
                wordList[0].capitalize() == __engine
            ):  # Check if the search engine is at the start of the query.
                queryType = "Search"
                for __engine in engines:
                    if (
                        wordList[-1].capitalize() == __engine
                    ):  # Checking if there is more than one engines present in the query, at start & at end.
                        if wordList[-2] in [
                            "on",
                            "at",
                        ]:  # Check if it contains the keywords that signifies that the word is the engine.
                            engine = wordList[-1].capitalize()
                            break
                        else:
                            engine = wordList[
                                0
                            ].capitalize()  # The search engine is at the start
                            break
                    else:
                        engine = wordList[
                            0
                        ].capitalize()  # The search engine is at the start

            elif (
                wordList[-1].capitalize() == __engine
            ):  # Checking if the searching engine is not at start but at the last.
                for __engine in engines:
                    if wordList[-2] in [
                        "on",
                        "at",
                    ]:  # Check if it contains the keywords that signifies that the word is the engine.
                        engine = wordList[-1].capitalize()
                        break
                    else:
                        engine = (
                            wordList[0].capitalize() if engine in engines else "Google"
                        )  # The search engine is at the start
                        if engine in engines:
                            break
                queryType = "search"
                break

            else:
                queryType = "not_search"

        if queryType == "Search":
            try:
                wordList.remove(engine.lower())
            except Exception:
                pass

            if wordList[0] in ["for", "at", "on"]:
                wordList.pop(0)
            if wordList[-1] in ["for", "at", "on"]:
                wordList.pop(-1)

            searchQuery = " ".join(wordList)

            if engine != None:
                self.searchEngine(query=searchQuery, engine=engine)
        else:
            syn.speak("I am unable to understand the query.")

    def searchEngine(self, query="", engine="Google"):
        """
        Opens the webpage by searching the provideed query on the specified search engine.
        If no engine is provided it will search the query on Google.
        """
        engine = engine.lower()
        query = query.replace(engine, "", 1)
        method = Tools().getSearchMethod(engine)
        webbrowser.open_new_tab(f"https://{engine}.com{method}{query}")


class Tools:
    """
    Class that contains some basic (misc.) tools.
    """

    def __init__(self):
        pass

    def getSearchMethod(self, engine=""):
        """
        Returns the search method of the specified search engine from the database.
        """
        # Get methods from sql database and map them to dicts.
        try:
            return sqlite.execute(
                databPath=dbServices,
                command=f"SELECT METHOD FROM ENGINES WHERE NAME='{engine.capitalize()}'",
                matrix=False,
            )[0][0][0]
        except Exception:
            return sqlite.execute(
                databPath=dbServices,
                command=f"SELECT METHOD FROM ENGINES WHERE NAME='Google'",
                matrix=False,
            )[0][0][0]

    def reOperation(self, query, string, method):
        """
        Performs some simple regular expressions operations on the specified query.
        """
        if type(string) is str:
            __temp = []
            __temp.append(string)
            string = __temp.copy()
            del __temp

        __temp = False
        for count in range(len(string)):
            if method == "at start":
                patt = re.compile(rf"^{string[count]}")
            elif method == "at end":
                patt = re.compile(rf"{string[count]}$")

            matches = patt.finditer(query)
            for match in matches:
                if match != None:
                    __temp = True
                else:
                    __temp = False

        if __temp:
            del __temp
            return True
        else:
            del __temp
            return False

    @property
    def getUserPath(self):
        from pathlib import Path

        return str(Path.home())

    @staticmethod
    def strTolst(query):
        intLst = (1, 2, 3, 4, 5, 6, 7, 8, 0)

        tempLst = (
            query.replace("[", "", 1)
            .replace("]", "", 1)
            .replace("(", "", 1)
            .replace(")", "", 1)
            .split(", ")
            .copy()
        )

        query = []
        for element in tempLst:
            try:
                if int(element) in intLst:
                    query.append(int(element))
                else:
                    query.append(element)
            except Exception:
                query.append(element)
        del intLst, tempLst
        return query


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
        words = ("hey", "jarvis", "please", "can", "may", "you")
        for word in words:
            if Tools().reOperation(query.lower(), word, "at start"):
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
            if Tools().reOperation(query.lower(), word, "at end"):
                query = query.lower().replace(word, "", 1).strip()

        del words
        self.query = query
        self.classify()

    def classify(self, webDomains=webDomains):
        """
        Classifies the string provided to different categories.
        """
        query = self.query

        # Open program
        if Tools().reOperation(query, "open", "at start"):
            self.openClassify(query.replace("open ", "", 1))
            bh.init()

        # Play content
        elif Tools().reOperation(query, "play", "at start"):
            self.playClassify(query.replace("play ", ""))
            bh.init()

        # Search content
        elif Tools().reOperation(query, "search", "at start"):
            var = Search()
            var.classify(query)
            bh.init()

        # Open web
        elif Tools().reOperation(query, "go to", "at start"):
            query = (
                query.replace("go to", "", 1)
                .replace("https://", "", 1)
                .replace("http://", "", 1)
                .replace(" ", "")
            )
            domain = Web().findDomain(query)
            if domain != "err_no_connection":
                if domain != "Webpage does not exists":
                    webbrowser.open_new_tab("https://" + query + domain)
                    bh.init()
            else:
                syn.speak("You don't have internet connection")

        # Other search for questions on Google
        elif query.split(" ")[0].upper() in Tools.strTolst(
            sqlite.execute(
                databPath=dbAttributes, command="SELECT * FROM KEYWORDS;", matrix=False
            )[0][0][1]
        ):
            # SCRAP GOOGLE TO GET RESULTS
            engine = "google"
            searchMethod = Tools().getSearchMethod(engine)
            link = "https://gaana.com/search/saaho"
            link = f"https://{engine}.com{searchMethod}{query}"

            headers = {
                "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
            }
            try:
                res = requests.get(link, headers=headers).text
                soup = bs4.BeautifulSoup(res, "lxml")

                try:
                    ans = soup.select(".Z0LcW")[0]
                except Exception:
                    syn.speak("No results found")
                    exit()

                syn.speak(f"{query} is {ans}")
            except Exception:
                syn.speak("You don't have internet connection")

        # Game
        elif "game" in query:
            import games

            games.init()

        # Exiting
        elif query == "exit":
            syn.speak("See you again.")
            quit(1)

        # Testing query
        elif "test" in query:
            bot.init()

        # Not understood
        else:
            syn.speak(
                "I am not able to understand your query at the moment. Please try after future updates."
            )

    def openClassify(self, query):
        """
        Classifies the query containing "open" keyword.
        """
        if self.platform == "Windows":
            # Try whether the application is present on machine or not.
            try:
                query = query.lower().capitalize()
                # Getting the location of the program
                try:
                    location = sqlite.execute(
                        databPath=dbProgramInstallData,
                        command=f'SELECT location FROM PROGRAMS_DATA WHERE name="{query}"',
                        matrix=False,
                    )[0][0][0]
                except Exception:
                    location = ""

                try:
                    if location != "":
                        applicationName = sqlite.execute(
                            databPath=dbProgramInstallData,
                            command=f'SELECT fileName FROM PROGRAMS_DATA WHERE name="{query}"',
                        )[0][0][0]
                        locationMethod = sqlite.execute(
                            databPath=dbProgramInstallData,
                            command=f'SELECT locationMethod FROM PROGRAMS_DATA WHERE name="{query}"',
                        )[0][0][0]
                        openMethod = sqlite.execute(
                            databPath=dbProgramInstallData,
                            command=f'SELECT openMethod FROM PROGRAMS_DATA WHERE name="{query}"',
                        )[0][0][0]

                        if locationMethod == "user":
                            # Application is dependent of user home path
                            if openMethod == "exe":
                                # Application is executable
                                os.startfile(
                                    f"{Tools().getUserPath}\\{location}\\{applicationName}"
                                )
                                syn.speak(random.choice(greetKeywords))
                            else:
                                # Application is of system
                                os.system(applicationName)
                        else:
                            # Application is independent of user home path
                            if openMethod == "exe":
                                # Application is executable
                                os.startfile(f"{location}\\{applicationName}")
                                syn.speak(random.choice(greetKeywords))
                            else:
                                # Application is of system
                                os.system(applicationName)
                    else:
                        # Checking for short names
                        for shortNameCount in range(1, 7):
                            # Getting location
                            try:
                                location = sqlite.execute(
                                    databPath=dbProgramInstallData,
                                    command=f'SELECT location FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                                )[0][0][0]
                            except Exception:
                                location = ""

                            if location != "":
                                applicationName = sqlite.execute(
                                    databPath=dbProgramInstallData,
                                    command=f'SELECT fileName FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                                )[0][0][0]
                                locationMethod = sqlite.execute(
                                    databPath=dbProgramInstallData,
                                    command=f'SELECT locationMethod FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                                )[0][0][0]
                                openMethod = sqlite.execute(
                                    databPath=dbProgramInstallData,
                                    command=f'SELECT openMethod FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                                )[0][0][0]

                                # Check whether the program opens according user home path
                                if locationMethod == "user":
                                    if openMethod == "exe":
                                        # Application is executable
                                        os.startfile(
                                            f"{Tools().getUserPath}\\{location}\\{applicationName}"
                                        )
                                        syn.speak(random.choice(greetKeywords))
                                        break
                                    else:
                                        # Application is of system
                                        os.system(applicationName)
                                        break
                                    break
                                else:
                                    # Independent of user home path
                                    if openMethod == "exe":
                                        # Application is executable
                                        os.startfile(f"{location}\\{applicationName}")
                                        syn.speak(random.choice(greetKeywords))
                                        break
                                    else:
                                        # Application is of system
                                        os.system(applicationName)
                                        break
                                    break
                            else:
                                if shortNameCount == 6:
                                    # Everything has been tried & application not found
                                    raise FileNotFoundError(
                                        "Application doesn't exists"
                                    )
                except Exception as e:
                    if str(e) != "index 0 is out of bounds for axis 0 with size 0":
                        raise FileNotFoundError("Application doesn't exists")
            # Checking for webpage
            except Exception:
                if Tools().reOperation(query, "webpage", "at start"):
                    if Web(query).checkConnection():
                        if Web(query).checkWebExists():
                            print("Open webpage")
                    else:
                        print("Webpage does not exists")

                elif Tools().reOperation(query, "my", "at start"):
                    query = query.replace("my", "", 1)
                    if "folder" in query:
                        query = query.replace("folder", "").replace(" ", "", 1)
                        # Add the user path to the folder name.
                        os.startfile(f"{os.path.expanduser('~')}\\{query}")

                    elif "favourate" in query:
                        query.replace("favourate", "")
                        if "video" in query:
                            # Get the file from the sql database.
                            file = r"test\files\video\vid_1.mp4"
                            os.startfile(file)
                        elif "music" or "song" in query:
                            # Get the file from the sql database.
                            file = r"test\files\music\mus_1.mp3"
                            os.startfile(file)
                        elif "image" or "photo" in query:
                            # Get the file from the sql database.
                            file = r"test\files\image\img_1.jpg"
                            os.startfile(file)

                else:
                    query = (
                        query.replace("go to", "", 1)
                        .replace("https://", "", 1)
                        .replace("http://", "", 1)
                        .replace(" ", "")
                    )
                    domain = Web().findDomain(query)
                    if domain:
                        webbrowser.open_new_tab("https://" + query + domain)
                    else:
                        syn.speak("You don't have internet connection")

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

        for i in [" on", " in", " at", " with"]:
            try:
                query = query.replace("youtube music", "youtubeMusic")
            except Exception:
                pass

        wordList = query.split(" ")

        for i in [" on", " in", " at", " with"]:
            if Tools().reOperation(
                " ".join(wordList[: len(wordList) - 1]), i, "at end"
            ):
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

        try:
            services[service](query)
        except Exception as e:
            print(e)
            if service is not None:
                syn.speak(f"{service} is not supported yet, I am opening it on YouTube")
            services["youtube"](query, openLink=True)
            syn.speak(random.choice(greetKeywords))


class Question:
    def __init__(self):
        self.quesType = ""

    def checkQuestion(self, query=""):
        """
        Checks whether the provided query is a question or not.
        """
        __temp = False
        qWords = (
            sqlite.execute(
                databPath=dbAttributes, command="SELECT * FROM KEYWORDS;", matrix=False
            )[0][0][1]
            .replace("(", "", 1)
            .replace(")", "", 1)
            .split(", ")
        )

        for word in qWords:
            if Tools().reOperation(query.upper(), word, "at start"):
                __temp = True
                self.quesType = word
                break

        self.quesType = self.quesType.lower()

        return __temp

    def analyse(self, query=""):
        pass
        # chatBot.AnalyseQuestion(self.quesType, query=query)
