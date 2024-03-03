
# random library
from random import *
random()
round(random(),4)
int(random()*20) # int == floor
int(random()*10+1) # 1~ 10 이하의 임의의 값을 생성
randrange(1,46)
randint(1,45)

# rand example
mon=3
print(str(mon)+ '월 오프라인 스터디 모임 날짜는 ' + str(randint(4,28)) + '일로 선정되었습니다.')

sentence='나는 소년입니다'; print(sentence)
sentence2="나는 소년입니다"; print(sentence2)
sentence3="""
나는 소년이고,
파이썬은 쉬워요
"""; print (sentence3)

# slicing
jumin="940423-1234567"
print("성별: " + jumin[7])
print("연: "+jumin[0:2]) # 0부터 2 직전까지 (=0부터 1까지)
print('월: '+ jumin[2:4])
print('일: '+jumin[4:6])
print('생년월일: '+jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리: '+jumin[7:])
print('뒤 7자리 (뒤에서부터)'+jumin[4:-2]) # 4번째 자리부터, 맨 뒤에서 2번째 자리 직전까지

# 문자열 처리
python1 = "Python is Amazing"
print(python1.lower())
print(python1.upper())
python1[0].isupper()
len(python1)
print(python1.replace('Python','Java').upper())

index=python1.index('n'); index
index=python1.index('n',6); index
print(python1.find('n'))
print(python1.find('Java'))
python1.index('on')
python1.count('n')

# 문자열 포맷
print('1'+'b')
print('a','b')
print('나는 %d살입니다.' % 20)
print('나는 %sdfd를 좋아해요.' % '파이썬')
print('Apple은 %c로 시작해요' % 'A')
print('I am %s years old.' % 20)
print(' I like %s and %s' % ('red','blue'))

print('I am {} years old'.format(20))
print('I like {1} and {0}'.format('blue','red'))

print('I am {age} years old, and I like {color}.'.format(age=20,color='red'))

age=20; color='red'
print(f'I am {age} years old, and I like {color}.')

# 탈출 문자
print('백문이 불여일견,\n 백견이 불여일타')
print("My name is \"Jaemin\". ")
print("\\은 어떻게 쓰일까요?")
print("Red apple \rPine") # 커서를 맨 앞으로
print("Redd\bApple") # 백스페이스
print('Red \tapple') # 탭