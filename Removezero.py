"""
This file consists of the 'delzero' function. This is a very light weight function with the sole purpose
of taking a list of values and removing any value from that list that is '0.0' or Silence. This is
important to the program as the music 21 add on does not accept silence and thus will break if you attempt
input any data with a the value '0.0' in it. Once the function has removed every value that it can, it will
return the new list as pl.
"""


def delzero(pl):
    # The program is told to run in a loop for as many items that there are on the list.
    for x in range(len(pl)):
        # The value of 0.0 is then removed.
        pl.remove(float(0.0))
        # If there is still a 0.0 in the list, the program will continue. If not it will break.
        if float(0.0) in pl:
            continue
        else:
            break
    # Once all have been removed, the function returns the list as pl.
    return pl
