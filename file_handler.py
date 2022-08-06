import os
import json
from typing import Any


class FileHandler:
    @staticmethod
    def check(file_name: str) -> Any:
        try:
            path = os.path.isdir((os.getcwd() + f"/{file_name}.json"))
            if not path:
                raise FileNotFoundError("File doesn't exist.")
        except FileNotFoundError:
            return "File doesn't exist."
        else:
            return True

    @staticmethod
    def write_json(file_name: str, data: object) -> None:
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f, indent=6)

    @staticmethod
    def read_json(file_name: str) -> None:
        with open(f"{file_name}.json", "r") as f:
            data = json.load(f)

        print(data)
