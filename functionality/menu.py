from __future__ import annotations


class Menu:
    def __init__(self):
        self._encrypt = encrypt or Encrypt()
        self._decrypt = decrypt or Decrypt()
        self.options = {
            1: self._encrypt.enter_text_to_encrypt,
            2: self._encrypt.encrypt_rot13,
            3: self._encrypt.encrypt_rot47,
            4: "self.executor.decrypt",
            5: menu.exit_programm(),
        }

    def operation(self) -> None:
        menu.show_menu()

    def show_menu(self) -> None:
        choice = int(
            input(
                "Choose any option:\n1. Enter text to encrypt \n2. Encrypt using ROT13 \n"
                "3. Encrypt using ROT47 \n4. Decrypt text \n5. Exit programm\n--> "
            )
        )
        self.execute(choice)

    @staticmethod
    def show_error():
        print("Error!")

    def execute(self, choice: int) -> None:
        self.options.get(choice, self.show_error)()

    @staticmethod
    def exit_programm():
        print("Bye. Hope to see you again :)")
        exit()


class Encrypt:
    def __init__(self):
        self.text = ""

    def enter_text_to_encrypt(self):
        self.text = input("Enter text: ")

    def encrypt_rot13(self):
        ROT13 = 13
        encrypted_text_rot13 = ""
        for letter in range(len(self.text)):
            if ord(self.text[letter]) > 122 - ROT13:
                encrypted_text_rot13 += chr(ord(self.text[letter]) + ROT13 - 26)
            else:
                encrypted_text_rot13 += chr(ord(self.text[letter]) + ROT13)
        print(encrypted_text_rot13)
        return encrypted_text_rot13

    def encrypt_rot47(self):
        encrypted_text_rot47 = ""
        for letter in range(len(self.text)):
            j = ord(self.text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += self.text[letter]
        print(encrypted_text_rot47)
        return encrypted_text_rot47


class Decrypt:
    def operation1(self) -> str:
        pass

    def operation_z(self) -> str:
        pass


def client_code(menu: Menu) -> None:
    print(menu.operation(), end="")


if __name__ == "__main__":
    encrypt = Encrypt()
    decrypt = Decrypt()
    menu = Menu()
    client_code(menu)
