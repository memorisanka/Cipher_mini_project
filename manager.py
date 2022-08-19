from typing import Union, Callable
from input_output_handler import InputOutputHandler as io
from rot import Rot13, Rot47, Rot, Rot3
from buffer import Buffer
from file_handler import FileHandler as fh
from sql_base import DataBase
from log import UserLog


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
        self.base = DataBase()
        self.log_user = UserLog()

    def run(self):
        """Uruchomienie programu."""

        self.log_user.log_manager()
        while self.__is_running:
            self.__show_menu()
            user_instruction = io.read("")
            self.__handle_instruction(user_instruction)
            io.print_text("\n")

    def __handle_instruction(self, user_text: Union[int, str]):
        """Funkcja zarządza wykonaniem odpowiednich czynności w menu, a jeśli użytkownik poda błędną instrukcję
        - zwraca błąd."""

        if user_text in self.__options:
            self.__options.get(user_text)()
        else:
            io.print_text(f"{user_text} is not an instruction")

    def __end_application(self):
        self.__is_running = False

    @staticmethod
    def __show_menu() -> None:
        """Instrukcje dla menu głównego programu."""

        io.print_text(
            "What do you want to do?",
            "Pick the number:",
            "1. Encrypt text (ROT47/ROT13/ROT3)",
            "2. Decrypt all (ROT47/ROT13/ROT3)",
            "3. Peak buffer",
            "4. Write to JSON file",
            "5. Log out",
            "---> ",
        )

    def __encrypt_text(self) -> None:
        """Funkcja szyfrująca w podanym przez użytkownika rot."""

        rot: Rot = self.__get_encryptor()
        text: str = io.read("Please write down text to encrypt: ")
        encoded_text: str = rot.cipher(text)
        encrypted_text = {rot.rot_type(): [encoded_text]}
        self.__buffer.add(encrypted_text)

        # match rot.rot_type():
        #     case "Rot 13":
        #         self.__buffer.add_buffer_rot13(encoded_text)
        #     case "Rot 47":
        #         self.__buffer.add_buffer_rot47(encoded_text)

    def __decrypt_text(self) -> None:
        """Funkcja deszyfruje słowa o podanym przez użytkownika indeksie."""

        self.__buffer.create_dict()
        rot: Rot = self.__get_encryptor()
        index_of_word: int = int(io.read(
            f"Choose word index do decrypt [1 - {len(self.__buffer.buffer_dict[rot.rot_type()])}]: ")
        )
        # TODO odczyt z json i odszyfrowanie podanego słowa

        if len(self.__buffer.buffer_dict[rot.rot_type()]) > 0:
            if index_of_word <= (len(self.__buffer.buffer_dict[rot.rot_type()]) - 1):
                decrypted_text = rot.cipher(self.__buffer.buffer_dict[rot.rot_type()][index_of_word - 1])
                io.print_text("Decrypted word: ", f"{decrypted_text}")
            else:
                io.print_text("Index is out of range.")
        else:
            io.print_text("There are no words to decrypt.")

        # if rot.rot_type() == "Rot 13":
        #     for txt in self.__buffer.buffer_rot13:
        #         decrypted_text = rot.cipher(txt)
        #         self.__buffer.decrypted_rot13.append(decrypted_text)
        #     for i in self.__buffer.decrypted_rot13:
        #         print(i)
        # elif rot.rot_type() == "Rot 47":
        #     for txt in self.__buffer.buffer_rot47:
        #         decrypted_text = rot.cipher(txt)
        #         self.__buffer.decrypted_rot47.append(decrypted_text)
        #     for i in self.__buffer.decrypted_rot47:
        #         print(i)
        # else:
        #     io.print_text("Invalid option")
        #     return self.__get_encryptor()

    def __get_encryptor(self) -> Rot:
        """Funkcja pozwala na wybór rota, którego chce użyć użytkownik."""

        io.print_text(
            "Which cipher do you want to use?",
            "Pick the number",
            "1: ROT47",
            "2: ROT13",
            "3: ROT3",
        )
        encryptor_no = io.read("")
        if encryptor_no == "1":
            return Rot47()
        elif encryptor_no == "2":
            return Rot13()
        elif encryptor_no == "3":
            return Rot3()
        else:
            io.print_text("Invalid option")
            return self.__get_encryptor()

    def __write_to_file(self) -> None:
        """Funkcja pozwala użytkownikowi na zapis wyników do pliku json. Nazwę pliku określa użytkownik."""

        if not self.folder:
            fh.check()
            self.folder = True
        self.__buffer.create_dict()
        file_name = input("File_name: ")

        fh.write_json(file_name, self.__buffer.buffer_dict)
        io.print_text("Saved to file.")
