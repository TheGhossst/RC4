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
    
def rc4_pseudo_random_generation(S, data):
    i, j = 0, 0
    result = []
    
def main():
    key = input("Enter the key as a string of ASCII characters : ")
    data = input("Enter the data to encrypt as a string of ASCII characters: ")

    key_bytes = [ord(char) for char in key]
    data_bytes = [ord(char) for char in data]
    
    steps = []

    key_scheduling = rc4_key_scheduling(key_bytes)
    steps.append(key_scheduling.copy())
    
    pseudo_random_data = rc4_pseudo_random_generation(key_scheduling, data_bytes)
    steps.append(pseudo_random_data.copy())
    
    print("\nKey Scheduling:")
    display_steps(steps[0])
    print("\nPseudo-random Data Generation:")
    display_steps(steps[1])
    print("\nFinal Result:")
    display_steps(pseudo_random_data)

if __name__ == "__main__":
    main()
