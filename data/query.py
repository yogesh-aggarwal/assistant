from sql_tools import sqlite
from tools_lib import bprint

databases = [
    "services.db",
    "attributes.db",
    "programInstallData.db",
    "history.db"
]

query = [
    "services.sql",
    "attributes.sql",
    "programInstallData.sql",
    "history.sql"
]


for i in range(len(databases)):
    sqlite.connect(fr"data/database/{databases[i]}")

    with open(f"data/query/{query[i]}") as f:
        read = f.readlines()
        for command in read:
            sqlite.execute(command)
    bprint(f"Done for {databases[i]}", bg="red")

    sqlite.disconnect(fr"data/database/{databases[i]}")

print()

bprint("---> Databases updated successfully ✅ <---", bg="red")
