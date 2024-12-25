from random import *
def main():
    length = randint(5, 10)
    x = [0]*length
    print ('Length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print (x[i], end = ' ')
    print()

main()
