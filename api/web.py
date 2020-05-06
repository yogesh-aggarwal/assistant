"""
Web API for Jycore API project.
"""

import requests


class Web:
    def __init__(self):
        pass


class GET(Web):
    def __init__(self):
        super().__init__()

    def request(self, url):
        res = requests.get(url)
        return res.text


class POST(Web):
    def __init__(self):
        super().__init__()

    def request(self, url, data=""):
        res = requests.post(url, data)
        return res.text
