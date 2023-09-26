def encode(text, key):
    cipher = make_cipher(key)
    print()
    print()
    print(cipher)
    print()
    print()
    ciphertext_chars = []
    for i in text:
        # alphabet = [chr(i + 98) for i in range(1, 26)] |||||| the ascii number in the comp was wrong
        ciphered_char = chr(65 + cipher.index(i))
        ciphertext_chars.append(ciphered_char)

    return "".join(ciphertext_chars)


def decode(encrypted, key):
    cipher = make_cipher(key)
    print()
    print()
    print(cipher)
    print()
    print()

    plaintext_chars = []
    for i in encrypted:
        # plain_char = cipher[65 - ord(i)] ||||| the operation in cipher was back to front
        plain_char = cipher[ord(i) - 65]
        print()
        print(ord(i))
        print()
        print(plain_char)
        print()
        print()
        plaintext_chars.append(plain_char)

    return "".join(plaintext_chars)


def make_cipher(key):
    alphabet = [chr(i + 97) for i in range(26)]
    print()
    print()
    print(alphabet)
    print()
    print()
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
