def rc4(key, plaintext):
    #KSA
    S = list(range(4))
    i=0
    j = 0
    T=[1,2,3,6]
    print("Initial State (S):", S)
    print("T = ",T)
    for i in range(0,4,1):
        j = (j + S[i] + T[i]) % 4
        print("Value of S[i] and T[i] is ",S[i],T[i])
        S[i], S[j] = S[j], S[i]
        print("Value of j is ",j)
        print(f"After iteration {i+1} (KSA):", S)
    print("\n\n")
    # PRGA
    i = j = 0
    key_stream = []

    for _ in range(len(plaintext)):
        i = (i + 1) % 4
        j = (j + S[i]) % 4
        print("Value of i is ",i)
        print("Value of j is ",j)
        S[i], S[j] = S[j], S[i]
        key_byte = S[(S[i] + S[j]) % 4]
        key_stream.append(key_byte)
        print(f"After iteration {_ + 1} (PRGA):", S)

    print("Key Stream:", key_stream)

    # XOR
    ciphertext = [plaintext[i] ^ key_stream[i] for i in range(len(plaintext))]
    return ciphertext
    
    
key = [1, 2, 3, 6]
plaintext = [1, 2, 2, 2]


ciphertext = rc4(key, plaintext)

print("\nKey:", key)
print("Plaintext:", plaintext)
print("Ciphertext:", ciphertext)

"""
Initial State (S): [0, 1, 2, 3]
T =  [1, 2, 3, 6]
Value of S[i] and T[i] is  0 1
Value of j is  1
After iteration 1 (KSA): [1, 0, 2, 3]
Value of S[i] and T[i] is  0 2
Value of j is  3
After iteration 2 (KSA): [1, 3, 2, 0]
Value of S[i] and T[i] is  2 3
Value of j is  0
After iteration 3 (KSA): [2, 3, 1, 0]
Value of S[i] and T[i] is  0 6
Value of j is  2
After iteration 4 (KSA): [2, 3, 0, 1]



Value of i is  1
Value of j is  3
After iteration 1 (PRGA): [2, 1, 0, 3]
Value of i is  2
Value of j is  3
After iteration 2 (PRGA): [2, 1, 3, 0]
Value of i is  3
Value of j is  3
After iteration 3 (PRGA): [2, 1, 3, 0]
Value of i is  0
Value of j is  1
After iteration 4 (PRGA): [1, 2, 3, 0]
Key Stream: [2, 0, 2, 0]

Key: [1, 2, 3, 6]
Plaintext: [1, 2, 2, 2]
Ciphertext: [3, 2, 0, 2]
"""