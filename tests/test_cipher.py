from rot import Rot47, Rot13, Rot3, RotAny


class TestsCipher:
    def test_should_return_true_if_function_encrypt_text_with_rot3(self):
        text = "test"
        result = "whvw"

        assert Rot3.cipher(text) == result

        text = "Ala ma kota"
        result = "Dod pd nrwd"

        assert Rot3.cipher(text) == result

        text = "Nauka to lubię!"
        result = "Qdxnd wr oxelę!"

        assert Rot3.cipher(text) == result

    def test_should_return_true_if_function_encrypt_text_with_rot13(self):
        text = "test"
        result = "grfg"

        assert Rot13.cipher(text) == result

        text = "Ala ma kota"
        result = "Nyn zn xbgn"

        assert Rot13.cipher(text) == result

        assert Rot13.cipher(text) == result

        text = "Nauka to lubię!"
        result = "Anhxn gb yhovę!"

        assert Rot13.cipher(text) == result

    def test_should_return_true_if_function_encrypt_text_with_rot47(self):
        text = "test"
        result = "E6DE"

        assert Rot47.cipher(text) == result

        text = "Ala ma kota"
        result = "p=2 >2 <@E2"

        assert Rot47.cipher(text) == result

        text = "Nauka to lubię!"
        result = "}2F<2 E@ =F3:ęP"

        assert Rot47.cipher(text) == result

    # def test_should_return_true_if_function_encrypt_text_with_rotAny(self):
    #     text = "test"
    #     result = "whvw"
    #
    #     assert RotAny.cipher(text) == result
    #
    #     text = "Ala ma kota"
    #     result = "Dod pd nrwd"
    #
    #     assert RotAny.cipher(text) == result
    #
    #     text = "Nauka to lubię!"
    #     result = "Qdxnd wr oxelę!"
    #
    #     assert RotAny.cipher(text) == result


def main():
    tests_cipher = TestsCipher()
    tests_cipher.test_should_return_true_if_function_encrypt_text_with_rot3()
    tests_cipher.test_should_return_true_if_function_encrypt_text_with_rot13()
    tests_cipher.test_should_return_true_if_function_encrypt_text_with_rot47()
    # tests_cipher.test_should_return_true_if_function_encrypt_text_with_rotAny()


if __name__ == "__main__":
    main()
