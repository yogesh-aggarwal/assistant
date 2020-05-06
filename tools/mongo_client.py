from pymongo import MongoClient

# from .constants import MongoURI
MongoURI = "mongodb://localhost:27017"
DB_NAME = "jycore"


client = MongoClient(MongoURI)[DB_NAME]

install_programs = client["install_programs"]


print(install_programs)
