import sqlite3


class DataBase:
    @staticmethod
    def create_base():
        """Create a database with three columns: ID, username, password."""

        with sqlite3.connect("users.sqlite") as conn:
            cur = conn.cursor()
            cur.execute(
                "CREATE TABLE IF NOT EXISTS Users ("
                "user_ID INTEGER PRIMARY KEY AUTOINCREMENT, "
                "user_name TEXT, "
                "password TEXT)"
            )
        # conn.close()

    @staticmethod
    def check_user(user_name: str, password: str) -> bool:
        """Check if there is a user and password in the database."""

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
        """Add new user to the database."""

        with sqlite3.connect("users.sqlite") as conn:
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO Users (user_ID, user_name, password) VALUES (NULL, ?, ?)",
                (user, password),
            )
            conn.commit()

    @staticmethod
    def check_username(user_name: str) -> str:
        """Check if there is a user with given username in the database."""
        with sqlite3.connect("users.sqlite") as conn:
            cur = conn.cursor()
            cur.execute(f"SELECT user_name FROM Users WHERE user_name = ?", (user_name,))
            val = cur.fetchone()

        if val:
            return val[0]
