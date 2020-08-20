"""
This file consists of the 'pitchfind' function. This function is an important part to the program
as it is responsible for recording audio from the users microphone and then storing this data
in the form of a dictionary for easy access later. The program works by first asking the
user for how many seconds they would like to record for. This input is then multiplied
in to an approximate amount of runs that the function can go through every second (44 ish)
to determine the amount of times the function will run. After this is done the program will begin to run.
The processes consists of the microphone recording what ever pitch it hears, and then inputting it
in to a dictionary. The dictionary consists of the key 'PitchX' (where x is equal to the number of runs
the program has been through), and the value of the pitch in Hz. Once the program has run for the specified
amount of time, it will return the pitches.
"""

import aubio
import numpy as num
import pyaudio

# Constraints for the file
bsize = 2048
channel = 1
form = pyaudio.paFloat32
method = "default"
srate = 44100
hopsize = 1024
psize = hopsize
run = 0
PitchDict = {}
pA = pyaudio.PyAudio()

# In this code the program opens the mic using the constraints.
mic = pA.open(format=form, channels=channel,
              rate=srate, input=True,
              frames_per_buffer=psize)
pDetection = aubio.pitch(method, bsize,
                         hopsize, srate)
# Here te unit and constraint for silence is set.
pDetection.set_unit("Hz")
pDetection.set_silence(-40)


# The function then begins
def pitchfind():
    # This function starts with asking the user for the amount of time to record
    c = 1
    while True:
        run = 0
        while c == 1:
            try:
                secin = int(input("How long do you want to record for in seconds?"))
            # It then validates their response
            except ValueError:
                print("Please enter a whole number")
                continue
            else:
                c = 2
                if secin < 1:
                    print("Please enter a number between 1 and 1000")
                    c = 1
                elif secin > 1000:
                    print("Please enter a number between 1 and 1000")
                    c = 1
                else:
                    sec = secin * 44
                    continue
        break

    # It then takes their input and runs the loop for how many seconds they specified.
    for x in range(sec):
        run = run + 1
        data = mic.read(psize)
        # Convert into number that Aubio understand.
        samples = num.fromstring(data,
                                 dtype=aubio.float_type)
        # It now puts the pitch in to a variable.
        pitch = pDetection(samples)[0]
        # This code prints the variable to show the user that there is something happening.
        print("Pitch" + str(run) + " = " + str(pitch))
        # Finally it is added to a dictionary of pitches.
        PitchDict["pitch " + str(run) + " ="] = pitch
    # After it has reached the end it returns the dictionary.
    return PitchDict
