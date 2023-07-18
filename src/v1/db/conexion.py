import sqlite3


def get_connection():
    try:
        return sqlite3.connect('src/v1/db/database.db')
    except Exception as ex:
        return ex