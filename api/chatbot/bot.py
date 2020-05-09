"""
Extention for chatbot for Jycore AI Project
"""
from tools.toolLib import Tools
import tools.synthesis as syn
from tools.web import Web
from tools import mongo_client

web = Web()
search_engines = mongo_client.search_engines


class AnalyseQuestion:
    def __init__(self, type, query=""):
        if type == "what":
            self.whatType(query.replace("what", "").strip())

    def whatType(self, query):
        pass


class Question:
    def __init__(self, query):
        self.query = query
        self.quesType = self.checkQuestion()

        if self.quesType:
            self.getAnswer()

        print(self.quesType)

    def checkQuestion(self):
        """
        Checks whether the provided query is a question or not.
        """
        # FIXME: Get question words from DB
        qWords = ["what", "when", "where", "which", "who", "why", "how"]

        for word in qWords:
            if Tools().reOperation(self.query, word, "at start"):
                return word
        return "what"

    def getAnswer(self, speak=True):
        engine = search_engines.find_one({"name": "Google"})
        METHOD = engine["querySlug"]
        HOST = engine["host"]
        PROTOCOL = "https" if engine["isHttps"] else "http"
        client = web.getWebClient(headless=1)
        client.get(f"{PROTOCOL}://{HOST}{METHOD}{self.query.replace(' ', '+')}")

        ele = None
        for xpath in self.getXPaths():
            try:
                ele = client.find_element_by_xpath(xpath)
                if speak:
                    syn.speak(ele.text)
                    break
            except:
                pass

    def getXPaths(self):
        if self.quesType == "who" or self.quesType == "what":
            return (
                '//*[@id="rhs"]/div/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div/div/span[1]',
                '//*[@id="rhs"]/div/div[1]/div[1]/div[1]/div/div[3]/div/div[1]/div/div/div/div/span[1]',
                '//*[@id="rhs"]/div/div[1]/div[1]/div[1]/div/div[4]/div/div[1]/div/div/div/div/span[1]',
            )
        elif self.quesType == "when":
            return (
                '//*[@id="rso"]/div[1]/div[1]/div[1]/div[1]/div/div[2]/div/div[1]/div/div/div[1]',
                '//*[@id="tsuid98"]/span/div/div/div[2]/div/div[1]/div/div/span[2]',
            )

    def analyse(self, query=""):
        pass
        # chatBot.AnalyseQuestion(self.quesType, query=query)
