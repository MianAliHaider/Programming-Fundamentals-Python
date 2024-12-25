from random import *
def main():
    s = ''
    a = randint(1, 1500)
    print (a)
    while a > 0:
        s = str(a%2) + s
        a = a // 2
    print(s)

main()
