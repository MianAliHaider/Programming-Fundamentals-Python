from random import *
def main():
    length = randint(5, 10)
    x = [0]*length
    print ('Length: ', length)
    sum = 0
    for i in range(length):
        x[i] = randint(10, 99)
        print (x[i], end = ' ')
        sum += x[i]
    average = sum / length
    print(f'\nAverage: {average:.2f}')
    for i in range(length):
        if x[i] > average:
            print (f'{x[i]} is greater than average')
        else:
            print (f'{x[i]} is less than equal average')

main()
