class Buffer:

    def __init__(self):
        self.__buffer = []
        self.__buffer_dict = {}

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
                if key not in self.__buffer_dict.keys():
                    self.__buffer_dict.update(dict)
                else:
                    self.__buffer_dict[key] += [value]

        return self.__buffer_dict

    def show_buffer_dict(self):
        print(self.__buffer_dict)
