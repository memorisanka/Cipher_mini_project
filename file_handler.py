import os
import json
from typing import Any


class FileHandler:
    @staticmethod
    def check(file_name: str, data: object) -> Any:
        if os.path.isdir((os.getcwd() + f"/{file_name}")):
            FileHandler.write_json(file_name, data)
        else:
            with open(file_name, "w", encoding="UTF-8") as f:
                f.write("")
            FileHandler.write_json(file_name, data)

    @staticmethod
    def write_json(file_name: str, data: object) -> None:
        with open(f"{file_name}.json", "w") as f:
            json.dump(data, f)

    @staticmethod
    def read_json(file_name: str) -> None:
        with open(f"{file_name}.json", "r") as f:
            data = json.load(f)

        print(data)

# FILEHANDLER files, czy istnieje
