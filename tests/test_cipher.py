from functionality.menu import Cipher

def test_should_return_true_if_function_encrypt_text_with_rot13():

    assert encrypt_rot13("Ala ma kota") == "Nyn zn xbgn"
