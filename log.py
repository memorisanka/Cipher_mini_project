from rot import Rot47
from sql_base import DataBase
from input_output_handler import InputOutputHandler as io


class UserLog:
    def __init__(self):
        self.users_buffer = {}
        self.counter = 0

    def add(self, usr: str, pw: str) -> None:
        self.users_buffer.update({usr: pw})

    def remove(self, user: str) -> None:
        self.users_buffer.pop(user, "User not found")

    def check(self, usr: str, pw: str) -> bool:
        if self.users_buffer[usr] == pw:
            return True
        return False

    def log(self) -> bool:
        while self.counter < 3:
            user_name: str = io.read("User name: ")
            password: str = io.read("Password: ")
            hash_password: str = Rot47.cipher(password)
            if DataBase.check_user(user_name, hash_password):
                io.print_text("Logged in!", "\n")
                return True
            else:
                self.counter += 1
                io.print_text("Invalid username or password", "Try again", f"Trials left: {3 - self.counter}")
                self.log()
        else:
            io.print_text("All trials were used. You have to run program again.")
            exit()

    def new_user(self) -> None:
        user_name: str = io.read("User name: ")
        password: str = io.read("Password: ")
        password_repeat: str = io.read("Repeat your password: ")
        if password == password_repeat:
            hash_password: str = Rot47.cipher(password)
            DataBase.add_user(user_name, hash_password)
            io.print_text("Created new user. Please log in.", "\n")
            self.log()
        else:
            io.print_text("Incorrect password")