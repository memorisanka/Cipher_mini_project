from abc import ABC, abstractmethod
import string


class Rot(ABC):
    @staticmethod
    @abstractmethod
    def cipher(text: str):
        pass

    @abstractmethod
    def rot_type(self) -> str:
        pass

    @abstractmethod
    def rot_buffer(self):
        pass

    @staticmethod
    @abstractmethod
    def shift(c, n, alf):
        pass


class Rot13(Rot):
    @staticmethod
    def shift(c, n, alf):
        if c in alf:
            oldIdx = alf.index(c)
            newIdx = (oldIdx + n) % len(alf)
            return alf[newIdx]

    @staticmethod
    def cipher(text: str, n=13, alf=string.ascii_lowercase):
        alf_lower = alf.lower()
        alf_upper = alf.upper()
        result = ""
        for c in text:
            if c in alf_lower:
                result += Rot13.shift(c, n, alf_lower)
            elif c in alf_upper:
                result += Rot13.shift(c, n, alf_upper)
            else:
                result += c
        return result

    def rot_type(self) -> str:
        return "Rot 13"

    def rot_buffer(self):
        return "buffer_rot13"


class Rot47(Rot):
    @staticmethod
    def cipher(text: str):
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

    @staticmethod
    def shift(c, n, alf):
        pass


class Rot3(Rot):
    def cipher(self, text: str):
        pass

    def rot_type(self) -> str:
        return "Rot 3"

    def rot_buffer(self):
        return "buffer_rot3"

    @staticmethod
    def shift(c, n, alf):
        pass
