python = 'Python is Amazing'
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(python[1].islower())
print(len(python))
print(python.replace('Python','Java',2))

index = python.index('n')
print(index)
index = python.index('n',6)
index

print(python.find('Java'))
print(python.index('yt'))
print(python.count('n'))
print(python.replace('Python','Java').count('a'))

## 문자열 포맷

print('a'+'b')
print('a','b')
print('a','b'+'c')

print('나는 %d살 입니다.'%20 )
print('나는 %s을 좋아합니다.'%'Python')
str1 = '바나나우유'
print('%s(는)은 %c로 시작합니다.'%(str1, str1[0]))

print('나는 {}살 입니다.'.format(20))
print('나는 {}를 좋아합니다.'.format('파이썬'))
print('{}는 {}로 시작합니다.'.format(str1,str1[0]))
print('{0}은 {1}로 시작하고 {2}로 끝납니다.'.format(str1,str1[0],str1[-1]))

print('나는 {age}살이며, {food}를(을) 좋아합니다. {food}는(은) {fd1}(으)로 시작해요.'.format(food=str1,fd1=str1[0],age=20))

age=20; food = '사과'
print(f'나는 {age} 살이며, {food}를 좋아합니다')
