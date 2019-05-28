import numpy as np
from sql_operation import Sqlite3 as sql

# # sql.createDatabase("jj.db")
# a = sql().execute("SELECT * FROM ENGINES;", databPath=r"F:\Python\AI\assistant\data\database\services.db")
# print(np.array(a))


# sql().execute("CREATE TABLE PROGRAMS(CAPTION TEXT, DESCRIPTION TEXT, IDENTIFYING NUMBER TEXT, INSTALL_DATE TEXT, INSTALL_DATE_2 TEXT, INSTALL_LOCATION TEXT, INSTALL_STATE TEXT, NAME TEXT, PACKAGE CACHE TEXT, SKU NUMBER TEXT, VENDOR TEXT, VERSION TEXT);")
# import re
# import linkGrabber

# links = linkGrabber.Links("https://www.youtube.com/results?search_query=slowly+slowly")
# gb = links.find(limit=pretty=True, duplicates=False)
import re

# query = "search google for python"
query = "google for python"

patt = re.compile(r"^search")

matches = patt.finditer(query)

replace = False

for match in matches:
    if match.span():
        replace = True

if replace:
    query = query.replace("search", "", 1)
print(query)

wordList = re.sub(r"[^\w]", " ",  query).split()

engine = ["google", "bing"]

for engine in engine:
    if wordList[0] == engine:
        print(engine)
        break
