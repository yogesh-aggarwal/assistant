import webbrowser

import bs4
import requests
from sql_tools import sqlite



class apiMusic:
    def gaana(name, album="", openLink=True):
        searchMethod = sqlite.execute("SELECT searchMethod FROM MUSIC_SERVICES", databPath=r"data/database/services.db")[0][0][0]
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
