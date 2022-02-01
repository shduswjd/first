# #마린 : 공격 유닛, 군인, 총을 쓸 수 있음

# name = "마린"
# hp = 40 #유닛의 체력
# damage = 5 #유닛의 공격력

# print("{} 유닛이 생성되었습니다.".format(name))
# print("체력 {0}, 공격력{1}\n".format(hp, damage))

# #탱크 : 공격 유닛, 탱크, 포를 쓸 수 있는데, 일반 모드/ 시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다. ".format(tank_name))
# print("체력 {0}, 공격력{1}\n" .format(tank_hp,tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다. ".format(tank2_name))
# print("체력 {0}, 공격력{1}\n" .format(tank2_hp,tank2_damage))

# def attack(name, location, damage):
#     print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]".format(name,location, damage))


# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank2_name, "1시", tank2_damage)


# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name, location, self.speed))
        # self.damage = damage # 메딕은 의무병이니까 데미지 없음
        # print("{0} 유닛이 생성 되었습니다.".format(self.name)) # 메딕 쓸때는 필요없음
        # print("체력 {0}, 공격력 {1} ".format(self.hp, self.damage)) # 메딕 쓸때는 필요없음

# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit ("탱크",150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹 (상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛이름: {0}, 공격력: {1} ".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} 는 현재 클로킹 상태 입니다.".format(wraith2.name))
# else:
#     print("{0} 는 현재 클로킹 상태가 아닙니다.".format(wraith2.name))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed)
        # self.name = name #위에 Unit 이랑 겹치는게 있기 때문에 굳이 이렇게 안써도 위에 것처럼 써도됨
        # self.hp = hp
        self.damage = damage

    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력 {2}]".format(self.name,location,self.damage))

    def damaged(self,damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print(" {0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 메딕 : 의무병
        
# 파이어뱃 : 공격 유닛, 화염방사기.
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# 공격 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 드랍쉽, 공중 유닛, 수송기. 마린/ 파이어뱃/ 탱크 등을 수송 공격 x

# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed): # 캐릭터 생성
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다 [속도: {2}] ".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스 
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        Flyable.__init__(self, flying_speed)
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 speed = 0
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
        
# 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
valkyrie = FlyableAttackUnit("발키리", 200, 6,5)
valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 좋음
vulture = AttackUnit( "벌쳐", 80, 10, 20)
vulture.move("11시")

# 배틀 크루져 : 공중 유닛, 체력 굉장히 좋음, 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25,3)
# battlecruiser.fly(battlecruiser.name, "9시") #def move 함수를 안썼을때
battlecruiser.move("9시")

# 건물 
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 일단 코드를 완벽히 적지 않아서 서플라이 디폿이라는 캐릭터의 정보입력에도 불구하고 그냥 넘어감

# # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛.
# supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start() #문구가 나옴
# game_over() #pass 해서 문구 없어서 그냥 함수부분 넘어감

# 건물
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0) 이거랑 밑에랑 같은거임
#         super().__init__(name,hp,0)
#         self.location = location


