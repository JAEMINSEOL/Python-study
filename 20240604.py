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

class Unit_Atk(Unit):
    def __init__(self,name,hp,atk,speed):
       Unit.__init__(self,name,hp,speed)
       self.atk = atk
       print(f'ATK: {atk}')

    def attack(self, location):
         print(f'{self.name}: attack for {location} direction. [ATK: {self.atk}]')

class Flying:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    def fly(self,name,location):
        print(f'{self.name}: flies to {location} direction. [speed: {self.flying_speed}]')


class Unit_Atk_Fly(Unit_Atk, Flying):
    def __init__(self,name,hp,atk,flying_speed):
        Unit_Atk.__init__(self,name,hp,atk,0)
        Flying.__init__(self,flying_speed)
    def move(self, location):
        self.fly(self.name, location)

class Marine(Unit_Atk):
    def __init__(self):
        Unit_Atk.__init__(self,'Marine',40,5,1)
    def stimpack(self):
        if self.hp>10:
            self.hp -=10
            print(f'{self.name} uses stimpack (HP -10)')
        else:
            print(f'{self.name} has not enough HP to use stimpack')

class SiegeTank(Unit_Atk):
    siege_dev = False
    def __init__(self):
        Unit_Atk.__init__(self,'SiegeTank',150,35,1)
        self.is_siege=False
    def siege_mode(self):
        if ~SiegeTank.siege_dev:
            return
        if ~self.is_siege:
            print(f'{self.name} goes to siege mode')
            self.atk = 300
            self.is_siege = True
        else:
            print(f'{self.name} goes to tank mode')
            self.atk = 150
            self.is_siege = False

class Wraith(Unit_Atk_Fly):
    def __init__(self):
        Unit_Atk_Fly.__init__(self,'Wraith',80,5,20)
        self.is_clocked = False

    def clocking(self):
        if self.is_clocked == False:
            print(f'{self.name} goes to clock mode')
            self.is_clocked = True
        else:
            print(f'{self.name} goes to visible mode')
            self.is_clocked = False
def game_start():
    print('New game start')
def game_over():
    print('gg \n player left. game over')

#%%
from random import *

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = SiegeTank()
t2 = SiegeTank()

w1 = Wraith()

attack_units = []
attack_units = [m1,m2,m3,t1,t2,w1]

for unit in attack_units:
    unit.move('NW')

SiegeTank.siege_dev = True
print('Siege development complete')

for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit,SiegeTank):
        unit.siege_mode()
    elif isinstance(unit,Wraith):
        unit.clocking()

for unit in attack_units:
    unit.attack('WW')

for unit in attack_units:
    unit.damaged(randint(5,21))
    unit.damaged(randint(5,21))
    unit.damaged(randint(5,21))
    unit.damaged(randint(5,21))

game_over()

#%% quiz

class real_estate:
    def __init__(self,location,house_type,deal_type, price, construct_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.construct_year = construct_year
    def show_detail(self):
        print(f'{self.location} {self.house_type} {self.deal_type} {self.price} {(self.construct_year)}년')

h1 = real_estate('강남','아파트','매매','10억',2010)
h2 = real_estate('마포','오피스텔','전세','5억',2007)
h3 = real_estate('송파','빌라','월세','500/50',2000)
house_list = [h1,h2,h3]

print(f'총 {len(house_list)}대의 매물이 있습니다.')
for house in house_list:
    house.show_detail()

#%%
