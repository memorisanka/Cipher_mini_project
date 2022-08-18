from rot import Rot47
from sql_base import DataBase
from input_output_handler import InputOutputHandler as io


class UserLog:
    def __init__(self):
        self.counter = 0

    def log_manager(self) -> None:
        """Panel logowania do programu. W zależności od wybranej opcji zwraca odpowiednią funkcję."""

        io.print_text(
            "Welcome to Cipher!",
            "--------------------",
            "Choose an option:",
            "1: Log in",
            "2: New user",
            "3: Exit",
        )
        encryptor_no: str = io.read("")
        if encryptor_no == "1":
            return self.log()
        elif encryptor_no == "2":
            return self.new_user()
        elif encryptor_no == "3":
            exit()
        else:
            io.print_text("Invalid option")
            return self.log_manager()

    def log(self) -> None:
        """Logowanie istniejącego w bazie użytkownika.
        Funkcja pobiera od użytkownika login oraz hasło, szyfruje hasło i sprawdza, czy dane zgadzają się
        z danymi w bazie danych. Gdy podane zostaną błędne dane użytkownik ma 3 próby na podanie właściwych, inaczej
        program kończy działanie."""

        io.print_text("Please, log in", "---------------------")
        user_name: str = io.read("User name: ")
        password: str = io.read("Password: ")
        hash_password: str = Rot47.cipher(password)
        if DataBase.check_user(user_name, hash_password):
            io.print_text("Logged in!", "\n")
        elif not DataBase.check_user(user_name, password):
            while self.counter < 3:
                io.print_text("Invalid username or password", "Try again", f"Trials left: {3 - self.counter}")
                self.counter += 1
                self.log()
            else:
                io.print_text("All trials were used. You have to run program again.")
                exit()

    def new_user(self) -> None:
        """Funkcja dodaje nowego użytkownika do bazdy danych."""
        # TODO sprawdzanie, czy użytkownik istnieje w bazie danych

        io.print_text("Create new user", "-------------------")
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
            self.new_user()
        # else:
        #     io.print_text("Choose other user name.")
        #     self.new_user()
