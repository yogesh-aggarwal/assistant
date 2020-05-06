"""
Play API for playing content for Jycore AI project
"""
import webbrowser

from exception import QueryError
from tools import mongo_client
from tools import synthesis as syn
from tools import web

# Web client
webClient = web.Web.getWebClient()
# Services
musicServices = mongo_client.music_services
videoServices = mongo_client.video_services


def scrapeService(service, query, openLink=True):
    query = query.replace(" ", "+")

    PROTOCOL = "https://" if service["isHttps"] else "http://"
    HOST = service["host"]
    SEARCH_SLUG = service["searchSlug"]
    XPATH = service["xpath"]

    webClient.get(f"{PROTOCOL}{HOST}{SEARCH_SLUG}{query}")

    link = False

    try:
        link = webClient.find_element_by_xpath(XPATH).get_attribute("href")
        webbrowser.open_new_tab(link) if openLink else False
    except:
        raise QueryError(
            "[api.play.apiMusic.gaana]: Connection error or Element not found (selenium)"
        )
    webClient.__exit__()

    return link


class apiMusic:
    def gaana(self, query, openLink=True):
        service = musicServices.find_one({"name": "Gaana"})
        scrapeService(service=service, query=query, openLink=True)

    def spotify(self, query, openLink=True):
        syn.speak(
            "Spotify is not available at the moment, please try after future updates"
        )

    def youtubeMusic(self, query, openLink=True, rand=False):
        service = musicServices.find_one({"name": "YouTube Music"})
        scrapeService(service=service, query=query, openLink=True)


class apiVideo:
    def youtube(self, query, openLink=True, rand=False):
        service = videoServices.find_one({"name": "YouTube"})
        scrapeService(service=service, query=query, openLink=True)
