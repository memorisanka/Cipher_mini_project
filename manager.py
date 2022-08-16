from typing import Union, Callable
from input_output_handler import InputOutputHandler as io
from rot import Rot13, Rot47, Rot
from buffer import Buffer
from file_handler import FileHandler as fh
from log import User
from sql_base import Base


class Manager:
    def __init__(self) -> None:
        self.__is_running = True
        self.__buffer = Buffer()
        self.__options: dict[str, Callable] = {
            "1": self.__encrypt_text,
            "2": self.__decrypt_text,
            "3": self.__buffer.peak,
            "4": self.__write_to_file,
            "5": self.__end_application,
        }
        self.folder = False
        self.log_user = User()
        self.base = Base()
        self.__log_options: dict[str, Callable] = {
            "1": self.log,
            "2": self.new_user,
            "3": self.__end_application(),
        }

    def log(self) -> None:
        io.print_text(
            "Please choose option:",
            "1. Log in",
            "2. New user registration",
            "3. Exit"
        )
        choice = io.read("")
        if choice == "1":
            user_name: str = io.read("User name: ")
            password: str = io.read("Password: ")
            hash_password: str = Rot47.cipher(password)
            if Base.check_user(user_name, hash_password):
                io.print_text("Logged in!", "\n")
                self.run()
            else:
                io.print_text("Invalid username or password", "Try again")  # nie zwraca komunikatu, jeśli False
                self.log()
            # if self.log_user.check(user, password):
            #     io.print_text("Logged in!", "\n")
            #     self.run()
            # else:
            #     io.print_text("Invalid username or password", "Try again")  # nie zwraca komunikatu, jeśli False
            #     self.log()
        elif choice == "2":
            user_name: str = io.read("User name: ")
            password: str = io.read("Password: ")
            password_repeat: str = io.read("Repeat your password: ")
            if password == password_repeat:
                hash_password: str = Rot47.cipher(password)
                Base.add_user(user_name, hash_password)
            #     self.log_user.add(user, password)
                self.log()
            else:
                io.print_text("Wrong password")
                self.__end_application()
        elif choice == "3":
            self.__end_application()

    def new_user(self):
        pass
    
    def run(self):
        while self.__is_running:
            self.__show_menu()
            user_instruction = io.read("")
            self.__handle_instruction(user_instruction)
            io.print_text("\n")

    def __handle_log_instruction(self, user_text: Union[int, str]):
        if user_text in self.__log_options:
            self.__log_options.get(user_text)()
        else:
            io.print_text(f"{user_text} is not an instruction")

    def __handle_instruction(self, user_text: Union[int, str]):
        if user_text in self.__options:
            self.__options.get(user_text)()
        else:
            io.print_text(f"{user_text} is not an instruction")

    def __end_application(self):
        self.__is_running = False

    @staticmethod
    def __show_menu() -> None:
        io.print_text(
            "What do you want to do?",
            "Pick the number:",
            "1. Encrypt text (ROT47/ROT13)",
            "2. Decrypt all (ROT47/ROT13)",
            "3. Peak buffer",
            "4. Write to JSON file",
            "5. Log out",
            "---> ",
        )

    def __encrypt_text(self) -> None:
        rot: Rot = self.__get_encryptor()
        text: str = io.read("Pls write down text to encrypt: ")
        encoded_text: str = rot.cipher(text)
        encrypted_text = {rot.rot_type(): [text, encoded_text]}
        self.__buffer.add(encrypted_text)

        match rot.rot_type():
            case "Rot 13":
                self.__buffer.add_buffer_rot13(encoded_text)
            case "Rot 47":
                self.__buffer.add_buffer_rot47(encoded_text)

    def __decrypt_text(self) -> Rot:
        rot: Rot = self.__get_encryptor()

        if rot.rot_type() == "Rot 13":
            for txt in self.__buffer.buffer_rot13:
                decrypted_text = rot.cipher(txt)
                self.__buffer.decrypted_rot13.append(decrypted_text)
            for i in self.__buffer.decrypted_rot13:
                print(i)
        elif rot.rot_type() == "Rot 47":
            for txt in self.__buffer.buffer_rot47:
                decrypted_text = rot.cipher(txt)
                self.__buffer.decrypted_rot47.append(decrypted_text)
            for i in self.__buffer.decrypted_rot47:
                print(i)
        else:
            io.print_text("Invalid option")
            return self.__get_encryptor()

    def __get_encryptor(self) -> Rot:
        io.print_text(
            "Which cipher do you want to use?",
            "Pick the number",
            "1: ROT47",
            "2: ROT13",
        )
        encryptor_no = io.read("")
        if encryptor_no == "1":
            return Rot47()
        elif encryptor_no == "2":
            return Rot13()
        else:
            io.print_text("Invalid option")
            return self.__get_encryptor()

    def __write_to_file(self) -> None:
        if not self.folder:
            fh.check()
            self.folder = True
        self.__buffer.create_dict()
        file_name = input("File_name: ")

        fh.write_json(file_name, self.__buffer.buffer_dict)
        io.print_text("Saved to file.")
