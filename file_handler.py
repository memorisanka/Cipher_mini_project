import os
import json
from typing import Any


class FileHandler:
    @staticmethod
    def check() -> None:
        if not os.path.isdir(os.getcwd() + '/files'):
            os.mkdir(os.getcwd() + "/files")


    @staticmethod
    def write_json(file_name: str, data: object) -> None:
        with open(f"files/{file_name}.json", "w") as f:
            json.dump(data, f, indent=6)

    @staticmethod
    def read_json(file_name: str) -> None:
        with open(f"files/{file_name}.json", "r") as f:
            data = json.load(f)

        print(data)
