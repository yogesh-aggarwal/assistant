"""
An integrative library that contains the tools required to work the assistant.
    * Integrated with Assistant
    * Inbuilt feature of Jycore AI Poject.
"""

# TODO: Improve parsing algorithm

import re
import webbrowser

from sql_tools import sqlite
from . import synthesis as syn

from . import web as web_tools
from .constants import dbServices

Web = web_tools.Web()


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
        engines = (
            sqlite.execute("SELECT name FROM ENGINES", db=dbServices,).get[0][0].T[0]
        )

        print(engines)
        # exit()

        isSearchInQuery = True if "search" in query else False
        wordList = query.lower().replace("search", "", 1).strip().split(" ")
        engine = None

        for i in range(len(wordList)):
            try:
                if wordList[0] in ["for", "at", "on"]:
                    wordList.pop(0)
            except Exception:
                pass
        print(wordList)

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
                wordList[-1].capitalize() == __engine or isSearchInQuery
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

        if queryType == "search":
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
        print(f"https://{engine}.com{method}{query}")
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
                db=dbServices,
                command=f"SELECT METHOD FROM ENGINES WHERE NAME='{engine.capitalize()}'",
            ).get[0][0][0][0]
        except Exception:
            return sqlite.execute(
                db=dbServices,
                command=f"SELECT METHOD FROM ENGINES WHERE NAME='Google'",
            ).get[0][0][0][0]

    def reOperation(self, query, string, method):
        """
        Performs some simple regular expressions operations on the specified query.
        """
        if type(string) is str:
            __temp = []
            __temp.append(string)
            string = __temp.copy()
            del __temp
        else:
            raise ValueError(
                f"[toolsLib.Tools.reOperation]: Query must be string, got {type(query)}"
            )

        __temp = False
        for letter in string:
            if method == "at start":
                patt = re.compile(rf"^{letter}")
            elif method == "at end":
                patt = re.compile(rf"{letter}$")

            matches = patt.finditer(query)
            for match in matches:
                if match != None:
                    __temp = True
                else:
                    __temp = False

        return __temp

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
