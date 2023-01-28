### 스타크래프트를 텍스트 기반으로 게임하는 것처럼 만든다.
from random import *

class Unit:
    def __init__(self, name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print('{0} 유닛이 생성되었습니다.'.format(self.name))

    def move(self,location):

        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

    def damaged(self, damaged): # 일반 유닛도 공격을 받을 수 있기 때문에 이 쪽으로 이동
        print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
        self.hp -= damaged
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 유닛이 파괴되었습니다.'.format(self.name))

class AttackUnit(Unit):
    def __init__(self, name,hp,speed,damage):

        Unit.__init__(self,name,hp,speed)

        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))

class marine(AttackUnit): # 마린 유닛을 직접 정의
    def __init__(self):
        AttackUnit.__init__(self,'마린', 40, 1, 5)

    def stimpack(self): # 마린 유닛의 버프
        if self.hp > 10:
            self.hp -= 10
            print('{0} : 스팀팩을 사용합니다. (HP 10 감소)'.format(self.name))

        else:
            print('{0} : 스팀팩을 사용하지 않았습니다. '.format(self.name))

class Tank(AttackUnit):
    seize_mode_dev = False # 시즈 모드 개발여부

    def __init__(self):
        AttackUnit.__init__(self,'탱크', 150, 1, 35)
        self.seize_mode = False
    def set_seize_mode(self):
        if Tank.seize_mode_dev == False:
            return # 시즈모드가 개발이 안되있으면 그냥 나감

        # 현재 시즈 모드가 아닐 때 -> 시즈모드
        if self.seize_mode == False:
            print('{0} : 시즈모드로 전환 합니다.'.format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 현재 시즈모드일 경우에는 시즈모드를 해제를 한다.
        else:
            print('{0} : 시즈모드를 해제 합니다.'.format(self.name))
            self.damage /= 2
            self.seize_mode = False


class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self,name, location):
        print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location,self.flying_speed))

class Flyable_Attact_Unit(Flyable,AttackUnit):
    def __init__(self, name, hp, damage,flying_speed):
        AttackUnit.__init__(self, name, hp,0,damage)
        Flyable.__init__(self, flying_speed)

    def move(self,location):

        self.fly(self.name, location)

class Wraith(Flyable_Attact_Unit):
    def __init__(self):
        Flyable_Attact_Unit.__init__(self, '레이스', 80, 20, 5)
        self.clocked = False # 레이스의 클로킹 모드(해제 상태)

    def clocking(self):
        # 탱크와 비슷하게 하면 된다. 클로킹 모드일 때는 클로킹 모드를 해제하고 클로킹 모드가 아니면 클로킹 모드를 설정하면 됨.
        if self.clocked == True: # 클로킹 모드일 때 => 해제
            print('{0} : 클로킹 모드를 해제합니다.'.format(self.name))
            self.clocked = False

        else: # 클로킹 모드가 아닐 때 => 클로킹
            print('{0} : 클로킹 모드로 전환합니다.'.format(self.name))
            self.clocked = True


def game_start():
    print('[알림] 새로운 게임을 시작합니다.')

def game_over():
    print('player : "gg"')
    print('player가 게임에서 퇴장했습니다.')


# 게임 진행

game_start()

# 마린 3기 생성
m1 = marine()
m2 = marine()
m3 = marine()

# 탱크 2기 생성
t1 = Tank()
t2 = Tank()

# 레이스 1기 생성

w1 = Wraith()

# 유닛을 일괄적으로 관리(생성된 모든 유닛을 append 처리함)

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군이동

for unit in attack_units:
    unit.move('1시')

# 탱크 시즈모드 개발
Tank.seize_mode_dev = True
print('[알림] 탱크 시즈 모드 개발이 완료되었습니다.')

# 공격 모드 준비 (마린: 스팀팩 사용, 탱크 : 시즈모드, 레이스 : 클로킹)
for unit in attack_units:
# 지금 만들어진 객체가 어떤 클래스의 인스턴스인지 확인하는 것
# 지금 attack_units는 서로 다른 클래스에 있는 것들을 넣어주었는데, 이 객체가 어떤 클래스의 인스턴스인지 확인해서 처리해주는 것이 필요하므로 이것을 적음
    if isinstance(unit, marine):
        unit.stimpack() # 지금 이 유닛이 marine class의 객체이면 스팀팩을 사용해라
    elif isinstance(unit, Tank):
        unit.set_seize_mode() # 지금 이 유닛이 Tank class의 객체이면 시즈모드를 해라

    elif isinstance(unit, Wraith):
        unit.clocking()

# 전군 공격
for unit in attack_units:
    unit.attack('1시')

# 전군 피해
for unit in attack_units:
    unit.damaged(randint(5,20)) # 5부터 20까지 공격을 랜덤으로 받음.

# 게임종료

game_over()
