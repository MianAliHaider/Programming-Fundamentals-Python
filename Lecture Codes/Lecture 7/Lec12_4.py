from random import *
def main():
    a = randint(1, 1500)
    print (a)
    while a > 0:
        print (a%2, end = '')
        a = a // 2

main()
