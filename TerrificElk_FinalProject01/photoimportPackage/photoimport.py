# photoimport/photo.py
# Name: Ben Ujvagi, Jacob Shultze, Danny Barnhouse, Dobry Shaw
# email:  ujvagibw@mail.uc.edu, schul2jt@mail.uc.edu, barnhodw@mail.uc.edu, shawdp@mail.uc.edu
# Assignment Number: Final Project
# Due Date:  12/10/2024
# Course #/Section:  IS4010-001
# Semester/Year:  Fall 2024
# Brief Description of the assignment: decrypt two different codes and take a picture at the location
# Brief Description of what this module does. In this module, we call everything together and print it out
# Citations: Microsoft Copilot

from PIL import Image
import matplotlib.pyplot as plt

def display_photo(photo_path):
    """
    Adds photo from data folder
    """
    img = Image.open(photo_path)
    plt.imshow(img)
    plt.axis('off')  # Hide the axes
    plt.show()
