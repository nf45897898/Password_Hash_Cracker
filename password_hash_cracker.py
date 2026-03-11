"""
Password Hash Cracker
Author: Nicholas Fernandez

Demonstrates SHA256 password hashing and dictionary attacks
using a wordlist file.
"""

import hashlib


# -----------------------------------------------------
# Generate SHA256 hash of a password
# -----------------------------------------------------
def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


# -----------------------------------------------------
# Dictionary attack using a wordlist file
# -----------------------------------------------------
def dictionary_attack(target_hash, wordlist_file):

    print("Starting dictionary attack...\n")

    # open wordlist file
    with open(wordlist_file, "r") as f:

        for word in f:

            # remove newline characters
            word = word.strip()

            # hash current word
            hashed = hash_password(word)

            # check if hashes match
            if hashed == target_hash:

                print("Password found:", word)
                return word

    print("Password not found in wordlist")
    return None


# -----------------------------------------------------
# Main program
# -----------------------------------------------------
def main():

    print("=== Password Hash Cracker ===\n")

    # user enters hash they want to crack
    target_hash = input("Enter SHA256 hash to crack: ")

    # wordlist file name
    wordlist_file = "wordlist.txt"

    dictionary_attack(target_hash, wordlist_file)


if __name__ == "__main__":
    main()
