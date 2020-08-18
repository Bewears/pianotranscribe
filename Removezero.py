'''


'''


def delzero(pl):
    for x in range(len(pl)):
        pl.remove(float(0.0))
        print(pl)
        if float(0.0) in pl:
            print("ok")
            continue
        else:
            break
    return pl
