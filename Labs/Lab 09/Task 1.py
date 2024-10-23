rows=int(input('Enter Rows:'))
character=65
for i in range (rows):
    for j in range(1,rows+1):
        print(chr(character),end=' ')
        for k in range (1,j+1):
            print(k,end=' ')
        character=character+1
    print()
