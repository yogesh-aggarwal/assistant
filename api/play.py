import random
import webbrowser

import bs4
import requests

from sql_tools import sqlite
from tools import synthesis as syn
from tools.constants import dbServices
from exception import QueryError


class apiMusic:
    def gaana(self, query, openLink=True):
        host, searchMethod = sqlite.execute(
            databPath=dbServices,
            command=f"SELECT host, searchMethod FROM MUSIC_SERVICES WHERE RANK=1",
        )[0][0]

        res = requests.get(f"{host}{searchMethod}{query}").text
        try:
            with open("h.html", "w") as f:
                f.write(res)

            link = res[
                res.index('<h3 class="item-heading"><a href="')
                + len('<h3 class="item-heading"><a href="') : res.index(' class="rt_arw " ')
                - 1
            ]
        except Exception:
            try:
                res.index(" No results found for “")
                raise QueryError
            except Exception:
                raise QueryError

        if openLink:
            webbrowser.open_new_tab(link)

        return link

    def spotify(self, query, openLink=True):
        syn.speak(
            "Spotify is not available at the moment, please try after future updates"
        )

    def youtubeMusic(self, query, openLink=True, rand=False):
        link = apiVideo().youtube(query, openLink=False, rand=rand)
        link = link.replace("https://youtube.com", "https://music.youtube.com")
        if openLink:
            webbrowser.open_new_tab(link)
        return link


class apiVideo:
    def youtube(self, query, openLink=True, rand=False):
        host, searchMethod, playMethod = sqlite.execute(
            databPath=dbServices,
            command=f"SELECT host, searchMethod, playMethod FROM VIDEO_SERVICES WHERE name='YouTube'",
        )[0][0]

        link = f"{host}{searchMethod}{query}"

        res = requests.get(f"{host}{searchMethod}{query}").text
        soup = bs4.BeautifulSoup(res, "lxml")
        links = []
        for link in soup.find_all("a", href=True):
            links.append(link["href"])

        vids = []
        for link in links:
            if playMethod in link:
                vids.append(link)
                if not rand:
                    break

        try:
            if rand:
                link = f"{host}{random.choice(vids)}"
            else:
                link = f"{host}{vids[0]}"

            if openLink:
                webbrowser.open_new_tab(link)

            return link
        except Exception:
            pass
