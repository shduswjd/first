# 리스트 []

# 지하철 칸별로 10명, 20명, 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)
subway = ["유재석", "조세호", "박명수"]
print(subway)

# # 조세호씨는 몇번쨰 칸에 타고 있는가?
print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음칸에 탐
subway.append("하하") #append는 항상뒤에 붙게된다.
print(subway)

# #정형돈씨를 유재석/ 조세호 사이에 태워봄
subway.insert(1, "정형돈")
print(subway)

# # 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop()) #하하
print(subway) #[유재석, 정형돈, 조세호, 박명수]

print(subway.pop()) #박명수
print(subway) #[유재석, 정형돈, 조세호]

print(subway.pop()) #조세호
print(subway) #[유재석, 정형돈]

# # 같은 사람이 몇명이 있는지?
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# # 정렬도 가능
num_list = [5, 2, 4, 3, 1]
num_list.sort() #[[1, 2, 3, 4, 5]
print(num_list)

num_list.reverse() #[5,4,3,2,1]
print(num_list)

num_list.clear()
print(num_list)

# # 다양한 자료형 함꼐 사용 가능
mix_list = ["조세호", 20, True]
print(mix_list)

# # 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)

# 사전 (key번호, value) 중복 불가능
cabinet = {3:"유재석`", 100:"김태호"}
# 3번 키를 유재석이 가지고 있고 100번 키를 김태호가 가지고 있어
print(cabinet[3]) 
# 프린트 해줘(캐비넷의[3번열쇠])를 누가 가지고 있어? 유재석
print(cabinet[100])

print(cabinet.get(3)) #print(cabinet[3]) 랑 같은 표현
# print(cabinet[5]) #에러뜰거임 5번 키는 아무도 안가지고 있으니까
print(cabinet.get(5)) #None이라고 뜸
print(cabinet.get(5,"사용 가능")) #사용 가능 #5번키에 사용가능이라는 값을 넣어주는거야

print(3 in cabinet) #True # 프린트해줘(3번키가 캐비넷 안에)? 예스
print(5 in cabinet) #False # 프린트해줘(5번키가 캐비넷 안에)? 노웁

#키번호가 만약 문자라면?
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"]) #유재석
print(cabinet["B-100"]) #김태호

#새손님
cabinet["A-3"] = "김종국" #원래 A-3은 유재석이었는데 김종국으로 업뎃이됨
cabinet["C-20"] = "조세호" #캐비넷c-20에 새로운 주인 등장
print(cabinet) #{'A-3': '김종국', 'B-100': '김태호', 'C-20': '조세호'}

#간 손님
del cabinet["A-3"] # 지워줘 캐비넷 A-3번
print(cabinet) #{'B-100': '김태호', 'C-20': '조세호'}

#사용중인 key들을 출력해줘
print(cabinet.keys()) #dict_keys(['B-100', 'C-20'])

#사용중인 value들만 출력해줘
print(cabinet.values()) #dict_values(['김태호', '조세호'])

#key, value 쌍으로 출력
print(cabinet.items()) #dict_items([('B-100', '김태호'), ('C-20', '조세호')])

# 목욕탕 폐점
cabinet.clear()
print(cabinet) #{}

#튜플 
#예를 들면 돈가스 집에 메누를 생각해보자
menu = ("돈가스", "치즈까스")
print(menu[0]) #돈까스
print(menu[1]) #치즈까스
# menu.add("생선가스") #에러남 
#튜플은 원소를 더하고 뺼수가 없어

name = "김종국"
age = 20
hobby = "코딩"
print(name, age, hobby) #김종국 20 코딩

#튜플의 형태로 한다면
(name, age, hobby) = ("김종국", 20, "코딩")
print(name, age, hobby) #김종국 20 코딩

# 집합 = 세트 =set
# 중복 안됨, 순서 없음
my_set = {1,2,3,3,3} # my_set라는 바구니에 1, 2, 3, 3, 3 총 카드 5장이 있어
print(my_set) #{1, 2, 3} # 프린트해줘(my_set) -> my_set에는 1카드, 2카드, 3카드 있다. 

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java & python 을 모두 할 수 있는 개발자)
print(python & java) #{'유재석'} #프린트해줘(파이썬 & 자바)
print(java.intersection(python)) #{'유재석'} # 위아래 똑같음

# 합집합 (java 할수 있거나 python 할수 있는 개발자)
print(java | python) # {'김태호', '유재석', '박명수', '양세형'} 
print(java.union(python)) # {'김태호', '유재석', '박명수', '양세형'}

# 차집합 (java 할수 있지만 python은 할줄 모르는 개발자)
print(java-python) #{'양세형', '김태호'}
print(java.difference(python)) #{'양세형', '김태호'}

# python 할줄 아는 사람이 늘어남
python.add("김태호") #파이썬에 넣어줘("김태호"를)  #{'박명수', '김태호', '유재석'}
print(python)
 
 # java 를 잊었어요
java.remove("김태호") # 자바에서.빼줘("김태호"를) #{'유재석', '양세형'}
print(java)

# 자료구조의 변경
# 예를 들면 커피숍
menu = { "커피", "우유", "주스"} # {}는 세트니까 밑에 타입도 menu는 세트라고 나옴
print(menu,type(menu)) # {'우유', '커피', '주스'} <class 'set'> # 프린트해줘(메뉴, 메뉴의 타입)

menu = list(menu) #메뉴 = 리스트(메뉴) -> 세트에서 리스트로 바꿀거임
print(menu,type(menu)) #프린트해줘(메뉴, 메뉴의 타입 # ['우유', '주스', '커피'] <class 'list'> 리스트니까 []바뀜

menu = tuple(menu) #메뉴 = 튜플(메뉴) -> 리스트(메뉴) 에서 튜플(메뉴) 로 바꿀거야
print(menu, type(menu)) #프린트해줘(메뉴, 메뉴의 타입) # ('커피', '우유', '주스') <class 'tuple'> 튜플이니까 () 버뀜

menu = set(menu) # 메뉴 = 세트(메뉴) -> 튜플(메뉴)에서 다시 세트(메뉴)로 바꿀거야
print(menu, type(menu)) #프린트해줘(메뉴, 메뉴타입) #{'주스', '우유', '커피'} <class 'set'> 세트니까 {} 바뀜

# # quiz #내가 쓴거
from random import * 
id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(" -- 당첨자 발표 -- ")
shuffle(id)
chicken = sample(id,1)
print("치킨 당첨자: " +str(chicken))
chicken_s = set(chicken)
id_s = set(id)
id2_s = id_s - chicken_s
# print(id2_s)
id2 = list(id2_s)
shuffle(id2)
coffee = sample(id2,3)
print("커피 당첨자:" + str(coffee))
print(" -- 축하합니다 --")


#quiz 선생님이 쓴거
from random import *
users = range(1,21) # 1번 부터 20까지
# print(type(users)) #<class, range>
users = list(users)  # range(users) 을 list(users)로 바꿔줘
shuffle(users) # 숫자 섞어줘

# 치킨 1명, 커피 3명 이니까 총 4명을 뽑아야되
winners = sample(users,4)

print(" -- 당첨자 발표 -- ")
print("치킨 당첨자: {0}".format(winners[0]))
print("커피 당첨자: {0}" .format(winners[1:]))
print("-- 당첨을 축하합니다. -- ")