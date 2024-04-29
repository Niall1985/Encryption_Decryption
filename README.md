# Encryption and Decryption Program
This is a basic Python program that allows users to encrypt and decrypt messages using a simple substitution cipher. The program utilizes random shuffling of characters to generate encryption and decryption keys.

## How to Use
1. Run the Program: Execute the Python script encryption_decryption.py.
2. Input Options:
a. Enter E to proceed to Encryption.
b. Enter D to proceed to Decryption.
c. Enter Q to exit the program.
3. Encryption:
a. Enter the text you want to encrypt when prompted.
b. The program will generate a ciphertext using a substitution cipher and display both the plaintext and the ciphertext.
4. Decryption:
a. Enter the encrypted code (ciphertext) that you want to decrypt.
b. The program will match the ciphertext with its corresponding plaintext and display the decrypted message.
5. Exiting the Program:
a. Enter Q at any time to exit the program.
# How It Works
1. Encryption:
a. The program generates random keys by shuffling characters from ASCII letters, digits, and punctuation.
b. Each character in the plaintext is substituted with its corresponding character from the generated keys, producing the ciphertext.
2. Decryption:
a. The program utilizes a dictionary to store the plaintext-ciphertext pairs.
b. When decrypting, it searches for the ciphertext in the dictionary and retrieves the corresponding plaintext.
# Notes
This program is for educational purposes and demonstrates a basic encryption technique.
It is not suitable for secure communications as it uses a simple substitution cipher, which can be easily broken.
