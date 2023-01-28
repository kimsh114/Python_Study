## class는 보통 붕어빵틀에 비유를 한다. // 서로 연관이 있는 변수와 함수의 집합으로 생각을 하면 좋다.

# class Unit:
#     def __init__(self, name,hp,damage):
#         self.name = name # self가 없는 name => 위에서 전달받은 인자를 사용한다.// 맴버 변수 초기화라고 함.
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
# marine1 = Unit('마린', 40, 5) # marine1, marine2, marine3, tank 처럼 클래스를 통해서 만들어지는 부분들을 객체라고 표현한다.
# marine2 = Unit('마린', 40, 5)
# marine3 = Unit('마린', 40, 5)
# tank = Unit('탱크', 150, 40)

###-----------init-------------------------
## __init__는 파이썬에서 쓰이는 생성자이다.  //  클래스에 있는 함수를 호출할 때는 self를 제외하고 전달값에 맞춰서 호출해야한다.

###-----------맴버변수--------------------------
##  self.name , self.hp, self.damage  => 이것들을 맴버변수라고 한다.
## 맴버변수는 클래스 내부에서 정의된 변수고 그 변수를 가지고 우리가 초기화를 할 수 있고 실제로 사용도 가능하다.

# class Unit:
#     def __init__(self, name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
# wraith1 = Unit('레이스', 80,5)
# print('유닛 이름: {0}, 공격력: {1}'.format(wraith1.name, wraith1.hp, wraith1.damage))
# # wraith1.name, wraith1.hp, wraith1.damage => 이런 식으로 점을 통해서 class 내부에 접근을 할 수가 있다. 즉 맴버변수를 외부에서도 쓸 수 있다.
#
# wratih2 = Unit('마인드 컨트롤 된 레이스', 80, 5)
# wratih2.clocking = True
# # clocking 이라는 변수는 class 내부에는 존재하지 않지만 이런 식으로 외부에서 생성할 수 있다.
# # 이처럼 클래스 외부에서도 객체를 통해서 변수를 생성할 수 있다. 하지만 생성된 변수는 생성한 객체에만 사용이 가능하다.
# if wratih2.clocking == True:
#     print('{0}는 현재 클로킹 상태입니다.'.format(wratih2.name))



### -----------------------메소드-------------------------------

# class Unit: # 일반유닛
#     def __init__(self, name,hp,damage):
#         self.name = name # self가 없는 name => 위에서 전달받은 인자를 사용한다.
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
# class AttackUnit: # 공격 유닛 생성
#     def __init__(self, name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
#     def attack(self, location): # 공격하는 함수( attack 메소드)
#         print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))
#         # self.name, self.damage => 위의 init 함수에서 정의된 name과 damage를 사용하는 것이다
#         # location => attack 함수에서 전달받은 값을 사용하겠다.
#
#
#     def damaged(self, damaged): # 공격받은 함수 (damaged 메소드)
#         print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
#         self.hp -= damaged
#         print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 유닛이 파괴되었습니다.'.format(self.name))
#
#
# firebat1 =  AttackUnit('파이어벳', 50, 16)
# firebat1.attack('5시')
#
# # 공격을 두 번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(30)

###----------------상속---------------------
## 상속을 하는 클래스를 부모 클래스라고 하고 상속을 받는 쪽을 자식 클래스라고 한다. 여기서 부모는 Unit, 자식은 AttackUnit

