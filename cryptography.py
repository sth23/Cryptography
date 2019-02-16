"""
cryptography.py
Author: Sean Healey
Credit: Tutorials, Stack Overflow

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

# Encrypt function, x = unecrypted string, y = key
def encrypt(x,y):
    message_chars = list(x)
    key_chars = list(y)
    return x

# Decrypt function, x = encrypted string, y = key
def decrypt(x,y):
    return x

# Takes user input to initiate program
process = ""
while process != "q": # program runs as long as process != q
    process = input("Enter e to encrypt, d to decrypt, or q to quit: ")
    if process == "e":
        message = input("Message: ")
        key = input("Key: ")
        print(encrypt(message, key))
    elif process == "d":
        message = input("Message: ")
        key = input("Key: ")
        print(decrypt(message, key))
    elif process == "q":
        print("Goodbye!")
    else:
        print("Did not understand command, try again.")