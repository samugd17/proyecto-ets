from __future__ import annotations

import sqlite3
from random import randint

DB_PATH = 'tablestars.db'

def create_db(db_path: str = DB_PATH) -> None:
    con = sqlite3.connect(db_path)
    con.row_factory = sqlite3.Row
    cur = con.cursor()

    sql_user = '''CREATE TABLE user (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT
    )'''

    cur.execute(sql_user)
    con.commit()


class User:
    def __init__(self, username: str, password: str, user_id: int = 0):
        self.con = sqlite3.connect(DB_PATH)
        self.con.row_factory = sqlite3.Row
        self.cur = self.con.cursor()

        self.username = username
        self.password = password
        self.id = user_id
        self.logged = False

    def save(self) -> None:
        sql = "INSERT INTO User (username, password) VALUES (?, ?)"
        self.cur.execute(sql, (self.username, self.password))
        self.id = self.cur.lastrowid
        self.con.commit()

    def login(self, password: str) -> None:
        sql = "SELECT count(*) from User where username = ? and password = ?"
        result = self.cur.execute(sql, (self.username, password))
        row = result.fetchone()
        self.logged = True if row[0] else False

    def __repr__(self):
        return f'{self.id}: {self.username}'

    @classmethod
    def from_db_row(cls, row: sqlite3.Row):
        return cls(row['username'], row['password'], row['id'])   

class Token:
    def __init__(self, color, position:int = 0):
        self.color = color
        self.position = position

    def move(self, steps):
        self.position += steps

    def restart(self):
        self.position = 0

    def __str__(self):
        return f"{self.color} token is in position {self.position} "

class Dice:
    def __init__(self, sides: int = 6):
        self.sides = sides

    def throw(self):
        return randint(1, self.sides)
    
# Ejemplo de uso
dado = Dice()
token = Token("red")

# Tira el dado y mueve la ficha
dice_result = dado.throw()
token.move(dice_result)

print(f"Dice result: {dice_result}")
print(token)