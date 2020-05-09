import socket, webbrowser

from selenium import webdriver

from .mongo_client import search_engines


class Web:
    """
    Class that contains tools for the web operations.
    """

    def __init__(self, query=""):
        self.query = query
        self.__domain_presence = False

    @staticmethod
    def checkConnection(query="google.com"):
        """
        Checks whether there is internet connection available or not. Returns boolean value as per the outcome.
        """
        query = query.replace("https://", "").replace("http://", "")

        try:
            host = socket.gethostbyname(query)
            s = socket.create_connection((host, 80), 2)
            s.close()
            return True
        except Exception:
            return False

    def getWebsiteLinkByName(self, query):
        client = self.searchOnPreferedEngine(query, openLink=False)
        link = (
            client.find_element_by_xpath('//*[@id="search"]')
            .find_element_by_tag_name("a")
            .get_attribute("href")
        )
        return link

    def searchOnPreferedEngine(self, query, openLink=True) -> (bool, webdriver.Chrome):
        engine = search_engines.find_one({"name": "Google"})
        HOST = engine["host"]
        PROTOCOL = "https" if engine["isHttps"] else "http"
        SEARCH_SLUG = engine["querySlug"]
        link = f"{PROTOCOL}://{HOST}{SEARCH_SLUG}{query}"

        if openLink:
            webbrowser.open_new_tab(link)
            return True
        else:
            client = self.getWebClient()
            client.get(link)
            return client

    @staticmethod
    def getWebClient(headless=True):
        webClientOptions = webdriver.ChromeOptions()
        webClientOptions.add_argument("headless") if headless else False
        webClientOptions.add_argument("--log-level=3")
        webClientOptions.add_experimental_option("excludeSwitches", ["enable-logging"])

        return webdriver.Chrome(options=webClientOptions)
