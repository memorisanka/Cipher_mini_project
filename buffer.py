class Buffer:
    def __init__(self):
        self.__buffer = []

    def add(self, message: dict) -> None:
        self.__buffer.append(message)

    def add_list(self, message: str) -> None:
        self.__buffer += message

    def peak(self) -> list:
        print(self.__buffer)
        return self.__buffer
