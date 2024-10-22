rows=int(input('Enter Rows:'))
i=1
while i<=rows:
    j=1
    count=0
    while j<=i+4:
        count=count+j
        print(j,end=' ')
        j=j+1
    print(' = '+str(count),end='')
    print()
    i=i+1
