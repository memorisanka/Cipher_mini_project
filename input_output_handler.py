class InputOutputHandler:
    @staticmethod
    def print_text(*text_list: str) -> None:
        for text in text_list:
            print(text)

    @staticmethod
    def read(text: str) -> str:
        return input(text)
