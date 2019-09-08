from sql_tools import sqlite

# sqlite.connect(r"data/database/services.db")
sqlite.connect(r"data/database/history.db")

# result = sqlite.getTableNames()
# result = sqlite.execute("SELECT * FROM engines")
# result = sqlite.getColumnNames("engines")
result = sqlite.execute("SELECT * FROM history")

print(result)
