# moviedecryption/decryptor.py

# Name: Ben Ujvagi, Jacob Schulte, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. In this module we decrypt the code that tells us our movie
# Citations: Microsoft Copilot


from cryptography.fernet import Fernet

"""
Decrypts an encrypted message using Fernet encryption.

Args:
    encrypted_message (str): The encrypted message.
    key (bytes): The decryption key.

Returns:
    str: The decrypted message.
"""

def decrypt_message_fernet(encrypted_message, key):
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message.encode())
    return decrypted_message.decode()
