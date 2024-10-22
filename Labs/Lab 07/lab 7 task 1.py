import random
i=1
cout=0
add=0
sub=0
mul=0
while i<=10:
    choice=random.randint(1,3)
    if choice==1:
        a1=random.randint(0,99)
        a2=random.randint(0,99)
        print('N1= ',a1 , 'N2= ',a2)
        add=a1+a2
        print(add)
        add=add
    elif choice==2:
        s1=random.randint(10,99)
        s2=random.randint(10,99)
        print('N1=',s1 , 'N2=',s2)
        sub=s1-s2
        print(sub)
        sub=sub
    elif choice==3:
        m1=random.randint(0,9)
        m2=random.randint(0,9)
        print('N1=',m1 , 'N2=',m2)
        mul=m1*m2
        print(mul)
        mul=mul
    x=int(input('Enter Addition: '))
    if x==add :
        
        print('correct')
        cout=cout+1
    else:
        print('Incorrect')
    y=int(input('Enter Subtraction: '))
    if y==sub:
         
         print('correct')
         cout=cout+1
    else:
        print('Incorrect')
    z=int(input('Enter Multiplication: '))
    if z==mul :
        
        print('correct')
        cout=cout+1
    else:
        print('Incorrect')
    
    i=i+1
Score=cout
print('score=',Score)
        
        
        
        
    
        
