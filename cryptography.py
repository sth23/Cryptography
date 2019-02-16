"""
cryptography.py
Author: Sean Healey
Credit: Tutorials

Assignment:

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"

# Encrypt function, x = unecrypted string, y = key
def encrypt(x,y):
    return x

# Decrypt function, x = encrypted string, y = key
def decrypt(x,y):
    return x

process = input("Enter e to encrypt, d to decrypt, or q to quit: ")
if process == "e":
    message = input("Message: ")
    key = input("Key: ")
    print(encrypt(message, key))
elif process == "d":
    message = input("Message: ")
    key = input("Key: ")
    print(decrypt(message, key)
#elif process == "q":
  #  Goodbye!
else:
    print("Did not understand command, try again.")