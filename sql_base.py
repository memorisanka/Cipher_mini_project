import sqlite3


class DataBase:
    @staticmethod
    def create_base():
        """Utworzenie bazy danych z trzema kolumnami: ID, username, password."""

        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(
            "CREATE TABLE IF NOT EXISTS Users ("
            "user_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
            "user_name TEXT, "
            "password TEXT)"
        )
        conn.close()

    @staticmethod
    def check_user(user_name: str, password: str) -> bool:
        """Funkcja sprawdza, czy w bazie danych są dane użytkownika: login oraz hasło."""

        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(
            f"SELECT user_name, password FROM Users WHERE user_name = ?", (user_name,)
        )
        val = cur.fetchone()
        tup = (user_name, password)
        if val == tup:
            return True
        return False

    @staticmethod
    def add_user(user: str, password: str) -> None:
        """Funkcja dodaje nowego użytkownika do bazy danych."""

        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO Users (user_ID, user_name, password) VALUES (NULL, ?, ?)",
            (user, password),
        )
        conn.commit()
        conn.close()

    @staticmethod
    def check_username(user_name: str) -> bool:
        """Funkcja sprawdza, czy w bazie jest podany przez użytkownika login."""

        conn = sqlite3.connect("users.sqlite")
        cur = conn.cursor()
        cur.execute(f"SELECT user_name FROM Users WHERE user_name = ?", (user_name,))
        val = cur.fetchone()[0]
        print(val)
        if val == user_name or val is not None:
            cur.close()
            return True
        return False
