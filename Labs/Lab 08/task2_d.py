rows=int(input('Enter Rows:'))
columns=int(input('Enter Columns:'))
i=1
while i<=rows:
    j=1
    while j<=columns:
        print('*',end=' ')
        j=j+1
    i=i+1
    print('>')
