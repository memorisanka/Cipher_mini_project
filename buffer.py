class Buffer:
    __buffer = []
    buffer_dict = {}


    def __len__(self):
        return len(Buffer.__buffer)

    @staticmethod
    def add(message: dict) -> None:
        """Dodawanie rekordów do buffera."""

        Buffer.__buffer.append(message)

    @staticmethod
    def add_list(message: str) -> None:
        """Dodatnie listy do buffera."""

        Buffer.__buffer += message

    @staticmethod
    def peak() -> list:
        """Funkcja zwraca wszystkie rekordy w bufferze bez grupowania na poszczególne ROT'y"""
        Buffer.create_dict()
        print(Buffer.buffer_dict)
        return Buffer.buffer_dict

    @staticmethod
    def create_dict():
        """Funkcja tworzy słownik z buffera z podziałem na poszczególne ROT'y."""
        for dct in Buffer.__buffer:
            for key, value in dct.items():
                if key not in Buffer.buffer_dict.keys():
                    Buffer.buffer_dict[key] = []
                    Buffer.buffer_dict[key] += [value]
                else:
                    Buffer.buffer_dict[key] += [value]

