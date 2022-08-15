import sqlite3


class Base:
    @staticmethod
    def create_base():
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS Users (" 
                    "user_ID INTEGER PRIMARY KEY AUTOINCREMENT, " 
                    "user_name TEXT, "
                    "password TEXT)")
        conn.close()

    @staticmethod
    def check_user(user_name, password):
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT user_name, password FROM Users WHERE user_name = ?", (user_name, ))
        val = cur.fetchone()
        tup = (user_name, password)
        if val == tup:
            return True
        return False

    @staticmethod
    def add_user(user, password):
        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute("INSERT INTO Users (user_ID, user_name, password) VALUES (NULL, ?, ?)", (user, password))
        conn.commit()
        conn.close()
