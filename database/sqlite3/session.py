import sqlite3
from sqlite3 import (
    Connection,
    Cursor,
)

from database.sqlite3.sqlite_engine import SqliteEngine


class SqliteSession:

    def __init__(self, engine: SqliteEngine):
        self.engine = engine
        self.connection: Connection = self.engine.get_conn()
        self.cursor: None | Cursor = self.connection.cursor()
        self.change_factory_to_row()

    def change_factory_to_row(self):
        self.cursor.row_factory = sqlite3.Row

    def close(self):
        self.connection.close()

    def lastrowid(self):  # noqa
        return self.cursor.lastrowid

    def execute(self, *query):
        self.cursor.execute(*query)

    def fetchall(self):
        return self.cursor.fetchall()  # Results

    def fetchone(self):
        return self.cursor.fetchone()

    def begin(self):
        self.execute('BEGIN')
        return self

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    def __enter__(self):
        self.begin()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f"An error occurred: {exc_type}, {exc_val}")
            self.rollback()
        self.cursor.close()
