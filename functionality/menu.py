class Menu:
    def __init__(self) -> None:
        self._cipher = cipher or Cipher()
        self.options = {
            1: self._cipher.encrypt_rot13,
            2: self._cipher.encrypt_rot47,
            3: self._cipher.decrypt_rot13,
            4: self._cipher.decrypt_rot47,
            5: self._cipher.write_buffer_to_file,
            6: self._cipher.show_buffer,
            7: Menu.exit_programm,
        }

    def operation(self) -> None:

        while True:
            menu.show_menu()

    def show_menu(self) -> None:

        choice = int(
            input(
                "Choose any option:\n------------------------\n1. Encrypt using ROT13 \n"
                "2. Encrypt using ROT47 \n3. Decrypt text using ROT13 \n4. Decrypt text using ROT47\n"
                "5. Save in file\n6. Read from buffer\n7. Exit programm\n--> "
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
        self.buffer = []

    def enter_text_to_encrypt(self):
        self.text = input("Enter text: ")
        cipher.write_file()

    def encrypt_rot13(self):
        cipher.enter_text_to_encrypt()

        encrypted_rot13 = "".join(
            [
                chr((ord(letter) - 97 + 13) % 26 + 97)
                if 97 <= ord(letter) <= 122
                else letter
                for letter in self.text.lower()
            ]
        )

        self.buffer.append(encrypted_rot13)

        print(f"Text after encryption: {encrypted_rot13}\n")
        return encrypted_rot13

    def encrypt_rot47(self):
        cipher.enter_text_to_encrypt()

        encrypted_text_rot47 = ""
        for letter in range(len(self.text)):
            j = ord(self.text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += self.text[letter]

        self.buffer.append(encrypted_text_rot47)

        print(f"Text after encryption: {encrypted_text_rot47}\n")
        return encrypted_text_rot47

    def decrypt_rot13(self):

        encrypted_rot13 = "".join(
            [
                chr((ord(letter) - 97 + 13) % 26 + 97)
                if 97 <= ord(letter) <= 122
                else letter
                for letter in self.text.lower()
            ]
        )

        print(f"Text after encryption ROT13: {encrypted_rot13}")
        return encrypted_rot13

    def decrypt_rot47(self):

        encrypted_text_rot47 = ""
        for letter in range(len(self.text)):
            j = ord(self.text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += self.text[letter]
        print(f"Text after encryption ROT47: {encrypted_text_rot47}")
        return encrypted_text_rot47

    def write_file(self):
        with open("text_to_encrypt.txt", "w",  encoding="utf-8") as f:
            f.write(self.text)

    def read_file(self):
        with open("text_to_encrypt.txt", "r", encoding="utf-8") as f:
            f.read()

    def show_buffer(self):
        for txt in self.buffer:
            print(txt)

    def write_buffer_to_file(self):
        with open("buffer.txt", "a",  encoding="utf-8") as f:
            for i in self.buffer:
                f.write(i + "\n")


def client_code(menu: Menu) -> None:
    print(menu.operation(), end="")


if __name__ == "__main__":
    cipher = Cipher()
    menu = Menu()
    client_code(menu)
