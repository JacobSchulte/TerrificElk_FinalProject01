#main.py
# Name: Ben Ujvagi, Jacob Shulte, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. Decrypts the building location
# Citations: Microsoft Copilot

# buildingdecryption.py

def read_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.readlines()
    return [word.strip() for word in words]

def decrypt_location(encrypted_numbers, words):
    decrypted_message = ' '.join(words[int(num)] for num in encrypted_numbers)
    return decrypted_message