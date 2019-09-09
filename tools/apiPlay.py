import random
import webbrowser

import bs4
import requests

from sql_tools import sqlite
from . import synthesis as syn
from .constants import dbServices

# from .toolLib import Search, Web


class apiMusic:
    def gaana(query, openLink=True):
        host, searchMethod = sqlite.execute(
            databPath=dbServices,
            command=f"SELECT host, searchMethod FROM MUSIC_SERVICES WHERE RANK=1",
        )[0][0]

        res = requests.get(f"{host}{searchMethod}{query}").text
        if openLink:
            webbrowser.open_new_tab(
                res[
                    res.index('<h3 class="item-heading"><a href="')
                    + len('<h3 class="item-heading"><a href="') : res.index(
                        ' class="rt_arw " '
                    )
                    - 1
                ]
            )


class apiVideo:
    def youtube(self, query, rand=False):
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

            webbrowser.open_new_tab(link)
        except Exception:
            pass
