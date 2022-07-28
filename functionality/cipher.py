class Cipher:
    def encrypt_rot13:
        zaszyfrowny = ""
        for i in range(len(txt)):
            if ord(txt[i]) > 122 - KLUCZ:
                zaszyfrowny += chr(ord(txt[i]) + KLUCZ - 26)
            else:
                zaszyfrowny += chr(ord(txt[i]) + KLUCZ)
        return zaszyfrowny