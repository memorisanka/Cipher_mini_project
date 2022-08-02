from abc import ABC, abstractmethod

class Rot(ABC):
    @abstractmethod
    def cipher(self, text: str):
        pass
    # @abstractmethod
    # def rot_type(self) -> str:
    #     pass

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


        print(f"Text after encryption: {encrypted_rot13}\n")
        return encrypted_rot13


class Rot47(Rot):
    def cipher(self, text: str):
        encrypted_text_rot47 = ""
        for letter in range(len(text)):
            j = ord(text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += text[letter]
        print(f"Text after encryption: {encrypted_text_rot47}\n")
        return encrypted_text_rot47

class Rot3(Rot):
    def cipher(self, text: str):
        pass