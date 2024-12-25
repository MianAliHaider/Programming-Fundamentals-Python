def main():
    a = 65
    count = 0
    while a <= 90:
        print (chr(a), end = '')
        count = count + 1
        if count == 5:
            print()
            count = 0
        a = a + 1

main()
