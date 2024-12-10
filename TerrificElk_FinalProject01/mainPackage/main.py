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

from buildingdecryptorPackage.buildingdecryptor import read_words as building_file_reader
from buildingdecryptorPackage.buildingdecryptor import decrypt_location as building_decryptor
from moviedecryptorPackage.moviedecryptor import decrypt_message_fernet as movie_decryptor
from photoimportPackage.photoimport import display_photo as photo_module
from JSONreaderPackage.JSONreader import JSONReader

def main():

    # Read JSON files using JSONReader
    hints_reader = JSONReader("./data/EncryptedGroupHints Fall 2024 Section 001.json")
    hints_data = hints_reader.load_data()

    messages_reader = JSONReader("./data/TeamsAndEncryptedMessagesForDistribution.json")
    messages_data = messages_reader.load_data()


    # Use the encrypted_message for further processing
    # File paths
    words_file_path = r'data\UCEnglish.txt'
    encrypted_numbers = ["7480", "28894", "8018", "42049", "46049", "7487", "18797", "28898", "10953", "31563", "28799", "10355", "2756", "23887", "30997", "42547", "5209", "42686", "14761", "38919"]

    # Encrypted movie title and key
    # We used CompleteDuck's key because Bill was at a football game
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
    photo_module('data\FinalProjectImage.jpeg')

if __name__ == "__main__":
    main()