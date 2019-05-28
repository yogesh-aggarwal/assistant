from sql_operation import Sqlite3 as sql


# sql = sql(databPath=r"data\database\services.db")
sql = sql(databPath=r"data\database\attributes.db")

# sql.execute("DROP TABLE ENGINES;")

# sql.execute("CREATE TABLE ENGINES(NAME TEXT PRIMARY KEY, METHOD TEXT);")
# sql.execute("INSERT INTO ENGINES VALUES('Google', '/search?q=');")
# sql.execute("INSERT INTO ENGINES VALUES('Bing', '/search?q=');")

# print(sql.execute("SELECT * FROM ENGINES;"))


# sql.createDatabase(name="test data.db")
# print(sql.moveDatabase(newPath="data/", database="test data.db"))
# sql.delDatabase(databPath="test data.db")

# sql.execute("CREATE TABLE DOMAIN(NAME TEXT, USAGE TEXT, CATEGORY TEXT);")
# sql.execute("INSERT INTO DOMAIN VALUES('COMMERCIAL', '.com', 'TLD');")
# sql.execute("INSERT INTO DOMAIN VALUES('EDUCATION', '.edu', 'TLD');")
# sql.execute("INSERT INTO DOMAIN VALUES('NETWORK', '.net', 'TLD');")

sql.execute("CREATE TABLE KEYWORDS(TYPE TEXT PRIMARY KEY, KEYWORDS TEXT)")
sql.execute("INSERT INTO KEYWORDS VALUES('QUESTION', '(WHAT, WHO, WHERE, HOW, WHOSE, WHOM, WHICH, WHY)');")
# sql.execute("")
# sql.execute("")
# sql.execute("")

print(sql.execute("SELECT * FROM KEYWORDS;")[0][1])
