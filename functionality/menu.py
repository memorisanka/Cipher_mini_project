class Menu:
    def __init__(self) -> None:
        self._cipher = cipher or Cipher()
        self.options = {
            1: self._cipher.rot13,
            2: self._cipher.rot47,
            3: self._cipher.rot13,
            4: Menu.exit_programm,
        }

    @staticmethod
    def operation() -> None:
        menu.show_menu()

    def show_menu(self) -> None:
        choice = int(
            input(
                "Choose any option:\n------------------------\n1. Encrypt using ROT13 \n"
                "2. Encrypt using ROT47 \n3. Decrypt text \n4. Exit programm\n--> "
            )
        )
        self.execute(choice)

    @staticmethod
    def show_error() -> None:
        print("Error!")

    def execute(self, choice: int) -> None:
        self.options.get(choice, self.show_error)()

    @staticmethod
    def exit_programm() -> None:
        print("Bye. Hope to see you again :)")
        exit()


class Cipher:
    """The same function encrypt and decrypt ROT13, so as ROT47. Running the function once again on encrypted text
    cause decryption."""

    def __init__(self):
        self.text = ""

    def enter_text_to_encrypt(self):
        self.text = input("Enter text: ")
        cipher.write_file()

    def rot13(self):
        cipher.enter_text_to_encrypt()

        encrypted_rot13 = "".join(
            [
                chr((ord(letter) - 97 + 13) % 26 + 97)
                if 97 <= ord(letter) <= 122
                else letter
                for letter in self.text.lower()
            ]
        )

        print(encrypted_rot13)
        return encrypted_rot13

    def rot47(self):
        cipher.enter_text_to_encrypt()

        encrypted_text_rot47 = ""
        for letter in range(len(self.text)):
            j = ord(self.text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += self.text[letter]
        print(encrypted_text_rot47)
        return encrypted_text_rot47

    def write_file(self):
        with open("text_to_encrypt.txt", "w",  encoding="utf-8") as f:
            f.write(self.text)

    def read_file(self):
        with open("text_to_encrypt.txt", "r", encoding="utf-8") as f:
            f.read()


def client_code(menu: Menu) -> None:
    print(menu.operation(), end="")


if __name__ == "__main__":
    cipher = Cipher()
    menu = Menu()
    client_code(menu)
