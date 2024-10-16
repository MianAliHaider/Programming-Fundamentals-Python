seconds=int(input('Enter the number seconds:'))
hours=seconds//3600
print('Number of Hours:',hours)
remaining_seconds=seconds%3600
minutes=remaining_seconds//60
print('Number of Minutes:',minutes)
print('Number of Seconds:',remaining_seconds%60)
