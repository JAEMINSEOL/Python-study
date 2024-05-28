#%%
weather = input('Weather?:')
if weather == 'rain':
    print('prepare umb.')
elif weather == 'dust':
    print('prepare mask')
else:
    print('go out w/o anything')



# %%
temp = int(input('temperature?: '))

if 30<=temp:
    print('too hot')
elif 10<=temp & temp<30:
    print('fine')
elif 0<=temp < 10:
    print('prepare coat')
else:
    print('too cold')
# %%
for i in (range(4)):
    print(f'num : {i}')
# %%
starbucks = ['Ironman','Thor','Groot']
for customer in starbucks:
    print(f'{customer}, your coffee is ready ')
# %%
# while
customer = 'Thor'
index=5
while index>=1:
    print(f'{customer}, your coffee is ready. {index} left')
    index -= 1
    if index==0:
        print('trash coffee')

# %%
customer = 'Ironman'
person='none'
index=1
while True:
    print(f'{customer}, your coffee is ready. {index} times calling')
    index +=1
    person = input("Customer? :")
    if person == customer:
        break

#%%
absent=  [2,5]
no_book = [7]
for student in range(1,11):
    if student in absent:
        print(f'{student} is missing')
    elif student in no_book:
        print(f'class is over. {student}, come to the principal\'s office')
        break
# %%
students=[1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

#%%
students = ['Iron man','Thor','Groot']
# students = [len(i) for i in students]
print(students)

students = [i.upper() for i in students]
print(students)


#%%
# quiz
from random import *

num=0
for i in range(1,51):
    time = randrange(5,51)
    if 5<=time<=15:
        allowed='O'; num+=1
    else:
        allowed=' '
    print(f'[{allowed}] {i} 번째 손님 (소요시간 : {time}분)')
print(f'총 탑승 승객 : {num}분')

# %%
