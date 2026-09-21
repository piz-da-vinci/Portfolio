Caesar Cipher Program

Overview

This is a simple Python script designed to encrypt and decrypt text using the classic Caesar Cipher algorithm. It works seamlessly with English text while preserving both uppercase and lowercase letters, as well as spaces, numbers, and special symbols.

How Decryption Works (Understanding Shift Values)

The English alphabet contains 26 letters. In this implementation, decrypting relies on finding the complementary shift value to complete a full 26-character cycle using the following logic:

Decryption Shift = 26 - Encryption Shift

Example:

1. Encryption Phase:  
   If a message is encrypted using a shift value of 7, each letter advances 7 positions forward in the alphabet.  
2. Decryption Phase:  
   To restore the original message, you must provide a shift value of 19 (calculated as 26 minus 7 equals 19). Shifting forward by 19 additional positions completes the 26-letter rotation, returning every character back to its starting position.

Additional Examples:

* Encryption Shift of 5 requires a Decryption Shift of 21 (26 - 5 = 21).  
* Encryption Shift of 7 requires a Decryption Shift of 19 (26 - 7 = 19).  
* Encryption Shift of 10 requires a Decryption Shift of 16 (26 - 10 = 16).

How to Run

1. Ensure Python 3.x is installed on your computer.  
2. Open your terminal or command prompt.  
3. Run the script using the following command:

python Caesar_cipher.py

4. Follow the on-screen prompts to enter your encrypted text and the complementary shift value.

Built for UTM students!