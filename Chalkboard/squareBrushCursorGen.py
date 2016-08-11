import math

def gen(size):
    eights = int(size/8) + 1

    padding = ((eights * 8) - size)/2

    brush = []

    b = ""

    for i in range(0, padding):
        for ii in range(0, eights * 8):
            b += ' '
        brush.append(b)
        b = ""

    for i in range(0,padding):
        b += ' '

    for i in range(0,size):
        b += 'X'

    for i in range(0,padding):
        b += ' '

    brush.append(b)
    b = ""

    for i in range(0, size-1):
        for ii in range(0,padding):
            b += ' '
        b += 'X'
        for ii in range(1,size-1):
            b += ' '
        b += 'X'
        for ii in range(0,padding):
            b += ' '
        brush.append(b)
        b = ""

    for i in range(0, padding):
        b += ' '

    for i in range(0,size):
        b += 'X'

    for i in range(0, padding):
        b += ' '
        
    brush.append(b)
    b = ""

    for i in range(0, padding):
        for ii in range(0, eights * 8):
            b += ' '
        brush.append(b)

    return tuple(brush)

    
