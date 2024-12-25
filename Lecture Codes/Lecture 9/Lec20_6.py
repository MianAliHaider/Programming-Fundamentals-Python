from random import *
def main():
    length = randint(5, 10)
    x = [0]*length
    print ('Length: ', length)
    for i in range(length):
        x[i] = randint(10, 99)
        print (x[i], end = ' ')
        if i==0:            max = min = x[i];
        elif max < x[i]:    max = x[i];
        elif min > x[i]:    min = x[i];
    print(f'\nMax: {max}\t\tMin: {min}')
    for i in range(length):
        print (f'{x[i]} is {max-x[i]} less than max and {x[i]-min} more than min')
main()
