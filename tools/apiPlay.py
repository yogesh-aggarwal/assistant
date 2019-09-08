import json
import webbrowser

import bs4
import requests
from sql_tools import Sqlite3

import tools.toolLib


class apiMusic:
    def gaana(name, album="", openLink=True):
        datab = Sqlite3(databPath=r"data\database\services.db")
        searchMethod = datab.execute("SELECT searchMethod FROM MUSIC_SERVICES")[0][0][0]
        # print(searchMethod)
        url = f"https://gaana.com{searchMethod}{name}"
        data = requests.get(url)
        soup = str(bs4.BeautifulSoup(data.text, 'html.parser'))
        start = soup.index('"https://gaana.com/song')
        stop = soup.index('"', start+1)
        link = soup[start:stop].replace('"', "")

        del url, data, soup, start, stop
        if openLink:
            webbrowser.open_new_tab(link)
            del link
        else:
            return link


class apiVideo:
    pass
