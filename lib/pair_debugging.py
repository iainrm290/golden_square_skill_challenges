def encode(text, key):
    print(f"!!!!!!!!!!{text}")
    print(f"!!!!!!!!!!{key}")
    cipher = make_cipher(key)

    ciphertext_chars = []

    print("!!!!!!!!!!!!!!Loop starts!!!")
    for i in text:
        ciphered_char = chr(65 + cipher.index(i))
        print(f"{ciphered_char}")
        ciphertext_chars.append(ciphered_char)

    print("!!!!!!!!!!!!!!Loop ends!!!")
    return "".join(ciphertext_chars)


# iusbfnivniuw


def decode(encrypted, key):
    print(f"!!!ENCRYPTION  {encrypted}")
    print(f"!!!KEY  {key}")
    cipher = make_cipher(key)


    plaintext_chars = []
    print("!!!LOOP STARTS!!!!!")
    for i in encrypted:
        plain_char = cipher[ord(i) - 65]
        print(f"Plain Char ==== {plain_char}")
        plaintext_chars.append(plain_char)
        print(f"Plain Text Chars ==== {plaintext_chars}")
    print("!!!LOOP ENDS!!!")
    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(26)]
    print(f"ALPHABET IS: {alphabet}")
    cipher_with_duplicates = list(key) + alphabet

    cipher = []
    for i in range(0, len(cipher_with_duplicates)):
        if cipher_with_duplicates[i] not in cipher_with_duplicates[:i]:
            cipher.append(cipher_with_duplicates[i])

    return cipher

# When you run this file, these next lines will show you the expected
# and actual outputs of the functions above.
print(f"""
 Running: encode("theswiftfoxjumpedoverthelazydog", "secretkey")
Expected: EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL
  Actual: {encode('theswiftfoxjumpedoverthelazydog', 'secretkey')}
""")

print(f"""
 Running: decode("EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL", "secretkey")
Expected: theswiftfoxjumpedoverthelazydog
  Actual: {decode('EMBAXNKEKSYOVQTBJSWBDEMBPHZGJSL', 'secretkey')}
""")
# iubwiruybviuwbsuiviuw   wfiuhriuh