from typing import Union, Callable
from input_output_handler import InputOutputHandler as io
from rot import Rot13, Rot47, Rot, Rot3, RotAny
from buffer import Buffer
from file_handler import FileHandler as fh
from sql_base import DataBase
from log import UserLog


class Manager:
    def __init__(self) -> None:
        self.__is_running = True
        self.__options: dict[str, Callable] = {
            "1": self.__encrypt_text,
            "2": self.__decrypt_text,
            "3": Buffer.peak,
            "4": self.__write_to_file,
            "5": fh.read_json,
            "6": self.__end_application,
        }
        self.folder = False
        self.base = DataBase()
        self.log_user = UserLog()

    def run(self):
        """Starting the program."""

        self.log_user.log_manager()
        while self.__is_running:
            self.__show_menu()
            user_instruction = io.read("")
            self.__handle_instruction(user_instruction)
            io.print_text("\n")

    def __handle_instruction(self, user_text: Union[int, str]):
        """The method manages the execution of appropriate actions in the menu, and if the user gives an incorrect
        instruction - returns an error."""

        if user_text in self.__options:
            self.__options.get(user_text)()
        else:
            io.print_text(f"{user_text} is not an instruction")

    def __end_application(self) -> None:
        self.__is_running = False

    @staticmethod
    def __show_menu() -> None:
        """Main menu of Manager."""

        io.print_text(
            "What do you want to do?",
            "Pick the number:",
            "1. Encrypt text (ROT47/ROT13/ROT3/ROT1-25)",
            "2. Decrypt (ROT47/ROT13/ROT3)",
            "3. Peak buffer",
            "4. Write to JSON file",
            "5. Read from JSON file",
            "6. Log out",
            "---> ",
        )

    def __encrypt_text(self) -> None:
        """The method encrypt text with the rot provided by the user."""

        rot: Rot = self.__get_encryptor()
        text: str = io.read("Please write down text to encrypt: ")
        encoded_text: str = rot.cipher(text)
        encrypted_text = {rot.rot_type(): encoded_text}
        Buffer.add(encrypted_text)

    def __decrypt_text(self) -> None:
        """The method decrypts words with the index provided by the user."""

        Buffer.create_dict()
        rot: Rot = self.__get_encryptor()
        index_of_word: int = int(io.read(
            f"Choose word index do decrypt [1 - {len(Buffer.buffer_dict[rot.rot_type()])}]: ")
        )

        if len(Buffer.buffer_dict[rot.rot_type()]) > 0:
            if index_of_word <= (len(Buffer.buffer_dict[rot.rot_type()]) - 1):
                decrypted_text = rot.cipher(Buffer.buffer_dict[rot.rot_type()][index_of_word - 1])
                io.print_text("Decrypted word: ", f"{decrypted_text}")
            else:
                io.print_text("Index is out of range.")
        else:
            io.print_text("There are no words to decrypt.")

    def __get_encryptor(self) -> Rot:
        """User chooses rot."""

        io.print_text(
            "Which cipher do you want to use?",
            "Pick the number",
            "1: ROT47",
            "2: ROT13",
            "3: ROT3",
            "4: Any shift"
        )
        encryptor_no = io.read("")
        if encryptor_no == "1":
            return Rot47()
        elif encryptor_no == "2":
            return Rot13()
        elif encryptor_no == "3":
            return Rot3()
        elif encryptor_no == "4":
            return RotAny()
        else:
            io.print_text("Invalid option")
            return self.__get_encryptor()

    def __write_to_file(self) -> None:
        """Export data to json file. The filename is chosen by user."""

        if not self.folder:
            fh.check()
            self.folder = True
        Buffer.create_dict()
        file_name = input("File_name: ")

        fh.write_json(file_name, Buffer.buffer_dict)
        io.print_text("Saved to file.")
