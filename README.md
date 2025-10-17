1. Caesar Cipher 

Hvs Eiwqy Pfckb Tcl Xiadg Cjsf Hvs Zonm Rcu.

Perform Frequency Analysis or a Brute-force attack to decrypt the ciphertext.
Provide the Python code solution and include the link to your GitHub repository.

Using a simple Python script that tests all 26 possible shifts, the decrypted message was:

The Quick Brown Fox Jumps Over The Lazy Dog.

The Caesar cipher is a monoalphabetic substitution cipher with only 25 possible keys.
It is not secure, since anyone can decrypt it by brute force or frequency analysis.
However, similar weak encryption is still used in legacy systems and simple data obfuscation, such as encoding serial numbers, basic puzzles, or toy applications.

2. XOR Encryption / Decryption 

Ciphertext:

mznxpz


Using the same Python brute-force logic, shift 21 gives:

rescue

Step 2: Solve the Anagram

rescue

When rearranged (anagram), it becomes:

secure — a fundamental concept in cryptography.

Step 3: XOR Decryption

Given Ciphertext (Base64):

Jw0KBlIMAEUXHRdFKyoxVRENEgkPEBwCFkQ=


XOR-decrypt the decoded bytes using the passphrase recovered from Step 2 (secure).

After decoding and XOR decryption, the final plaintext is:

This is the XOR challenge!


The Caesar cipher illustrates early symmetric encryption but is trivial to break.

XOR encryption, when combined with a strong, truly random key (one-time pad), can achieve perfect secrecy.

In this lab, these methods were used to explore core cryptographic principles: encoding, key usage, and the relationship between encryption and decryption.
