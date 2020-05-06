from sql_tools import sqlite

# sqlite.connect(r"data/database/services.db")
# sqlite.connect(r"data/database/history.db")
sqlite.connect(r"data/database/programInstallData.db")

# result = sqlite.getTableNames()
# result = sqlite.execute("SELECT * FROM engines").get
# result = sqlite.getColumnNames("MUSIC_SERVICES")
# result = sqlite.execute("SELECT * FROM MUSIC_SERVICES").get
# result = sqlite.execute("UPDATE MUSIC_SERVICES SET scrapMethod='requests' WHERE rank=1").get
# result = sqlite.execute("SELECT * FROM MUSIC_SERVICES").get
# result = sqlite.execute("INSERT INTO MUSIC_SERVICES VALUES ('YouTube music', 'https://music.youtube.com', '/search?q=', '/watch?v=', '3', 'bs4', 'RUN')").get
# result = sqlite.getColumnNames("engines")
# result = sqlite.execute("SELECT * FROM PROGRAMS_DATA_WIN32").get
result = sqlite.execute("SELECT * FROM history").get
# result = sqlite.execute("SELECT * FROM history WHERE solved='false'").get
# result = sqlite.getNoOfRecords(["history", "history"])

print(result)
