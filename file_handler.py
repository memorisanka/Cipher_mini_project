import os
import json


class FileHandler:
    @staticmethod
    def check(file_name: str):
        return os.path.isdir((os.getcwd() + f"/{file_name}"))

    @staticmethod
    def write_json(file_name: str, data: dict):
        with open(f'{file_name}.json', 'w') as f:
            json.dump(data, f)

    def read_json(self):
        pass


# FILEHANDLER files, czy istnieje
