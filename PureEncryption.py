import string
import random
import sys
def generate_keys():
    chars = " " + string.ascii_letters + string.digits + string.punctuation
    chars = list(chars)
    keys = chars.copy()
    random.shuffle(keys)
    return keys

def program_run():
    keys = generate_keys()
    chars = generate_keys()
    User_input=input("Enter E to proceed to Encryption and Q to exit:")
    if User_input == 'E':
        plain_text(keys,chars)
    else:
        sys.exit(0)

def plain_text(keys,chars):
    plain_text=input("Enter text to be encrypted:")
    cipher_text=""
    for letters in plain_text:
        index = chars.index(letters)
        cipher_text += keys[index]
    print(f"Plain Text:{plain_text}")
    print(f"Cipher Text:{cipher_text}")

while True:
    program_run()
