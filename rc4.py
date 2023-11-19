def main():
    key = input("Enter the key as a string of ASCII characters : ")
    data = input("Enter the data to encrypt as a string of ASCII characters: ")

    key_bytes = [ord(char) for char in key]
    data_bytes = [ord(char) for char in data]