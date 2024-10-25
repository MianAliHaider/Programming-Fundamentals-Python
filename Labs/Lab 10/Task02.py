from random import*
x = [0]*10
y = [0]*10
z = [0]*10
sum = [0]*10
score = 0
for i in range(10):
    x[i] = randint(1,9)
for i in range(10):
    y[i] = randint(1,9)
for i in range(10):
    sum[i] = x[i] + y[i]
for i in range(10):
    number= int(input(f'{x[i]} + {y[i]} = '))
    z[i] = number
    if number==sum[i]:
        score = score+1
print('score',score,'/10')
print('Incorrect\t\tCorrect')
for i in range(10):
    if z[i] != sum[i]:
        print(x[i],' + ',y[i],' = ',z[i],'    ',x[i],' + ',y[i],'=',sum[i])
print('Correct')
for i in range(10):
    if z[i]==sum[i]:
        print(x[i],' + ',y[i],' = ',z[i])
        
