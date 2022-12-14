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

    @staticmethod
    @abstractmethod
    def shift(c, n, alf):
        pass


class Rot13(Rot):
    @staticmethod
    def shift(char: str, n: int, alf: str) -> str:
        if char in alf:
            old_idx: int = alf.index(char)
            new_idx: int = (old_idx + n) % len(alf)
            return alf[new_idx]

    @staticmethod
    def cipher(text: str, n=13, alf=string.ascii_lowercase) -> str:
        alf_lower: str = alf.lower()
        alf_upper: str = alf.upper()
        result: str = ""
        for char in text:
            if char in alf_lower:
                result += Rot13.shift(char, n, alf_lower)
            elif char in alf_upper:
                result += Rot13.shift(char, n, alf_upper)
            else:
                result += char
        return result

    def rot_type(self) -> str:
        return "Rot 13"


class Rot47(Rot):
    @staticmethod
    def cipher(text: str) -> str:
        encrypted_text_rot47: str = ""
        for letter in range(len(text)):
            j = ord(text[letter])
            if 33 <= j <= 126:
                encrypted_text_rot47 += chr(33 + (j + 14) % 94)
            else:
                encrypted_text_rot47 += text[letter]
        return encrypted_text_rot47

    def rot_type(self) -> str:
        return "Rot 47"

    @staticmethod
    def shift(c, n, alf):
        pass


class Rot3(Rot):
    @staticmethod
    def cipher(text: str, n=3, alf=string.ascii_lowercase) -> str:
        alf_lower: str = alf.lower()
        alf_upper: str = alf.upper()
        result: str = ""
        for char in text:
            if char in alf_lower:
                result += Rot3.shift(char, n, alf_lower)
            elif char in alf_upper:
                result += Rot3.shift(char, n, alf_upper)
            else:
                result += char
        return result

    def rot_type(self) -> str:
        return "Rot 3"

    @staticmethod
    def shift(char: str, n: int, alf: str) -> str:
        if char in alf:
            old_idx: int = alf.index(char)
            new_idx: int = (old_idx + n) % len(alf)
            return alf[new_idx]


class RotAny(Rot):
    user_shift = 0
    @staticmethod
    def shift(char: str, n: int, alf: str) -> str:
        if char in alf:
            old_idx: int = alf.index(char)
            new_idx: int = (old_idx + n) % len(alf)
            return alf[new_idx]

    @staticmethod
    def cipher(text: str, alf=string.ascii_lowercase) -> str:
        RotAny.user_shift = int(input("Enter shift (1-25): "))
        alf_lower: str = alf.lower()
        alf_upper: str = alf.upper()
        result: str = ""
        for char in text:
            if char in alf_lower:
                result += RotAny.shift(char, RotAny.user_shift, alf_lower)
            elif char in alf_upper:
                result += RotAny.shift(char, RotAny.user_shift, alf_upper)
            else:
                result += char
        return result

    def rot_type(self) -> str:
        return f"Rot {RotAny.user_shift}"
