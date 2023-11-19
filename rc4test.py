
key = [1, 2, 3, 6]
plaintext = [1, 2, 2, 2]


ciphertext = rc4(key, plaintext)

print("\nKey:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)
