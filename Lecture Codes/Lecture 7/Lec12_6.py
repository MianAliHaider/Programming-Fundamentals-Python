from random import *
def main():
    n = 0
    a = randint(0, 15000)
    print ('Decimal Number: ', a)
    i = 1
    while a > 0:
        r = a % 2
        if r == 1:
            n = i + n
        a = a // 2
        i = i * 10
    print ('Binary Number: ', n)

main()
