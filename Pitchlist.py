import aubio
import numpy as num
import pyaudio
import sys
from music21 import *

#Constants for the file
BUFFER_SIZE = 2048
CHANNELS = 1
FORMAT = pyaudio.paFloat32
METHOD = "default"
SAMPLE_RATE = 44100
HOP_SIZE = BUFFER_SIZE // 2
PERIOD_SIZE_IN_FRAME = HOP_SIZE
run = 1
PitchList = {}

# Initiating PyAudio
pA = pyaudio.PyAudio()
# Open the microphone
mic = pA.open(format=FORMAT, channels=CHANNELS,
              rate=SAMPLE_RATE, input=True,
              frames_per_buffer=PERIOD_SIZE_IN_FRAME)

# Initiating Aubio's pitch detection object.
pDetection = aubio.pitch(METHOD, BUFFER_SIZE,
                         HOP_SIZE, SAMPLE_RATE)
# Set unit.
pDetection.set_unit("Hz")
# Frequency under -40 dB will considered as silence
pDetection.set_silence(-40)
#loop

def square(x):
    y = x * x
    return y

def pitchfind():
    run = 0
    while True:
        try:
            secin = int(input("How long do you want to recorde for?"))
        except ValueError:
            print("Please enter a whole number")
            continue
        else:
            sec = secin * 44
            break
    for x in range(sec):
        run = run + 1
        # Always listening to the microphone.
        data = mic.read(PERIOD_SIZE_IN_FRAME)
        # Convert into number that Aubio understand.
        samples = num.fromstring(data,
                                 dtype=aubio.float_type)
        # Finally get the pitch.
        pitch = pDetection(samples)[0]

        #print the pitch
        print("Pitch" + str(run) + " = " + str(pitch))
        PitchList["pitch " + str(run) + " ="] = pitch
    return PitchList
