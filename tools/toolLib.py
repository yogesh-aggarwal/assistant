import os
import random
import re
import webbrowser

import bs4
import numpy as np
import requests

import assistant
import features.assist_games as games
import features.chatBot as chatBot
import features.faceRecognition as fr
from tools.sql_operation import Sqlite3

# Garbage
# web_domains = np.array([".com", ".in", ".org", ".net",
#                         ".edu", ".int", ".gov", ".mil", ".arpa"])
web_domains = Sqlite3(databPath=r"data\database\services.db").execute(
    "SELECT USAGE FROM DOMAIN")
greet_keywords = np.array(
                [["Sure!", "Okay!", "Here it is", "Here is what you have demanded"]])


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
                    web_page = web_page.replace.replace(
                        "https://", "").replace("http://", "")
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
        except:
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

        if self.checkConnection():
            for domain in web_domains:
                domain = domain[0]
                if domain not in query:
                    self.__domain_presence = False
                else:
                    self.__domain_presence = True
                    break

            for domain in web_domains:
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
                    except:
                        pass
                else:
                    if self.checkConnection(query):
                        exist = True
                        break
            if exist:
                return True
            else:
                return False
        else:
            return "No internet connection"
            # print("No internet connection")

    def findDomain(self, query=""):
        """
        Finds the web domain of the name provided.

        If there is connection return problem return "No internet connection", else return True or False.
        """
        __domain_presence = False
        __domain = ""

        for domain in web_domains:
            domain = domain[0]
            if Tools().reOperation(query, domain, "at end"):
                __domain = domain
                __domain_presence = True
                break

        if not __domain_presence:
            for domain in web_domains:
                domain = domain[0]
                if Web().checkWebExists(query=query + domain) == True:
                    return domain
                elif Web().checkWebExists(query=query + domain) == False:
                    return "Webpage doesn't exists."
                else:
                    return "No internet connection"
        else:
            return ""


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
        # Get it from the database and save it in the form of numpy array before using it.
        sql = Sqlite3(
            databPath=r"F:\Python\AI\assistant\data\database\services.db")
        # print(sql)

        engines = np.array(["google", "bing", "ask", "yahoo", "youtube"])
        services = np.array(["youtube.com", "ganna.com"])

        patt = re.compile(r"^search")

        matches = patt.finditer(query)

        replace = False

        for match in matches:
            if match.span():
                replace = True

        if replace:
            query = query.replace("search", "", 1)
        del replace

        engine = ""
        wordList = re.sub(r"[^\w]", " ",  query).split()

        for engine_test in engines:
            if wordList[0] == engine_test:
                engine = engine_test
                break

        for count in range(2):
            if engine:
                garbage = np.array(["for", "at", "on"])
                for word in garbage:
                    query = query.replace(word, "", 1)
                del garbage
                self.searchEngine(query=query, engine=engine)
                break
            else:
                for engine_test in engines:
                    if wordList[len(wordList)-1] == engine_test:
                        engine = engine_test
                        break

        if engine not in engines:
            garbage = np.array(["for", "at", "on"])
            for word in garbage:
                query = query.replace(word, "", 1)
            del garbage
            self.searchEngine(query=query)

        elif True:
            # More search methods
            pass

    def searchEngine(self, query="", engine="google"):
        """
        Opens the webpage by searching the provideed query on the specified search engine.
        If no engine is provided it will search the query on Google.
        """
        query = query.replace(engine, "", 1)
        method = Tools().getSearchMethod(engine)
        webbrowser.open_new_tab(f"https://{engine}.com{method}{query}")

    def youtubeVideoSearch(self, query=""):
        """
        Opens the youtube video to the provided search query. By default it opens the first video.
        """
        res = requests.get(f"https://youtube.com{Tools().getSearchMethod('youtube')}{query}").text
        soup = bs4.BeautifulSoup(res, "lxml")
        links = []
        for link in soup.find_all("a", href=True):
            links.append(link["href"])
        vid = ""

        for link in links:
            if "/watch?v=" in link:
                vid = link
                break

        return f"https://www.youtube.com{vid}"


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
            return Sqlite3(databPath=r"data\database\services.db").execute(f"SELECT METHOD FROM ENGINES WHERE NAME='{engine.capitalize()}'")[0][0]
        except:
            return Sqlite3(databPath=r"data\database\services.db").execute(f"SELECT METHOD FROM ENGINES WHERE NAME='Google'")[0][0]

    def reOperation(self, query, string, method):
        """
        Performs some simple regular expressions operations on the specified query.
        """
        # print(f"re ---> query ---> {query}")
        # print(f"re ---> string ---> {string}")
        __temp = False
        if method == "at start":
            patt = re.compile(rf"^{string}")
        elif method == "at end":
            patt = re.compile(rf"{string}$")
        
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
    
    def getUserPath(self):
        from pathlib import Path
        return str(Path.home())

    def strTolst(self, query):
        intLst = (1, 2, 3, 4, 5, 6, 7, 8, 0)

        tempLst = query.replace("[", "").replace("]", "").split(", ").copy()

        query = []
        for element in tempLst:
            try:
                if int(element) in intLst:
                    query.append(int(element))
                else:
                    query.append(element)
            except:
                query.append(element)
        del intLst, tempLst
        return query

