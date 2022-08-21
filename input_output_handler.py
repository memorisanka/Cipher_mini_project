class InputOutputHandler:
    @staticmethod
    def print_text(*text_list: str) -> None:
        """Funkcja wyświetla napisy podane jako argumenty w formie listy."""

        for text in text_list:
            print(text)

    @staticmethod
    def read(text: str) -> str:
        """Funkcja służąca do pobierania wartości od użytkownika."""

        return input(text)
