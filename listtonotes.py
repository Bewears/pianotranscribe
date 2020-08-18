'''


'''

from music21 import *

chrome = scale.ChromaticScale('C4')

def printsheet(x):
    detectedPitchesFreq = audioSearch.detectPitchFrequencies(x, useScale=chrome)
    detectedPitchesFreq = audioSearch.smoothFrequencies(detectedPitchesFreq, smoothLevels=4)
    (detectedPitches, listPlot) = audioSearch.pitchFrequenciesToObjects(
        detectedPitchesFreq, useScale=chrome)
    print(len(detectedPitches))
    (notesList, durationList) = audioSearch.joinConsecutiveIdenticalPitches(detectedPitches)
    s, lengthPart = audioSearch.notesAndDurationsToStream(notesList, durationList)
    s.show()
