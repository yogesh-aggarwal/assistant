"""
An integrative library that contains the tools required to work the assistant.
    * Integrated with Assistant
    * Inbuilt feature of Jycore AI Poject.
"""

# TODO: Improve parsing algorithm

import re
import webbrowser

from . import web as web_tools
from .mongo_client import search_engines

Web = web_tools.Web()


class Search:
    """
    Class that contains the search operation methods to perform various kinds of searching work efficiently.
    """

    def __init__(self):
        pass

    def classify(self, query="") -> None:
        """
        Classfies the type of search query provided.
        """
        engines = Dict.getOnlyValuesOfKey_lod(
            search_engines.find({}), "name", lambda x: x.lower()
        )
        wordList = query.replace("search", "", 1).strip().split(" ")
        engine = None

        # / Checking if the searching engine is not at start but at the last.
        if (
            (wordList[-1] in engines)
            and (len(wordList) > 1)
            and (wordList[-2] in ["on", "at"])
        ):  # Check if it contains the keywords that signifies that the word is the engine.
            engine = wordList[-1]
            wordList.pop(-1)
            wordList.pop(-1)

        # / Check if the search engine is at the start of the query.
        elif wordList[0] in engines:
            engine = wordList[0]

        try:
            wordList.remove(engine)
        except:
            pass

        searchQuery = " ".join(wordList)

        if engine == None:
            engine = "google"

        print(wordList, engine)
        self.searchEngine(query=searchQuery, engine=engine)

    def searchEngine(self, query="", engine="google") -> None:
        """
        Opens the webpage by searching the provideed query on the specified search engine.
        If no engine is provided it will search the query on Google.
        """
        query = query.replace(engine, "", 1)
        engine = search_engines.find_one({"name": engine.capitalize()})
        if not engine:
            engine = search_engines.find_one({"name": "Google"})
        METHOD = engine["querySlug"]
        HOST = engine["host"]
        PROTOCOL = "https" if engine["isHttps"] else "http"
        webbrowser.open_new_tab(f"{PROTOCOL}://{HOST}{METHOD}{query}")


class String:
    @staticmethod
    def spaceToCamelcase(string) -> str:
        wordList = "".join([x.title() for x in string.split(" ")])
        return f"{wordList[0].lower()}{wordList[1:]}"


class Dict:
    @staticmethod
    def getOnlyValuesOfKey_lod(list, key, _callback) -> list:
        """
        Returns the list of values of the specified key from the list of dicts
        For eg: `[{"name": "foo"}, {"name": "bar", "age": 20}]`
             -> `["foo", "bar"]`
        """
        values = []
        for x in list:
            if _callback:
                x = _callback(x[key])
                values.append(x)
            else:
                values.append(x[key])
        return values


class Tools:
    """
    Class that contains some basic (misc.) tools.
    """

    def __init__(self):
        pass

    def reOperation(self, query, strings, method) -> bool:
        """
        Performs some simple regular expressions operations on the specified query.
        """
        if type(strings) is str:
            strings = [strings]

        isMatchFound = False
        for string in strings:
            if method == "at start":
                patt = re.compile(rf"^{string}")
            elif method == "at end":
                patt = re.compile(rf"{string}$")

            matches = patt.finditer(query)
            if len(tuple(matches)) > 0:
                isMatchFound = True
                break

        return isMatchFound

    @property
    def getUserPath(self) -> str:
        from pathlib import Path

        return str(Path.home())

    @staticmethod
    def strTolst(query) -> list:
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
