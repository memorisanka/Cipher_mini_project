from functionality.cipher import Cipher


class Menu:
    def __init__(self):
        self.executor = Executor()
        self.cipher = Cipher()
        self.options = {
            1: self.executor.enter_text_to_encrypt,
            2: self.executor.do_sth_two,
            3: self.executor.do_sth_three,
            4: self.executor.do_sth_four,
            5: self.executor.do_sth_five,
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

    def execute(self, choice: int):
        self.options.get(choice, self.show_error)()


class Executor:
    def enter_text_to_encrypt(self) -> str:
        text_to_encrypt = input("Enter text: ")
        return text_to_encrypt

    def do_sth_two(self):
        pass

    def do_sth_three(self):
        pass

    def do_sth_four(self):
        pass

    @staticmethod
    def do_sth_five():
        print("Bye. Hope to see you again :)")
        exit()


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == "__main__":
    main()
