# Password_Hash_Cracker

This project demonstrates a basic password cracking technique using a dictionary attack. The program attempts to recover a password by comparing SHA256 hashes of words from a wordlist against a target hash.

This project was inspired by my work with John the Ripper and helped me understand how password cracking tools operate on a smaller scale by performing hash comparisons against large wordlists.

## Features
- SHA256 password hashing
- Dictionary attack using a wordlist file
- Hash comparison to recover plaintext passwords

## How It Works
1. The user enters a SHA256 password hash.
2. The program reads passwords from a wordlist file.
3. Each word is hashed and compared to the target hash.
4. If a match is found, the original password is revealed.

## Creating Your Own Wordlist

You can test your own password hashes by creating a custom wordlist.

1. Create a text file named:

wordlist.txt

2. Add possible passwords you want to test, one per line. Example:

password  
123456  
computer  
duckies  
orange  

3. Run the program and enter the hash you want to crack. The program will test each word in the list.

## Example

=== Password Hash Cracker ===

Enter SHA256 hash to crack: <hash_here>

Starting dictionary attack...

Password found: duckies
