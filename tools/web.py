import socket

from selenium import webdriver

from .constants import webDomains


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

    @staticmethod
    def getWebClient():
        webClientOptions = webdriver.ChromeOptions()
        webClientOptions.add_argument("headless")
        webClientOptions.add_argument("--log-level=3")
        webClientOptions.add_experimental_option("excludeSwitches", ["enable-logging"])

        return webdriver.Chrome(options=webClientOptions)

    def checkWebExists(self, query=""):
        """
        Checks the existance of the address provided.

        If there is connection return problem return "err_no_connection", else return True or False.

        Exists = True,
        Not exists = False
        """
        domainPresence = False
        result = False
        for dom in webDomains:
            if dom in query:
                domainPresence = True
                del dom
                break

        for domain in webDomains:
            domain = domain if not domainPresence else ""
            result = True if self.checkConnection(f"{query}{domain}") else False

        return result

    def findDomain(self, query=""):
        """
        Finds the web domain of the name provided.

        If there is connection return problem return "err_no_connection", else return True or False.
        """
        for domain in webDomains:
            result = domain if self.checkWebExists(query=f"{query}{domain}") else False
            if not result:
                continue
            else:
                return result
        else:
            return False
