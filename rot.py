from abc import ABC, abstractmethod


class Rot(ABC):
    @abstractmethod
    def cipher(self, text: str):
        pass

    @abstractmethod
    def rot_type(self) -> str:
        pass

    @abstractmethod
    def rot_buffer(self):
        pass


class Rot13(Rot):
    def cipher(self, text: str):
        encrypted_rot13 = "".join(
            [
                chr((ord(letter) - 97 + 13) % 26 + 97)
                if 97 <= ord(letter) <= 122
                else letter
                for letter in text.lower()
            ]
        )
        return encrypted_rot13

    def rot_type(self) -> str:
        return "Rot 13"

    def rot_buffer(self):
        return "buffer_rot13"


class Rot47(Rot):
    def cipher(self, text: str):
        encrypted_text_rot47 = ""
        for letter in range(len(text)):
            j = ord(text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += text[letter]
        return encrypted_text_rot47

    def rot_type(self) -> str:
        return "Rot 47"

    def rot_buffer(self):
        return "buffer_rot47"


class Rot3(Rot):
    def cipher(self, text: str):
        pass

    def rot_type(self) -> str:
        return "Rot 3"

    def rot_buffer(self):
        return "buffer_rot3"
