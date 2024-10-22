from random import *
i=1
passed=0
failed=0
mid_total=0
final_total=0
sessional_total=0
overall_total=0
print (f'Roll No.\tMid\tFinal\tSessional\tTotal\tGrade')
while i<=30:
    mid=randint(0,35)
    final=randint(0,40)
    sessional=randint(0,25)
    total=mid+final+sessional
    grade=()
    if total>=85:
        grade='A'
    elif total>=80:
        grade='A-'
    elif total>=75:
        grade='B+'
    elif total>=70:
        grade='B'
    elif total>=65:
        grade='B-'
    elif total>=61:
        grade='C+'
    elif total>=58:
        grade='C'
    elif total>=55:
        grade='C-'
    elif total>=50:
        grade='D'
    else:
        grade='F'
    if total>=50:
        passed=passed+1
    else:
        failed=failed+1
    mid_total=mid_total+mid
    final_total=final_total+final
    sessional_total=sessional_total+sessional
    overall_total=overall_total+total
    i=i+1
    print (f'{i}\t\t{mid}\t{final}\t{sessional}\t\t{total}\t{grade}')
print (f'Total: {i}')
print (f'Pass: {passed}')
print (f'Fail: {failed}')
print (f'Overall Average Marks: {overall_total/i}')
print (f'Average Midterm Marks: {mid_total/i}')
print (f'Average Sessional Marks: {sessional_total/i}')
