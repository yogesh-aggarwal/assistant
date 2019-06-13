"""
An integrative library which contains games that are operated by the user through the assistant.
    * Integrated with Assistant
    * Inbuilt feature of Jarvis AI Poject.
"""

def path():
    import sys
    import os
    sys.path.insert(0, os.getcwd())
path()

import os
import sys

import numpy as np
import pandas as pd
from tools.sql_operation import Sqlite3 as sql

# import pygame

class Games:
    def __init__(self):
        self.start_threshold = True
    
    @classmethod
    def choice(cls):
        # Choosing the right game for the user on the basis of the previous data.
        # Fetch the data from the sql database and convert it to the numpy array.
        pass
    
    @staticmethod
    def store_score(score):
        pass

    def start(self, name):
        # Start the game provided
        pass

