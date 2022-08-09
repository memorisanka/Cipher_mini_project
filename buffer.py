class Buffer:

    def __init__(self):
        self.__buffer = []
        self.buffer_dict = {}

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
                    # self.buffer_dict.update(dct)
                else:
                    self.buffer_dict[key] += [value]

        # return self.__buffer_dict

    def show_buffer_dict(self):
        print(self.buffer_dict)
