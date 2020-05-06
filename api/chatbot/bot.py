"""
Extention for chatbot for Jycore AI Project
"""


class AnalyseQuestion:
    def __init__(self, type, query=""):
        if type == "what":
            self.whatType(query.replace("what", "").strip())

    def whatType(self, query):
        pass
