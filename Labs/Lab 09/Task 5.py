rows=int(input('Enter Rows:'))
columns=int(input('Enter Columns:'))
i=1
while i<=rows:
    j=1
    s=0
    n=1
    while  j<=columns:
        print(n,end='')
        if j<columns:
            print('+',end='')
        s=s+n
        n=n+i
        j=j+1
    print('=',s)
    i=i+1
