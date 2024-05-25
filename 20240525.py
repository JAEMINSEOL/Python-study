cabinet = {3:'사과', 100:'바나나'}
cabinet[3]
print(cabinet.get(3))

print(cabinet.get(5))
print(cabinet.get(5,'사용 가능'))
print('hi')

print(3 in cabinet)

cabinet = {'A-3':'사과','ㅠ-4':'바나나'}
print('A-3' in cabinet)
cabinet['C-5'] = 'grape'

del cabinet['A-3']

print(cabinet.keys())
print(cabinet.values())
print(cabinet.items())
cabinet.clear()

print(cabinet.keys())

# tuple
menu = ('apple','banana')

print(menu[0])

name='banana'
price='3000'

name, price = 'banana', 20
print(name, price)

# set
my_set = {4,1,2,3,3,'apple','banana'}

print(my_set)

fruit = {'apple','banana','grape'}
red = set(['apple','blood'])

print(fruit & red)

print(fruit.intersection(red))

print(fruit | red)
print(fruit.union(red))

print(fruit - red)
print(fruit.difference(red))

fruit.add('tomato')
print(fruit)

fruit.remove('grape')
print(fruit)

# change
menu = {'coffee','milk','juice'}
print(menu, type(menu))

menu = list(menu)
print(menu,type(menu),menu[2])

menu = tuple(menu)

menu = set(menu)


# quiz
reply = list(range(1,21))

from random import *
shuffle(reply)
chicken = reply.pop()
coffee = sample(reply,3)

print(f'--당첨자 발표-- \n 치킨 당첨자: {chicken} \n 커피 당첨자: {coffee} \n --축하합니다--')
