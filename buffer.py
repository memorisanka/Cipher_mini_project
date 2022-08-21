class Buffer:

    def __init__(self):
        self.__buffer = []
        self.buffer_dict = {}

    def add(self, message: dict) -> None:
        """Dodawanie rekordów do buffera."""

        self.__buffer.append(message)

    def add_list(self, message: str) -> None:
        """Dodatnie listy do buffera."""

        self.__buffer += message

    def peak(self) -> list:
        """Funkcja zwraca wszystkie rekordy w bufferze bez grupowania na poszczególne ROT'y"""

        print(self.__buffer)
        return self.__buffer

    def create_dict(self):
        """Funkcja tworzy słownik z buffera z podziałem na poszczególne ROT'y."""
        for dct in self.__buffer:
            for key, value in dct.items():
                if key not in self.buffer_dict.keys():
                    self.buffer_dict[key] = []
                    self.buffer_dict[key] += [value]
                else:
                    self.buffer_dict[key] += [value]

