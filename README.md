# Cracking-Vigenere-Cipher
python code used to decrypt the vigenere cipher with kerchoffs method 

In this method(Kerchoff), we decrypt the vigenere cipher without knowing the actual key

This code finds the top 6 possible key lengths and find the key for only first 4 key lengths

# Code-working conditions
cipher text should be alphabets only. It won't work with symbols.

Given cipher text length should be larger. so that there will maximum probability for finding correct key

# Assumptions
Key length will be between 1 to 30 letters. 

But you can increase the value to your requirments by changing the value("30") code in line 16 [while k<30:]
