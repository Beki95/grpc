import sqlite3
from sqlite3 import (
    Connection,
)


class SqliteEngine:

    def __init__(self, path: str, check_same_thread: bool = False):
        self.connection: Connection = None
        self.path = path
        self.check_same_thread = check_same_thread

    def get_conn(self):
        self.connection = sqlite3.connect(self.path, check_same_thread=self.check_same_thread)
        return self.connection