# class Unit: # 방어 유닛 (스타크레프트의 메딕같은 유닛), 이 유닛들은 공격력이 없음.
#     def __init__(self, name,hp):
#         self.name = name
#         self.hp = hp
#
#
# class AttackUnit(Unit):  # AttackUnit class에 괄호로 방어 유닛 클래스인 Unit을 상속함.
#     def __init__(self, name,hp,damage):
#         # 방어 유닛 클래스의 def는 이런 식으로 AttactUnit 클래스에 상속이 가능함.
#         Unit.__init__(self,name,hp)
#         # 이때 AttackUnit은 self.name 과 self.hp는 이미 Unit클래스에 지정이 되어있어 그것을 상속받는 것이므로 전달값에만 적어주면 됨.
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))
#
#
#
#
#     def damaged(self, damaged):
#         print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
#         self.hp -= damaged
#         print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 유닛이 파괴되었습니다.'.format(self.name))
#
#
# firebat1 =  AttackUnit('파이어벳', 50, 16)
# firebat1.attack('5시')
#
#
# firebat1.damaged(25)
# firebat1.damaged(30)


###------------------다중상속----------------
## 부모 클래스를 두개 이상 상속받는 것이 다중상속이다.


# class Unit:
#     def __init__(self, name,hp):
#         self.name = name
#         self.hp = hp
#
#
# class AttackUnit(Unit):
#     def __init__(self, name,hp,damage):
#
#         Unit.__init__(self,name,hp)
#
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))
#
#
#
#     def damaged(self, damaged):
#         print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
#         self.hp -= damaged
#         print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 유닛이 파괴되었습니다.'.format(self.name))
#
# class Flyable: # 날 수 있는 기능을 가진 유닛들 공격기능은 없음. (ex. 옵저버 같은 유닛)
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name, location):
#         print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location,self.flying_speed))
#
# class Flyable_Attact_Unit(Flyable,AttackUnit): # 공중에서 공격하는 유닛// AttackUnit과 Flyable class를 다중 상속받아 초기화를 해주는 역할
# ## 여기서 중요한 것은 다중상속은 콤마로 한다는 것이다. 공중 공격 유닛은 날 수도 있어야 하고, 공격도 가능해야 하므로 Flyable,AttackUnit 두 개의 클라스를 전달함.
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp,damage) # 공격 유닛 클래스의 __init__ 함수에서 name과 hp, damage를 전달.
#         Flyable.__init__(self, flying_speed)
#
#
# valkyrie = Flyable_Attact_Unit('발키리', 200, 10, 10)
# valkyrie.fly(valkyrie.name, '3시')  # 여기서 fly는 Flyable class의 fly 이며, 여기는 name 변수가 없기 때문에 name을 만듦


###------------메소드 오버라이딩--------------------
## 부모클래스에서 정의한 메소드 말고 자식클래스에서 정의한 메소드를 쓰고 싶을 때 메소드를 새롭게 정의해서 사용할 수 있는데 이를 메소드 오버라이딩이라고 한다.

# class Unit:
#     def __init__(self, name,hp, speed): # 지상유닛의 스피드 추가
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#
#     def move(self,location):
#         print('[지상 유닛 이동]')
#         print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
#
# class AttackUnit(Unit):
#     def __init__(self, name,hp,speed,damage):
#
#         Unit.__init__(self,name,hp,speed)
#
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))
#
#
#
#     def damaged(self, damaged):
#         print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
#         self.hp -= damaged
#         print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 유닛이 파괴되었습니다.'.format(self.name))
#
# class Flyable: # 날 수 있는 기능을 가진 유닛들 공격기능은 없음. (ex. 옵저버 같은 유닛)
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name, location):
#         print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location,self.flying_speed))
#
# class Flyable_Attact_Unit(Flyable,AttackUnit): # 공중에서 공격하는 유닛
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp,0,damage) # 공중 유닛들의 스피드는 Flyable에 있기 때문에 지상 유닛의 스피드는 0 이라는 의미이다.
#         Flyable.__init__(self, flying_speed)
#
#     def move(self,location): # move 함수를 위의 지상 유닛과 더불어 공중 공격 유닛에서도 재정의 한 과정
#         print('[공중 유닛 이동]')
#         self.fly(self.name, location) # Flyable 클래스의 fly 함수를 받아서 날 수 있기 때문에 self.fly를 사용

