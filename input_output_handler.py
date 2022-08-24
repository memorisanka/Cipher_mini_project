class InputOutputHandler:
    @staticmethod
    def print_text(*text_list: str) -> None:
        """Print arguments on separate lines."""

        for text in text_list:
            print(text)

    @staticmethod
    def read(text: str) -> str:
        """Get a value from user."""

        return input(text)
