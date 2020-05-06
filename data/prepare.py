#####################################################################################
from pymongo import MongoClient

MongoURI = "mongodb://localhost:27017"
DB_NAME = "jycore"


client = MongoClient(MongoURI)[DB_NAME]

install_programs = client["install_programs"]
search_engines = client["search_engines"]
video_services = client["video_services"]
music_services = client["music_services"]
#####################################################################################

# from tools import mongo_client
from bson import json_util


def getBsonData(file):
    with open(file) as f:
        return json_util.loads(f.read())


install_programs.insert_many(getBsonData("files/win32_install_programs.json"))
install_programs.insert_many(getBsonData("files/linux_install_programs.json"))
search_engines.insert_many(getBsonData("files/search_engines.json"))
video_services.insert_many(getBsonData("files/video_services.json"))
music_services.insert_many(getBsonData("files/video_services.json"))
