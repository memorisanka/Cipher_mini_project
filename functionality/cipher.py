def encrypt_rot47(text):
    encrypted_text_rot47 = ""
    for letter in range(len(text)):
        j = ord(text[letter])
        if 33 <= j <= 126:
            encrypted_text_rot47 += chr(33 + (j + 14) % 94)
        else:
            encrypted_text_rot47 += text[letter]
    return encrypted_text_rot47

def encrypt_rot13(text):
    ROT13 = 13
    encrypted_text_rot13 = ""
    for letter in range(len(text)):
        if ord(text[letter]) > 122 - ROT13:
            encrypted_text_rot13 += chr(ord(text[letter]) + ROT13 - 26)
        else:
            encrypted_text_rot13 += chr(ord(text[letter]) + ROT13)
    return encrypted_text_rot13


print(encrypt_rot47("Ala ma kota"))
print(encrypt_rot13("Ala ma kota"))