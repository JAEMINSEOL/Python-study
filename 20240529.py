#%%
def profile(name, age, lan1, lan2, lan3, lan4, lan5):
    print(f'name :{name}\tage : {age}\t', end=' ') #end=''은 print 후 줄바꿈을 생략하는 방법
    print(lan1, lan2, lan3, lan4, lan5)
# %%
profile('설재민',20,'Python','Java', 'C','C++','Matlab')
# %%
def profile_var(name, age, *language):
     print(f'name :{name}\tage : {age}\t', end=' ')
     for lang in language:
          print(lang, end=' ')
     print()

profile_var('설재민',30,'Matlab','Python')
# %%
gun = 10

def checkpoint(soldiers):
     global gun # 전역 공간에 있는 gun 변수 사용
     gun = gun - soldiers
     print(f'[함수 내] 남은 총: {gun}')

def checkpoint_ret(gun, soldiers):
     gun = gun - soldiers
     print(f'[함수 내] 남은 총: {gun}')
     return gun


print(f'전체 총: {gun}')
checkpoint(2)
gun=checkpoint_ret(gun,2)
print(f'남은 총: {gun}')
# %% quiz
def std_weight(height, gender):
     if height>3:
          height /= 100
     if gender=='남자':
          c_weight=22
     elif gender=='여자':
          c_weight=21
     std_w =  height**2 * c_weight
     print(f'키 {round(height*100)}cm {gender}의 표준 체중은 {round(std_w,2)}kg 입니다.')
     # return std_w

std_weight(165,'남자')

#%%
import sys
print('Python','Java',sep=' vs. ', end='?')
print('Python','Java',file=sys.stdout)
print('Python','Java',file=sys.stderr)
# %%
scores = {'Math' : 0, 'English':40, 'Coding': 30, 'Science':50}
for subject, score in scores.items():
     # print(f'{subject} 점수는 {score} 입니다.'.ljust(8))
     print(subject.ljust(8), str(score).rjust(4), sep=':')
# %%
for num in range(1,21):
     print('대기번호 : ' + str(num).zfill(3))
# %%
answer = input('아무값이나 입력하세요:')
print(type(answer))
print(f'입력하신 값은 {answer} 입니다.')
# %%
#1. 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0: >10}'.format(500))
#2. 양수일 때는 +, 음수일 때는 -로 표시
print(('{0: >+10}'.format(-100)))
#3. 왼쪽 정렬하고, 빈칸은 _로 채우기
print('{0:_<+10}'.format(300))
#4. 3자리마다 콤마를 찍고, +- 부호 붙이기
print('{0:+,}'.format(340000002))
#5. 3자리 콤마, 부호, 빈 공간에 *
print('{0:*>+30,}'.format(3000402))
#6. 소수점 출력
print('{0:.3f}'.format(23/7))
# %%
