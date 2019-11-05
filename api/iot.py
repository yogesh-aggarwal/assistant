"""
API for interaction & control between IoT devices through Jarvis
"""


class Connection:
    def __init__(self, conn):
        pass

    def wireless(self):
        pass

    def bluetooth(self):
        pass


class Chromecast(Connection):
    def __init__(self, conn):
        super().__init__(conn)


class Bluetooth(Connection):
    def __init__(self, conn):
        super().__init__(conn)
