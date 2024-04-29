import string
import random
import sys
dict={}
def generate_keys():
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)
    return keys

def program_run():
    keys = generate_keys()
    chars = generate_keys()
    User_input=input("Enter E to proceed to Encryption, D to proceed to Decryption and Q to exit:")
    if User_input == 'E':
        plain_text(keys,chars)
    elif User_input == 'D':
        cipher_text()
    elif User_input == 'Q':
        sys.exit(0)
    else:
        print("Invalid Input")

def plain_text(keys,chars):
    plain_text=input("Enter text to be encrypted:")
    cipher_text=""
    for letters in plain_text:
        index = chars.index(letters)
        cipher_text += keys[index]
        dict[plain_text]=cipher_text
    print(f"Plain Text:{plain_text}")
    print(f"Cipher Text:{cipher_text}")

def cipher_text():
    cipher_text=input("Enter the Encrypted code which you want to Decrypt:")
    for key, value in dict.items():
        if value == cipher_text:
            print("Decrypted Message:",key)
        else:
            print("Incorrect Encryption input")

while True:
    program_run()
