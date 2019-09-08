from sql_tools import sqlite

# sqlite.connect(r"data/database/services.db")
sqlite.connect(r"data/database/attributes.db")

# result = sqlite.getTableNames()
# result = sqlite.execute("SELECT * FROM engines")
# result = sqlite.getColumnNames("engines")

result = st(sqlite.execute("SELECT * FROM KEYWORDS")[0][0][1])

print(result)
