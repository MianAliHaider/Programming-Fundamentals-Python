from random import *
def main():
    a = chr(randint(0, 255))
    a = ord(a)  #get ascii value of character
    print (a)
    i = 1
    mask = 1
    while i <= 8:
        if (a & mask) == 0:
            print (f' Bit {i} is off')
        else:
            print (f' Bit {i} is on')
        i = i + 1
        mask = mask * 2

main()
