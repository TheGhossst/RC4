def rc4_key_scheduling(key):
    
    
    
def main():
    key = input("Enter the key as a string of ASCII characters : ")
    data = input("Enter the data to encrypt as a string of ASCII characters: ")

    key_bytes = [ord(char) for char in key]
    data_bytes = [ord(char) for char in data]
    
    steps = []

    key_scheduling = rc4_key_scheduling(key_bytes)
    steps.append(key_scheduling.copy())