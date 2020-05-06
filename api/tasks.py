"""
Tasks API for helping user to compelete and keep track of the
tasks as an entension of Jycore AI project.
"""

import io
from abc import ABCMeta
import calendar
import time


class TaskIO:
    def __init__(self):
        pass

    def getTasks():
        pass

    def getTaskById():
        pass

    def getTaskByDay():
        pass

    def getTaskByMonth():
        pass

    def getTaskByYear():
        pass


class TaskCrud:
    """
    Base class for task crud operations
    """

    def __init__(self, lst):
        self.lst = lst


class TaskCreate(TaskCrud):
    def __init__(self, lst):
        super().__init__(lst)


class TaskRead(TaskCrud):
    def __init__(self, lst):
        super().__init__(lst)


class TaskUpdate(TaskCrud):
    def __init__(self, lst):
        super().__init__(lst)


class TaskDelete(TaskCrud):
    def __init__(self, lst):
        super().__init__(lst)
