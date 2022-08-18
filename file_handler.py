import os
import json


class FileHandler:
    @staticmethod
    def check() -> None:
        """Funkcja sprawdza, czy podany plik istnieje"""

        if not os.path.isdir(os.getcwd() + "/files"):
            os.mkdir(os.getcwd() + "/files")

    @staticmethod
    def write_json(file_name: str, data: object) -> None:
        """Funkcja zapisuje dane do pliku json."""

        with open(f"files/{file_name}.json", "w") as f:
            json.dump(data, f, indent=6)

    @staticmethod
    def read_json(file_name: str) -> None:
        """Funkcja pobiera dane z pliku json."""

        with open(f"files/{file_name}.json", "r") as f:
            data = json.load(f)

        print(data)