class Analyse():
    """
    Class that contains analysis tools for the query provided.
    """
    def __init__(self, query):
        self.query = query

    def classify(self, web_domains=web_domains):
        """
        Classifies the string provided to different categories.
        """
        query = self.query

        if Tools().reOperation(query, "open", "at start"):
            self.openClassify(query.replace("open ", "", 1))
        elif Tools().reOperation(query, "play", "at start"):
            self.playClassify(query.replace("play ", ""))
        elif Tools().reOperation(query, "search", "at start"):
            var = Search()
            var.classify(query)
        elif Tools().reOperation(query, "go to", "at start"):
            query = query.replace("go to", "", 1).replace(
                "https://", "", 1).replace("http://", "", 1).replace(" ", "")
            domain = Web().findDomain(query)
            if domain != "No internet connection":
                if domain != "Webpage does not exists":
                    webbrowser.open_new_tab("https://" + query + domain)
            else:
                # print("Error")
                assistant.speak("No internet connection")
        # elif query == "test":
        # elif Tools().reOperation(query, "test", "at start"):
        #     print(Question().checkQuestion(query=query.replace("test ---> ", "", 1)))
        elif query.split(" ")[0].upper() in tuple(Sqlite3(databPath=r"data\database\attributes.db").execute("SELECT * FROM KEYWORDS;")[0][1].replace("(", "", 1).replace(")", "", 1).split(", ")):
            Search().searchEngine(query=query)
        else:
            assistant.speak(
                "I am not able to understand your query at the moment. Please try after future updates.")

    @staticmethod
    def openClassify(query):
        """
        Classifies the query containing "open" keyword.
        """
        if True:
            query = query.lower().capitalize()
            location = Sqlite3(databPath=r"data\database\programInstallData.db").execute(f'SELECT location FROM PROGRAMS_DATA WHERE name="{query}"')[0][0]
            try:
                if location != "":
                    applicationName = Sqlite3(databPath=r"data\database\programInstallData.db").execute(f'SELECT fileName FROM PROGRAMS_DATA WHERE name="{query}"')[0][0]
                    os.startfile(f"{Tools().getUserPath()}\\{location}\\{applicationName}")
                    assistant.speak(random.choice(greet_keywords[0]))
                else:
                    location = Sqlite3(databPath=r"data\database\programInstallData.db").execute(f'SELECT location FROM PROGRAMS_DATA WHERE shortName="{query}"')[0][0]
                    if location != "":
                        applicationName = Sqlite3(databPath=r"data\database\programInstallData.db").execute(f'SELECT fileName FROM PROGRAMS_DATA WHERE shortName="{query}"')[0][0]
                        os.startfile(f"{Tools().getUserPath()}\{location}\{applicationName}")
                        assistant.speak(random.choice(greet_keywords[0]))
                    else:
                        raise ValueError
            except Exception as e:
                print(f"EXCEPTION ---> {e}")
            # First check for the programs available on the machine.
            pass
        elif Tools().reOperation(query, "webpage", "at start"):
            if Web(query).checkWebExists() == "No internet connection":
                assistant.speak("No internet connection")
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
            query = query.replace("go to", "", 1).replace(
                "https://", "", 1).replace("http://", "", 1).replace(" ", "")
            domain = Web().findDomain(query)
            if domain != "Webpage doesn't exists.":
                webbrowser.open_new_tab("https://" + query + domain)
            else:
                print(domain)



    @staticmethod
    def playClassify(query):
        """
        Classifies the query containing "play" keyword.
        """
        if "video" in query:
            # Get the greet keywords from the sql database and convert it to numpy array before using it.
            # print("Playing")
            assistant.speak(random.choice(greet_keywords[0]))
            video_folder = "D:/Videos/Music Videos"

            if not video_folder:
                # Link to different video services. Get the preferred service from the user database if available.
                pass
            else:
                # Get the folder path from the sql database and convert it to numpy array before using it.
                files = os.listdir(video_folder)
                os.startfile(f"{video_folder}/{random.choice(files)}")
        elif "music" in query or "song" in query:
            # Get the greet keywords from the sql database and convert it to numpy array before using it.
            # print("Playing")
            assistant.speak(random.choice(greet_keywords[0]))

            music_folder = "D:/Music/All time Music"

            if not music_folder:
                print("not")
                # Link to different music services. Get the preferred service from the user database if available.
                pass
            else:
                # Get the folder path from the sql database and convert it to numpy array before using it.
                files = os.listdir(music_folder)
                os.startfile(f"{music_folder}/{random.choice(files)}")
        elif "game" in query:
            # import game module and use the different classes for different games.
            # games.Games.choice()
            pass
        else:
            # Play video online
            if Web.checkConnection():
                import webbrowser
                webbrowser.open_new_tab(Search().youtubeVideoSearch(query))
            else:
                assistant.speak("No internet connection!")
                # print("No internet connection!")


class Question:
    def __init__(self):
        self.quesType = ""

    def checkQuestion(self, query=""):
        """
        Checks whether the provided query is a question or not.
        """
        __temp = False
        keywords = tuple(Sqlite3(databPath=r"data\database\attributes.db").execute(
            "SELECT * FROM KEYWORDS;")[0][1].replace("(", "", 1).replace(")", "", 1).split(", "))
        for word in keywords:
            word = word.lower()
            if Tools().reOperation(query, word, "at start"):
                __temp = True
                self.quesType = word
                break

        if __temp:
            del __temp
            return True
        else:
            del __temp
            return False

