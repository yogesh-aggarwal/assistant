"""
Behaviour extention for user behaviour detection for Jarvis AI Project.
"""

# import threading
from tools_lib import bprint

def init():
    bprint("-> Tracking started <-", bg="white", fg="red")


def terminate():
    bprint("-> Tracking stopped <-", bg="white", fg="red")
