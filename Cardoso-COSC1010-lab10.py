# Isabella Cardoso
# UWYO COSC 1010
# 11/22/2024
# Lab 10
# Lab Section: 12
# Sources, people worked with, help given to: Kelly Joyce
# your
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()



# Files and Exceptions

# For this assignment, you will be writing a program to "crack" a password. You will need to open the file `hash` as this is the password you are trying to "crack."

# To begin, you will need to open the 'rockyou.txt' file:
# - This file contains a list of compromised passwords from the rockyou dump.
# - This is an abridged version, as the full version is quite large.
# - The file contains the plaintext version of the passwords. You will need to hash them to check against the password hash you are trying to crack.
#   - You can use the provided `get_hash()` function to generate the hashes.
#   - Be careful, as "hello" and "hello " would generate a different hash.

try:
    password = Path('hash')
    hash = password.read_text()
except:
    print("this file does not exist")

# You will need to include a try-except-catch block in your code.
# - The reading of files needs to occur in the try blocks.

try:
    possible_passwords = Path('rockyou.txt')
    passwords = possible_passwords.read_text()
except:
    print("This file does not exist")
else:
    passwords = passwords.splitlines()

# - Read in the value stored within `hash`.
#   - You must use a try and except block.

for line in passwords:
    hash_it = get_hash(line)

    if hash_it == hash:
        print(line)
        break

# Read in the passwords in `rockyou.txt`.
# - Again, you need a try-except-else block.
# Hash each individual password and compare it against the stored hash.
# - When you find the match, print the plaintext version of the password.
# - End your loop.
