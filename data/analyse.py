from sql_tools import sqlite

sqlite.connect(r"data/database/services.db")
# sqlite.connect(r"data/database/history.db")

# result = sqlite.getTableNames()
# result = sqlite.execute("SELECT * FROM engines")
result = sqlite.getColumnNames("MUSIC_SERVICES")
# result = sqlite.execute("SELECT * FROM MUSIC_SERVICES")
# result = sqlite.execute("UPDATE MUSIC_SERVICES SET scrapMethod='requests' WHERE rank=1")
# result = sqlite.getColumnNames("engines")
# result = sqlite.execute("SELECT * FROM history")

print(result)
