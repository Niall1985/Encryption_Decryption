import string
import random
import sys
chars = " " + string.ascii_letters + string.digits + string.punctuation
chars = list(chars)
keys = chars.copy()
random.shuffle(keys)

def program_run():
    user_input = input("Enter [encryption/decryption/exit]:").lower()
    if user_input == "encryption":
        plain_text()
    elif user_input == "decryption":
        cipher_text()
    elif user_input == "exit":
        sys.exit(0)

def plain_text():
    plain_text=input("Enter text to be encrypted:")
    cipher_text=""
    for letters in plain_text:
        index = chars.index(letters)
        cipher_text += keys[index]
    print(f"Plain Text:{plain_text}")
    print(f"Cipher Text:{cipher_text}")

def cipher_text():
    cipher_text=input("Enter text to be decrypted:")
    plain_text=""
    for letters in cipher_text:
        index = keys.index(letters)
        plain_text += chars[index]
    print(f"Cipher Text:{cipher_text}")
    print(f"Plain Text:{plain_text}")

while True:
    program_run()
