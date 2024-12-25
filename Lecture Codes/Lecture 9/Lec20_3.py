from random import *
def main():
    x = [0]*10
    print ('Length: ', len(x))
    for i in range(len(x)):
        x[i] = randint(10, 99)
        print (x[i], end = ' ')
    print()

main()
