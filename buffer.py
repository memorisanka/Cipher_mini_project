class Buffer:

    def __init__(self):
        self.__buffer = []
        self.buffer_dict = {}
        self.buffer_rot13 = []
        self.buffer_rot47 = []
        self.decrypted_rot13 = []
        self.decrypted_rot47 = []

    def add(self, message: dict) -> None:
        self.__buffer.append(message)

    def add_list(self, message: str) -> None:
        self.__buffer += message

    def peak(self) -> list:
        print(self.__buffer)
        return self.__buffer

    def create_dict(self):
        for dct in self.__buffer:
            for key, value in dct.items():
                if key not in self.buffer_dict.keys():
                    self.buffer_dict[key] = []
                    self.buffer_dict[key] += [value]
                else:
                    self.buffer_dict[key] += [value]

    def add_buffer_rot13(self, message: str):
        self.buffer_rot13.append(message)

    def add_buffer_rot47(self, message: str):
        self.buffer_rot47.append(message)
