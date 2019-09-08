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
import numpy as np
import requests

from sql_tools import sqlite
# import features.assist_games as games
# import features.chatBot as chatBot
# import features.faceRecognition as fr
from tools.apiPlay import apiMusic, apiVideo

from . import behaviour as bh
from . import synthesis as syn

webDomains = [".com", ".org", ".in", ".edu", ".net", ".arpa"]
# webDomains = sqlite.execute(databPath=r"data/database/services.db", command="SELECT USAGE FROM DOMAIN")
greetKeywords = np.array(
    [["Sure!", "Okay!", "Here it is", "Here is what you have demanded"]]
)


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

        If there is connection return problem return "No internet connection", else return True or False.

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

        If there is connection return problem return "No internet connection", else return True or False.
        """
        __domain_presence = False
        __domain = ""

        for domain in webDomains:
            domain = domain[0]
            if Tools().reOperation(query, domain, "at end"):
                __domain = domain
                __domain_presence = True
                break

        if not __domain_presence:
            for domain in webDomains:
                domain = domain[0]
                if Web().checkWebExists(query=query + domain) == True:
                    return domain
                elif Web().checkWebExists(query=query + domain) == False:
                    return False
                else:
                    return False
        else:
            return ""

    def playOnline(self, query, objType="video", service="YouTube", rand=False):
        if Web.checkConnection():
            import webbrowser

            webbrowser.open_new_tab(
                Search().videoSearch(query, service="YouTube", rand=rand)
            )
        else:
            # REMOVE IT IN FUTURE
            import webbrowser

            webbrowser.open_new_tab(
                Search().videoSearch(query, service="YouTube", rand=rand)
            )
            # syn.speak("You don't have internet connection!")


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
            databPath=r"data/database/services.db",
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
                queryType = "Search"
                break

            else:
                queryType = "Not search"

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

    def searchEngine(self, query="", engine="Google"):
        """
        Opens the webpage by searching the provideed query on the specified search engine.
        If no engine is provided it will search the query on Google.
        """
        engine = engine.lower()
        query = query.replace(engine, "", 1)
        method = Tools().getSearchMethod(engine)
        webbrowser.open_new_tab(f"https://{engine}.com{method}{query}")

    def videoSearch(self, query="", service="", rand=False):
        """
        Returns the url of the video of the trending(according to the database [services.db]) video engine. By default it opens the first video.
        """
        if not service:
            host = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT host FROM VIDEO_SERVICES WHERE rank=1",
            )[0][0][0]
        else:
            host = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT host FROM VIDEO_SERVICES WHERE name='{service}'",
            )[0][0][0]

        searchMethod = sqlite.execute(
            databPath=r"data/database/services.db",
            command=f"SELECT searchMethod FROM VIDEO_SERVICES WHERE host='{host}'",
        )[0][0][0]
        playMethod = sqlite.execute(
            databPath=r"data/database/services.db",
            command=f"SELECT playMethod FROM VIDEO_SERVICES WHERE host='{host}'",
        )[0][0][0]

        if not searchMethod:
            syn.speak(
                "The video service doesn't exists. So I am opening it on other service."
            )
            host = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT host FROM VIDEO_SERVICES WHERE rank=1",
            )[0][0][0]
            searchMethod = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT searchMethod FROM VIDEO_SERVICES WHERE rank=1",
            )[0][0][0]
            playMethod = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT playMethod FROM VIDEO_SERVICES WHERE rank=1",
            )[0][0][0]

        link = f"{host}{searchMethod}{query}"

        res = requests.get(f"{host}{searchMethod}{query}").text
        soup = bs4.BeautifulSoup(res, "lxml")
        links = []
        for link in soup.find_all("a", href=True):
            links.append(link["href"])

        vids = []
        for link in links:
            if playMethod in link:
                vids.append(link)
                if not rand:
                    break

        if rand:
            return f"{host}{random.choice(vids)}"
        else:
            return f"{host}{vids[0]}"


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
                databPath=r"data/database/services.db",
                command=f"SELECT METHOD FROM ENGINES WHERE NAME='{engine.capitalize()}'",
                matrix=False,
            )[0][0][0]
        except Exception:
            return sqlite.execute(
                databPath=r"data/database/services.db",
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
            if domain != "No internet connection":
                if domain != "Webpage does not exists":
                    webbrowser.open_new_tab("https://" + query + domain)
                    bh.init()
            else:
                syn.speak("No internet connection")

        # Other search for questions on Google
        elif query.split(" ")[0].upper() in Tools.strTolst(
            sqlite.execute(
                databPath=r"data/database/attributes.db",
                command="SELECT * FROM KEYWORDS;",
                matrix=False,
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
                syn.speak("No internet connection")

        # Exiting
        elif query == "exit":
            syn.speak("See you again.")
            quit(1)

        # Testing query
        elif "test" in query:
            print(Question().checkQuestion(query=query.replace("test ", "")))

        # Not understood
        else:
            syn.speak(
                "I am not able to understand your query at the moment. Please try after future updates."
            )

    @staticmethod
    def openClassify(query):
        """
        Classifies the query containing "open" keyword.
        """
        try:
            query = query.lower().capitalize()
            try:
                location = sqlite.execute(
                    databPath=r"data/database/programInstallData.db",
                    command=f'SELECT location FROM PROGRAMS_DATA WHERE name="{query}"',
                    matrix=False,
                )[0][0][0]
            except Exception:
                location = ""
            try:
                if location != "":
                    applicationName = sqlite.execute(
                        databPath=r"data/database/programInstallData.db",
                        command=f'SELECT fileName FROM PROGRAMS_DATA WHERE name="{query}"',
                    )[0][0][0]
                    locationMethod = sqlite.execute(
                        databPath=r"data/database/programInstallData.db",
                        command=f'SELECT locationMethod FROM PROGRAMS_DATA WHERE name="{query}"',
                    )[0][0][0]
                    openMethod = sqlite.execute(
                        databPath=r"data/database/programInstallData.db",
                        command=f'SELECT openMethod FROM PROGRAMS_DATA WHERE name="{query}"',
                    )[0][0][0]
                    if locationMethod == "user":
                        if openMethod == "exe":
                            os.startfile(
                                f"{Tools().getUserPath}\\{location}\\{applicationName}"
                            )
                            syn.speak(random.choice(greetKeywords[0]))
                        else:
                            os.system(applicationName)
                    else:
                        if openMethod == "exe":
                            os.startfile(f"{location}\\{applicationName}")
                            syn.speak(random.choice(greetKeywords[0]))
                        else:
                            os.system(applicationName)
                else:
                    for shortNameCount in range(1, 7):
                        try:
                            location = sqlite.execute(
                                databPath=r"data/database/programInstallData.db",
                                command=f'SELECT location FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                            )[0][0][0]
                        except Exception:
                            location = ""

                        if location != "":
                            applicationName = sqlite.execute(
                                databPath=r"data/database/programInstallData.db",
                                command=f'SELECT fileName FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                            )[0][0][0]
                            locationMethod = sqlite.execute(
                                databPath=r"data/database/programInstallData.db",
                                command=f'SELECT locationMethod FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                            )[0][0][0]
                            openMethod = sqlite.execute(
                                databPath=r"data/database/programInstallData.db",
                                command=f'SELECT openMethod FROM PROGRAMS_DATA WHERE shortName{shortNameCount}="{query}"',
                            )[0][0][0]

                            if locationMethod == "user":
                                if openMethod == "exe":
                                    os.startfile(
                                        f"{Tools().getUserPath}\\{location}\\{applicationName}"
                                    )
                                    syn.speak(random.choice(greetKeywords[0]))
                                    break
                                else:
                                    os.system(applicationName)
                                    break
                                break
                            else:
                                if openMethod == "exe":
                                    os.startfile(f"{location}\\{applicationName}")
                                    syn.speak(random.choice(greetKeywords[0]))
                                    break
                                else:
                                    os.system(applicationName)
                                    break
                                break
                        else:
                            if shortNameCount == 6:
                                raise FileNotFoundError("Application doesn't exists")
            except Exception as e:
                if str(e) != "index 0 is out of bounds for axis 0 with size 0":
                    raise FileNotFoundError("Application doesn't exists")

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

    @staticmethod
    def playClassify(query):
        """
        Classifies the query containing "play" keyword.
        """
        if "video" in query:
            # Get the greet keywords from the sql database.
            # print("Playing")
            syn.speak(random.choice(greetKeywords[0]))
            video_folder = sqlite.execute(
                databPath=r"data/database/attributes.db",
                command="SELECT value FROM USER_ATTRIBUTES WHERE name='videoDirectory'",
                matrix=False,
                inlineData=True,
            )[0][0][0]

            if not video_folder:
                # Link to different video services. Get the preferred service from the user database if available.
                pass
            else:
                # Get the folder path from the sql database.
                files = os.listdir(video_folder)
                os.startfile(f"{video_folder}/{random.choice(files)}")

        elif "music" in query or "song" in query:
            if Tools().reOperation(query, ["music", "song"], "at start"):
                syn.speak(random.choice(greetKeywords[0]))

                music_folder = sqlite.execute(
                    databPath=r"data/database/attributes.db",
                    command="SELECT value FROM USER_ATTRIBUTES WHERE name='musicDirectory'",
                    matrix=False,
                    inlineData=True,
                )[0][0][0]

                if not music_folder:
                    print("No folder available for playing song.")
                    Web().playOnline(query, objType="music")
                    # Link to different music services. Get the preferred service from the user database if available.
                else:
                    # Get the folder path from the sql database.
                    try:
                        files = os.listdir(music_folder)
                        os.startfile(f"{music_folder}/{random.choice(files)}")
                    except:
                        Web().playOnline("latest songs", rand=True)

            else:
                Web().playOnline(query)
                syn.speak(random.choice(greetKeywords[0]))

        elif "game" in query:
            # import game module and use the different classes for different games.
            # games.Games.choice()
            pass

        else:
            musicServices = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT name FROM MUSIC_SERVICES",
                splitByColumns=True,
            )[0][0]
            videoServices = sqlite.execute(
                databPath=r"data/database/services.db",
                command=f"SELECT name FROM VIDEO_SERVICES",
                splitByColumns=True,
            )[0][0]
            wordList = query.split(" ")
            __temp = wordList.copy()
            __temp.pop(-1)
            service = None

            query = " ".join(__temp)
            for i in [" on", " in", " at", " with"]:
                if Tools().reOperation(" ".join(__temp), i, "at end"):
                    service = wordList[-1]
                    query = query.replace(i, "", -1)
                    break

            if service == "gaana":
                apiMusic.gaana(query)

            else:
                Web().playOnline(
                    query,
                    objType="music",
                    service=sqlite.execute(
                        databPath=r"data/database/services.db",
                        command=f"SELECT name FROM MUSIC_SERVICES WHERE rank=1",
                    )[0][0][0],
                )
                syn.speak(random.choice(greetKeywords[0]))


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
                databPath=r"data/database/attributes.db",
                command="SELECT * FROM KEYWORDS;",
                matrix=False,
            )[0][0][1]
            .replace("(", "", 1)
            .replace(")", "", 1)
            .split(", ")
        )

        print(qWords)

        for word in qWords:
            if Tools().reOperation(query.upper(), word, "at start"):
                __temp = True
                self.quesType = word
                break

        self.quesType = self.quesType.lower()
        print(self.quesType)

        return __temp

    def analyse(self, query=""):
        pass
        # chatBot.AnalyseQuestion(self.quesType, query=query)
