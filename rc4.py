def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

def rc4_key_scheduling(key):
    key_length = len(key)
    S = list(range(256))
    i=0
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        swap(S, i, j)

    return S
    
    
def main():
    key = input("Enter the key as a string of ASCII characters : ")
    data = input("Enter the data to encrypt as a string of ASCII characters: ")

    key_bytes = [ord(char) for char in key]
    data_bytes = [ord(char) for char in data]
    
    steps = []

    key_scheduling = rc4_key_scheduling(key_bytes)
    steps.append(key_scheduling.copy())