# vulture = AttackUnit('벌쳐', 80,10,20)
#
# BattleCruiser = Flyable_Attact_Unit('배틀크루저', 500, 100, 3)
#
# vulture.move('11시')
# BattleCruiser.move('9시') # Fly_Attact_Unit 클래스의 move함수에는 self.name이 이미 있기 때문에 location만 정의해주면 끝이다.

###-----------------pass------------------

# class Unit:
#     def __init__(self, name,hp, speed):
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#
#     def move(self,location):
#         print('[지상 유닛 이동]')
#         print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))
#
# class AttackUnit(Unit):
#     def __init__(self, name,hp,speed,damage):
#
#         Unit.__init__(self,name,hp,speed)
#
#         self.damage = damage
#         print('{0} 유닛이 생성 되었습니다.'.format(self.name))
#         print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))
#
#     def attack(self, location):
#         print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))
#
#
#
#     def damaged(self, damaged):
#         print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
#         self.hp -= damaged
#         print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
#         if self.hp <= 0:
#             print('{0} : 유닛이 파괴되었습니다.'.format(self.name))
#
# class Flyable:
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed
#
#     def fly(self,name, location):
#         print('{0} : {1} 방향으로 날아갑니다. [속도 {2}]'.format(name, location,self.flying_speed))
#
# class Flyable_Attact_Unit(Flyable,AttackUnit):
#     def __init__(self, name, hp, damage,flying_speed):
#         AttackUnit.__init__(self, name, hp,0,damage)
#         Flyable.__init__(self, flying_speed)
#
#     def move(self,location):
#         print('[공중 유닛 이동]')
#         self.fly(self.name, location)
#
# class BuildingUnit(Unit): # 이번에는 건물을 짓는 유닛
#
#     def __init__(self, name, hp, location):
#         pass # 이 패스의 의미는 아무것도 안하고 일단은 넘어가자는 의미이다. (일단은 코드가 완성된 것처럼 보이는 것)
#
# # 서플라이 디폿 생성(유닛의 인구를 조정하는 건물)
# supply_depot = BuildingUnit('서플라이 디폿', 500, '7시')
#
#
# def game_start():
#     print('[알림] : 새로운 게임을 시작합니다.')
#
# def game_over():
#     pass
# game_start()
# game_over()


###---------------super-------------------------

class Unit:
    def __init__(self, name,hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed

    def move(self,location):
        print('[지상 유닛 이동]')
        print('{0} : {1} 방향으로 이동합니다. [속도 {2}]'.format(self.name, location, self.speed))

class AttackUnit(Unit):
    def __init__(self, name,hp,speed,damage):

        Unit.__init__(self,name,hp,speed)

        self.damage = damage
        print('{0} 유닛이 생성 되었습니다.'.format(self.name))
        print('체력 {0}, 공격력 {1}'.format(self.hp, self.damage))

    def attack(self, location):
        print('{0} : {1} 방향으로 적군을 공격 합니다. [공격력{2}]'.format(self.name, location, self.damage))



    def damaged(self, damaged):
        print('{0}: {1} 데미지를 입었습니다.'.format(self.name, damaged))
        self.hp -= damaged
        print('{0} : 현재 체력은 {1}입니다.'.format(self.name, self.hp))
        if self.hp <= 0:
            print('{0} : 유닛이 파괴되었습니다.'.format(self.name))

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
        print('[공중 유닛 이동]')
        self.fly(self.name, location)

class BuildingUnit(Unit):

    def __init__(self, name, hp, location):
        # Unit.__init__(self,name,hp,0) # 건물은 이동을 못하므로 스피드는 0// 이게 기존의 상속 방법
        super().__init__(name,hp,0) # 이게 super의 사용법// super 뒤 () 붙이기, super는 self를 넣지 않기
        # 문제는 다중 상속 시에 발생이 됨. => 다중 상속 시에 super는 맨 앞의 class만 상속 받는다. 그러므로 다중 상속시에는 사용하지 않는다.

        self.location = location
