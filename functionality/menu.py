class Menu:
    def __init__(self):
        self.executor = Executor()
        self.options = {1: self.executor.do_sth_one, 2: self.executor.do_sth_two, 3: self.executor.do_sth_three}

    def show_menu(self):
        choice = int(input("Choose any option:\n1. Enter text to encrypt \n2. Encrypt using ROT13 \n"
                           "3. Encrypt using ROT47 \n4. Decrypt text \n5. Exit programm"))
        self.execute(choice)

    @staticmethod
    def show_error():
        print("Error!")

    def execute(self, choice: int):
        self.options.get(choice, self.show_error)


class Executor:
    def do_sth_one(self):
        pass

    def do_sth_two(self):
        pass

    def do_sth_three(self):
        pass


def main():
    menu = Menu()
    menu.show_menu()


if __name__ == "__main__":
    main()
