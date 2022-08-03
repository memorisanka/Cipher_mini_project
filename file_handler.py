import os
import json


class FileHandler:
    @staticmethod
    def check(file_name: str):
        return os.path.isdir((os.getcwd() + f"/{file_name}"))

    @staticmethod
    def write_json(file_name: str, data: dict):
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def read_json(file_name: str):
        with open(f"{file_name}.json", "r") as f:
            data = json.load(f)
        
        print(data)

# FILEHANDLER files, czy istnieje
