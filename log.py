from rot import Rot47
from sql_base import DataBase
from input_output_handler import InputOutputHandler as io


class UserLog:
    def __init__(self):
        self.counter = 0

    def existing_user(self) -> None:
        user_name: str = io.read("User name: ")
        password: str = io.read("Password: ")
        hash_password: str = Rot47.cipher(password)
        if DataBase.check_user(user_name, hash_password):
            io.print_text("Logged in!", "\n")

    def invalid_user_password(self, user, password):
        if not DataBase.check_user(user, password):
            self.counter += 1
            io.print_text("Invalid username or password", "Try again", f"Trials left: {3 - self.counter}")
        # else:
        #     io.print_text("All trials were used. You have to run program again.")
        #     exit()

    def new_user(self) -> None:
        user_name: str = io.read("User name: ")
        if not DataBase.check_username(user_name):
            password: str = io.read("Password: ")
            password_repeat: str = io.read("Repeat your password: ")
            if password == password_repeat:
                hash_password: str = Rot47.cipher(password)
                DataBase.add_user(user_name, hash_password)
                io.print_text("Created new user. Please log in.", "\n")
                # self.log()
            else:
                io.print_text("Incorrect password")
                self.new_user()
        else:
            io.print_text("Choose other user name.")
            self.new_user()
