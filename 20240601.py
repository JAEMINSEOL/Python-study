#%%
score_file = open('score.txt','w',encoding='utf8')
print('수학: 0', file=score_file)
print('영어: 50', file= score_file)
score_file.close()

#%%
score_file = open('score.txt','a',encoding='utf8')
score_file.write('과학 : 80')
score_file.write('\n코딩: 100')
score_file.close()

#%%
score_file = open('score.txt','r',encoding='utf8')
print(score_file.read())
score_file.close()

#%%
score_file = open('score.txt','r',encoding='utf8')
print(score_file.readline(),end=' ')
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()
# %%
score_file = open('score.txt','r',encoding='utf8')
while True:
    line = score_file.readline()
    if not line:
        break
    print(line)
score_file.close()
# %%
score_file = open('score.txt','r',encoding='utf8')
lines = score_file.readlines() # 모든 line을 list 형태로 저장
# %% pickle
import pickle
profile_file = open('profile.pickle','wb')
profile = {'name':'Seol','age': 30, 'hobby':['soccer','coding','golf']}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정보를 실제 file에 저장
profile_file.close()

#%%
profile_file = open('profile.pickle','rb')
profile = pickle.load(profile_file)
profile_file.close()

#%% with_ close file이 필요가 없는 파일 I/O 구문
import pickle
with open('profile.pickle','rb') as profile_file:
    print(pickle.load(profile_file))
with open('study.txt','w',encoding='utf8') as study_file:
    study_file.write('I am studying Python hard')
#%%
with open('study.txt','r',encoding='utf8') as study_file:
    print(study_file.read())

#%% quiz
for day in range(1,51):
    with open(f'{day}주차.txt', 'a',encoding='utf8') as report_file:
        report_file.write(f'- {day} 주차 주간보고 -')
        report_file.write(f'\n부서 : \n이름 : \n업무 요약 : ')


#%% class
class Unit:
    def __init__(self,name,hp,atk):
        self.name = name
        self.hp = hp
        self.atk = atk
        print(f'** {name} unit is generated **\nMax hp: {hp}, ATK: {atk}')

marine1 = Unit('Marine',40,5)
marine2 = Unit('Marine',40,5)
tank1 = Unit('Siege Tank',150,35)
wraith1 = Unit('Wraith',80,5)

print(f'Unit name: {wraith1.name}, ATK: {wraith1.atk}')

wraith2 = Unit('Wraith',80,5)
wraith2.clocking = True

if wraith2.clocking==True:
    print(f'{wraith2.name} is in clocking state')

#%%
class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print(f'** {name} is generated **\nMax hp: {hp}')
    def damaged(self, damage):
        self.hp -= damage
        if self.hp<=0:
            self.hp =0
        print(f'{self.name}: took damage of {damage}. [HP remain: {self.hp}]')
        if self.hp<=0:
            print(f'{self.name} is destroyed')
    def move(self,location):
        print(f'{self.name}: moves to {location} direction. [speed: {self.speed}]')

class Flying:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name,location):
        print(f'{self.name}: flies to {location} direction. [speed: {self.flying_speed}]')

class Unit_Atk(Unit):
    def __init__(self,name,hp,atk,speed):
       Unit.__init__(self,name,hp,speed)
       self.atk = atk
       print(f'ATK: {atk}')
    def damaged(self, damage):
        Unit.damaged(self,damage)
    def attack(self, location):
         print(f'{self.name}: attack for {location} direction. [ATK: {self.atk}]')

class Unit_Atk_Fly(Unit_Atk, Flying):
    def __init__(self,name,hp,atk,flying_speed):
        Unit_Atk.__init__(self,name,hp,atk,0)
        Flying.__init__(self,flying_speed)
    def move(self, location):
        self.fly(self.name, location)

class Building(Unit):
    def __init__(self,name,hp,location):
        # Unit.__init__(self,name,hp,0)
        super().__init__(name,hp,0)
        self.location = location
#%%

marine1 = Unit_Atk('Marine',40,5,10)
marine2 = Unit_Atk('Marine',40,5,10)
tank1 = Unit_Atk('Siege Tank',150,35,15)
wraith1 = Unit_Atk_Fly('Wraith',80,5,24)
medic1 = Unit('Medic',40,10)
vulture1 = Unit_Atk('Vulture',80,10,20)
battlecruiser1 = Unit_Atk_Fly('BattleCruiser',500,25,3)
#%%
marine1.attack('NE')
marine1.damaged(11)
wraith1.move('SW')
vulture1.move('SS')


#%%