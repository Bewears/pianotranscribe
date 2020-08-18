'''
This project is used for the purpose of transcribing live music in to a sheet music format.

'''

from music21 import *
from Pitchlist import *
from Removezero import *
from listtonotes import *

PitchList = pitchfind()
print(PitchList)
pl = list(PitchList.values())
print(pl)
delzero(pl)
print(pl)
printsheet(pl)
