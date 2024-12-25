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
    sum = 0
    for i in range(length):
        sum += (x[i] - average) ** 2
    print (f'Variance: {sum/length}')
    print (f'Standard Deviation: {(sum/length) ** 0.5}')

main()
