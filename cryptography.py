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
    encrypted = ""
    decrypt_chars = list(x)
    key_chars = list(y)
    decrypt_nums = [associations.index(x) for x in decrypt_chars]
    key_nums = [associations.index(x) for x in key_chars]
    encrypt_nums = []
    key_count = 0
    for x in decrypt_nums:
        encrypt_nums.append(x + key_nums[key_count % len(key_nums)])
        key_count += 1
    encrypt_chars = [associations[x % len(associations)] for x in encrypt_nums]
    encrypted = ''.join(encrypt_chars)
    return encrypted

# Decrypt function, x = encrypted string, y = key
def decrypt(x,y):
    decrypted = ""
    encrypt_chars = list(x)
    key_chars = list(y)
    encrypt_nums = [association.index(x) for x in encrypt_chars]
    key_nums = [associations.index(x) for x in key_chars]
    decrypt_nums = []
    key_count = 0
    for x in encrypt_nums:
        decrypt_nums.append(x - key_nums[key_count % len(key_nums)])
        key_count += 1
    decrypt_chars = [associations[x % len(associations)] for x in decrypt_nums]
    decrypted = ''.join(decrypt_chars)
    return decrypted

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