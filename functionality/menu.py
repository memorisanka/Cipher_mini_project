class Menu:
    def __init__(self):
        self.executor = Executor()
        self.options = {
            1: self.executor.enter_text_to_encrypt,
            2: self.executor.encrypt_rot13,
            3: self.executor.encrypt_rot47,
            4: self.executor.decrypt,
            5: self.executor.exit_programm,
        }

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


class Executor:
    @staticmethod
    def enter_text_to_encrypt():
        text_to_encrypt = input("Enter text: ")
        Executor.write_text(text_to_encrypt)
        return text_to_encrypt

    def encrypt_rot13(self, text):
        ROT13 = 13
        encrypted_text_rot13 = ""
        for letter in range(len(text)):
            if ord(text[letter]) > 122 - ROT13:
                encrypted_text_rot13 += chr(ord(text[letter]) + ROT13 - 26)
            else:
                encrypted_text_rot13 += chr(ord(text[letter]) + ROT13)
        return encrypted_text_rot13

    def encrypt_rot47(self, text):
        encrypted_text_rot47 = ""
        for letter in range(len(text)):
            j = ord(text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += text[letter]
        return encrypted_text_rot47

    def decrypt(self):
        pass

    @staticmethod
    def exit_programm():
        print("Bye. Hope to see you again :)")
        exit()

    def write_text(self, text):
        with open ("text_to_encrypt.txt", "-w", encoding="utf-8") as f:
            f.write(text)


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == "__main__":
    main()
