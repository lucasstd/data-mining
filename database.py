#!/usr/bin/python

import sqlite3

__PATH__ = ""


def connect_to_db():
    try:
        # connection = sqlite3.connect('{}/{}'.format(__PATH__, "music.db"))
        connection = sqlite3.connect("music.db")
        print("[*] Database connected")
        return True, connection.cursor
    except sqlite3.OperationalError:
        print("[!] Error at Database connection")
        return False

def manage_db():
    db = connect_to_db()

    if db:
        # create tables
        db[-1].execute('''CREATE TABLE IF NOT EXISTS MUSIC(
            id                 INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            band_name          VARCHAR(25) NOT NULL,
            music_name         VARCHAR(25) NULL,
            chords             TEXT NOT NULL,
            difficulty         INT(1) NOT NULL,
            tab                TEXT NOT NULL
        );''')
    
print(manage_db())