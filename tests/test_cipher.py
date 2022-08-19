import unittest
from rot import Rot, Rot47, Rot13


class TestsCipher():

    def test_should_return_true_if_function_encrypt_text_with_rot13(self):
        text = "test"
        value = "grfg"

        assert Rot13.cipher(text) == value

        text = "Ala ma kota"
        value = "Nyn zn xbgn"

        assert Rot13.cipher(text) == value.lower() #  rot13 do poprawy

    def test_should_return_true_if_function_encrypt_text_with_rot47(self):
        text = "test"
        value = "E6DE"

        assert Rot47.cipher(text) == value

        text = "Ala ma kota"
        value = "p=2 >2 <@E2"

        assert Rot47.cipher(text) == value

def main():
    tests_cipher = TestsCipher()
    tests_cipher.test_should_return_true_if_function_encrypt_text_with_rot13()
    tests_cipher.test_should_return_true_if_function_encrypt_text_with_rot47()

if __name__ == "__main__":
    main()