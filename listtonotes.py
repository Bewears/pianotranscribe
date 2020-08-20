"""
This file consists of the 'printsheet' function. The Purpose   of this function in my code is to take the
list of pitches and transferee them in to a type of data that the music 21 add on can understand. After
this has been completed the function will then transform the data in to sheet music and open this as
an .xml file.
"""

# imported libraries
from music21 import *

# Here the constants for the file are set. The only constant needed is the scale that the notation will be written in.
chrome = scale.ChromaticScale('C4')


def printsheet(x):
    detectedpitchesfreq = audioSearch.detectPitchFrequencies(x, useScale=chrome)
    detectedpitchesfreq = audioSearch.smoothFrequencies(detectedpitchesfreq, smoothLevels=4)
    (detectedPitches, listPlot) = audioSearch.pitchFrequenciesToObjects(
        detectedpitchesfreq, useScale=chrome)
    # Next the program joins identical pitches in order to calculate an accurate length.
    (notesList, durationList) = audioSearch.joinConsecutiveIdenticalPitches(detectedPitches)
    # It then combines the list of notes and the list of durations in to a single 'stream' called stream1
    stream1, lengthPart = audioSearch.notesAndDurationsToStream(notesList, durationList)
    # This stream is then finally opened by the program.
    stream1.show()
