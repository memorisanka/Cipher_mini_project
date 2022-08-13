import sqlite3


class Base:
    @staticmethod
    def create_base():
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS Users")
        cur.execute("CREATE TABLE Users (user_name TEXT, password TEXT")
        conn.close()

    @staticmethod
    def add_user(user, password):
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute("INSERT INTO Users (user_name, password) VALUES (?, ?)", (user, password))
        conn.commit()
        conn.close()

    @staticmethod
    def check_user(user, password):
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT user_name, password FROM Users WHERE user_name = {user}")
        if cur == (user, password):
            return True
        return False
