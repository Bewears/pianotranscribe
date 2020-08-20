"""
This project is used for the purpose of transcribing live music in to a sheet music format. The is the main file
that is the culmination of three main components. These components are a recording component to record and store
audio input, a component that filter out all of the silence from the recorded input and a component to transform
this input data in to sheet music.
"""

from Pitchlist import *
from Removezero import *
from listtonotes import *

# This program starts off with an introduction, which explains
print("Welcome to music buddy!")
print("This program was created to take your live musical input and transform it in to sheet music.")
print("To run this program you will need to install a program capable of running xml files. "
      "Musescore is an easy one to set up")
input("Please press enter when you have installed it.")

# The program then asks the user for permission to access their microphone.
micuse = str.lower(input("For this program to work, it has to access your microphone. Are you okay with this?"))
# This while loop is used to validate the users input and ask again if it is invalid.
while True:
    if micuse == "yes":
        break
    elif micuse == "no":
        print("Very well, have a good day!")
        exit()
    else:
        micuse = str.lower(input("Please enter yes or no:"))

''' From this point is the main part of the program. This consists with in a while loop which 
allows users to record as many times as they please without having to restart.'''

while True:
    # The function pitchfind is called as the variable PitchDict.
    # This results in the recorded input being placed directly in to a variable.
    PitchDict = pitchfind()
    # Next this diction ary is transformed in to a list variable.
    pl = list(PitchDict.values())
    # This list is then run through the delzero function which removes any value that is 0.0
    delzero(pl)
    # The program then splits in to an If statement based on how many pitches were recorded.
    if len(pl) > 10:
        # If there were enough to turn in to sheet music, the data is then passed through the printsheet function.
        # This function takes the list of pitches and changes it in to sheet music which is then opened as an xml file.
        printsheet(pl)
        # The user is then asked if they would like to run the program again
        print("Thank you for using music buddy! You can now save your work through Musescore.")
        redo = str.lower(input("Would you like to record again?"))
        # User input validation
        b = 1
        while b == 1:
            if redo == "yes":
                b = 2
                continue
            elif redo == "no":
                print("Very well, see you again soon!")
                exit()
            else:
                redo = str.lower(input("Please enter yes or no:"))
    else:
        # If there was not enough pitches to print, the user is asked if they want to run it again or exit the program.
        print("There is not enough data in your recording to write down.")
        novalue = str.lower(input("Would you like to re-record?"))
        # User input validation
        a = 1
        while a == 1:
            if novalue == "yes":
                a = 2
                continue
            elif novalue == "no":
                print("Very well, have a good day!")
                exit()
            else:
                novalue = str.lower(input("Please enter yes or no:"))
