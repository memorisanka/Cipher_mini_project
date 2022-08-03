import os


class FileHandler:
    @staticmethod
    def check(file: str):
        return os.path.isdir((os.getcwd() + f"/{file}"))

    def write(self):
        pass

    def read(self):
        pass


# FILEHANDLER files, czy istnieje
