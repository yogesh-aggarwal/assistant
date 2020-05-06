"""
Extention for chatbot for Jycore AI Project
"""
from tools.toolLib import Tools
from sql_tools import sqlite
from tools.constants import dbAttributes


class AnalyseQuestion:
    def __init__(self, type, query=""):
        if type == "what":
            self.whatType(query.replace("what", "").strip())

    def whatType(self, query):
        pass


class Question:
    def __init__(self):
        self.quesType = ""

    def checkQuestion(self, query=""):
        """
        Checks whether the provided query is a question or not.
        """
        __temp = False
        qWords = (
            sqlite.execute(db=dbAttributes, command="SELECT * FROM KEYWORDS;")
            .get[0][0][1]
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

        __temp = (
            False  # TODO Remove this line for searching questions related to assistant
        )
        return __temp

    def analyse(self, query=""):
        pass
        # chatBot.AnalyseQuestion(self.quesType, query=query)
