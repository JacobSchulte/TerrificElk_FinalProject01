#main.py
# Name: Ben Ujvagi, Jacob Schulte, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. In this module, we call everything together and print it out
# Citations: Microsoft Copilot

def main():
    # File paths
    words_file_path = r'C:\Users\benja\Downloads\Final Project IS4010-001 Fall 2024-1-2 (1)\UCEnglish.txt'
    encrypted_numbers = ["7480", "28894", "8018", "42049", "46049", "7487", "18797", "28898", "10953", "31563", "28799", "10355", "2756", "23887", "30997", "42547", "5209", "42686", "14761", "38919"]

    # Encrypted movie title and key
    encrypted_movie_title = 'gAAAAABnJ6xXc8WnJ2DxuUMI3yz9g4ZaGNGUd6TPU96o-rmP1YfrxSq387RxZtyEt2Hc1WNWXcsUaz5oWJGd_W7Gs6wNXMoDG7bnwSawyeXVmuNEP88HlA8='
    key = b'WVRqW7wUIQ1mgbz5PAonHGJn-XknVdDV74L_RNFjU0o='

    # Read the words from the .txt file for the location decryption
    words = building_file_reader(words_file_path)

    # Decrypt the location
    location = building_decryptor(encrypted_numbers, words)
    print(f"Decrypted Location: {location}")

    # Decrypt the movie title
    movie_title = movie_decryptor(encrypted_movie_title, key)
    print(f"Decrypted Movie Title: {movie_title}")

    # Display the photo
    photo_module.display_photo(photo_path)

if __name__ == "__main__":
    main()