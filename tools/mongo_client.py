from pymongo import MongoClient
from .constants import MongoURI, dbName

client = MongoClient(MongoURI)[dbName]

win32_install_programs = client["win32_install_programs"]
linux_install_programs = client["linux_install_programs"]
search_engines = client["search_engines"]
video_services = client["video_services"]
music_services = client["music_services"]
