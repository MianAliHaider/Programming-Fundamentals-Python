from random import *
def main():
    a = randint(201, 15000)
    print (a)
    mask = 1
    i = 1
    while mask <= a:
        if (a & mask) == 0:
            print (f' Bit {i} is off')
        else:
            print (f' Bit {i} is on')
        mask = mask * 2
        i = i + 1

main()
