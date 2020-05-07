"""
Extention for chatbot for Jycore AI Project
"""
from tools.toolLib import Tools


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
        # FIXME: Get question words from DB
        qWords = []

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
