class Cipher:

    def encrypt_rot13(self, txt):
        ROT13 = 13
        encrypted_text_rot13 = ""
        for i in range(len(txt)):
            if ord(txt[i]) > 122 - ROT13:
                encrypted_text_rot13 += chr(ord(txt[i]) + ROT13 - 26)
            else:
                encrypted_text_rot13 += chr(ord(txt[i]) + ROT13)
        return encrypted_text_rot13

    def encrypt_rot47(self):
        pass

