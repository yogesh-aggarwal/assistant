"""
Search API for Jarvis API project.
"""

import requests
import bs4


class Decide:
    pass


class Web(Decide):
    def __init__(self):
        super().__init__()

    def google(self, query):
        query = '+'.join(query.split(' '))
        url = f'https://www.google.com/search?q={query}&ie=utf-8&oe=utf-8'
        response = requests.get(url)
        soup = bs4.BeautifulSoup(response.text, 'html.parser')

        googleAnswers = soup.findAll("div", {"class": "BNeawe iBp4i AP7Wnd"})
        for answer in googleAnswers:
            if answer.text:
                return self.parse(answer.text)

        firstAnswers = soup.findAll("div", {"class": "BNeawe s3v9rd AP7Wnd"})
        for answer in firstAnswers:
            if answer.text:
                return self.parse(answer.text)

        allDiv = soup.findAll("div")
        googleAnswerKeys = ['BNeawe', 's3v9rd', 'AP7Wnd', 'iBp4i']

        for div in allDiv:
            for key in googleAnswerKeys:
                if key in div:
                    return self.parse(div.text)

    def parse(self, result):
        result = result.split('\n')[0]
        if result.endswith('Wikipedia'):
            result = result[:result.find('Wikipedia')]

        return result
    

class Device(Decide):
    def __init__(self):
        super().__init__()
