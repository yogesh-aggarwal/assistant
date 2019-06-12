import datetime
import os
import random
import re
import shutil
import subprocess
import sys
import traceback
import webbrowser

import numpy as np
import pandas as pd
import requests
import sklearn
import wikipedia

import assistant
import share
import tools.toolLib
from tools.sql_operation import Sqlite3 as sql

# from . import faceRecognition as fr


"""
Chatbot AI Project.
* Integrated with Assistant
* Inbuilt feature of Jarvis AI Poject.
Some features are-
    1) Interact with humans.
    2) Can give some interesting stuff to the user.
    3) ______
"""


class Greet:
    def __init__(self):
        pass


class Talk:
    def __init__(self):
        pass


class Play:
    def __init__(self):
        pass


class AnalyseQuestion:
    def __init__(self, type, query=""):
        if type == "what":
            self.whatType(query.replace("what", "").strip())

    def whatType(self, query):
        pass


class AImethods:
    def __init__(self):
        pass

    def graph(self, **kwargs):
        pass

    def bestResult(self, *awargs):
        pass

    def predict(self, obj):
        pass


class AITools:
    def __init__(self):
        pass
