rows=int(input('Enter Rows:'))
d=rows*2-2
for i in range (rows):
    for j in range (i):
        print(' ',end='')
    print('|_ ',end='')
    for j in range(d):
        print(' ',end='')
    if j<d:
        print('_|')
    else:
        print('|')
    d=d-2
