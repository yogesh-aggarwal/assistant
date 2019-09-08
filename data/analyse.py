from sql_tools import sqlite


sqlite.connect("data/database/services.db")

result = sqlite.getTableNames()
result = sqlite.execute("SELECT * FROM engines")
result = sqlite.getColumnNames("engines")

print(result)
