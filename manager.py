from typing import Union, Callable
from input_output_handler import InputOutputHandler as io
from rot import Rot13, Rot47, Rot
from buffer import Buffer
from file_handler import FileHandler as fh


class Manager:
    def __init__(self) -> None:
        self.__is_running = True
        self.__buffer = Buffer()
        self.__buffer_dict = Buffer()
        self.__options: dict[str, Callable] = {
            "1": self.__encrypt_text,
            "3": self.__buffer.peak,
            "4": self.__write_to_file,
            "5": self.__end_application,
        }

    def run(self):
        while self.__is_running:
            self.__show_menu()
            user_instruction = io.read("")
            self.__handle_instruction(user_instruction)
            io.print_text("\n")

    def __handle_instruction(self, user_text: Union[int, str]):
        if user_text in self.__options:
            self.__options.get(user_text)()
        else:
            io.print_text(f"{user_text} is not a instruction")

    def __end_application(self):
        self.__is_running = False

    @staticmethod
    def __show_menu() -> None:
        io.print_text(
            "What do you want to do?",
            "Pick the number:",
            "1. Encrypt text (ROT47/ROT13)",
            "3. Peak buffer",
            "4. Write to JSON file",
            "5. Exit",
            "---> ",
        )

    def __encrypt_text(self) -> None:
        rot: Rot = self.__get_encryptor()
        text: str = io.read("Pls write down text to encrypt: ")
        encoded_text: str = rot.cipher(text)
        encrypted_text = {rot.rot_type(): [text, encoded_text]}
        # TODO Klasa pomocnicza do dicta,Property class method na create. rot: str, text:str
        self.__buffer.add(encrypted_text)

    def __get_encryptor(self) -> Rot:
        io.print_text(
            "Which encryptor do you want to use?",
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
        buffer = self.__buffer_dict.create_dict()
        file_name = "Encrypted text.json"
        fh.check(file_name, buffer)
