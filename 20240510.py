from math import *
from random import *
print(randint(1,3))

sentence = 'I am a boy'
print(sentence)
sentence2 = 'python is easy'
print(sentence2)
sentence3 = '''
i am a boy, and
python is easy
'''
print(sentence3)

jumin='940423-1234567'
print(jumin[3])
print('gender = '+jumin[7])
print('year=' +jumin[0:2])
print('month='+str(int(jumin[2:4])))
print('생년월일: ' + jumin[:6]) # 처음부터 6 직전까지
print('뒤 7자리 :' + jumin[7:]) # 7부터 끝까지
print('뒤 7자리 (뒤에서부터): ' + jumin[-7:]) # 맨 뒤에서 7번째부터, 끝까지
