# weather = input("오늘 날씨 어때요? ")

# # if 조건
#     #실행명령문
# if weather == "비" or weather == "눈": # 이 조건에 부합한다면 
#     print("우산을 챙기세요") # 이 문장을 프린트 할것이고
# elif weather =="미세먼지": # 이 조건에 맞는다면
#     print("마스크를 챙기세요") #이 문장을 프린트 할것이야
# else: # 조건 외에 모든 경우에는
#     print("준비물이 필요 없어요") # 이 문장을 프린트 해줄거임

# wether = input("오늘 날씨 어때요? ") 라고 코드를 쓰면
# 오늘 날씨 어때요? 라고 컴퓨터가 쓸거야
# 그리고 그옆에 커서가 깜빡거릴거야, 그러면 너가 닶을 쓰면 되 
# 너의 답은 스트링 형태로 저장이 될거야. 그게 바로 input()의 원리

# temp = int(input("기온은 어때요? "))
# if 30 <= temp:
#     print("너무 더워요. 나가지 마세요")
# elif 10 <= temp and temp <30:
#     print("괜찮은 날씨에요.")
# elif 0 <= temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요. 나가지 마세요")

# for waiting_no in range(1,6) : #1, 2, 3, 4, 5 
#     print("대기번호 : {} ".format(waiting_no))
# # 대기번호 : 1 
# # 대기번호 : 2 
# # 대기번호 : 3 
# # 대기번호 : 4 
# # 대기번호 : 5 

# starbucks = ["아이언맨", "토르", "아이엠 그루트"] # 스타벅스 = [손님1, 손님2, 손님3]
# for customer in starbucks:  # 위해(for) 손님들을(customer) 안에(in) 스타벅스(starbucks) = 스타벅스 안에 (있는) 손님들을 위헤 (해보자)
#     print("{}, 커피가 준비되었습니다.".format(customer)) #프린트해줘("커피가 준비되었다고". 손님 1번부터 차례대로)


#while 문을 배워보자
# customer = "노연정"
# index = 5
# #while (조건):
# while index >= 1:
#     print("{0}님, 커피가 준비되었습니다. {1}남았습니다".format(customer,index))
#     index = index - 1 #index -= 1
#     if index == 0:
#         print("{0}님, 커피가 폐기처분 되었습니다.".format(customer))

# customer = "아이언맨"
# index =1
# while True: 
#     print("{}님, 커피가 준비되었습니다. 호출 {}회".format(customer,index))
#     index += 1
# #무한대로 계속 호출을 할때는 while True를 쓴다.
# #output을 멈추고 싶으면 ctrl + c (command + c 해봤는데 안되더라)

# customer = "토르"
# person = "unknown"

# while person != customer:
#     print("{}님, 커피가 준비되었습니다.".format(customer))
#     person = input("이름이 어떻게 되세요?") # 토르가 아니면 계속 이 루프를 반복하고 물어볼것이고 # 토르이면 커피를 줄거니까 이 루프를 탈출하겠지
#     if person == customer:
#         print("감사합니다.")


#continue를 배워보자
# absent = [2, 5]
# no_book = [7]
# for student in range(1,11): #1번부터 11번학생을 위해서 계속 반복해줘
#     if student in absent: #만약 학생중 결석한 친구를 불렀다면
#             continue #건너뛰고 다음 번호 학생을 불러줘
#     elif student in no_book: #만약 학생중 책을 안가져온 친구가 불렸다면
#             print("오늘 수업 여기까지. {} 은 교무실로 따라와".format(student)) # 이 문장을 프린트해줘
#             break #여기서 완전히 끝내줘 (반복문 종료)
#     print("{}, 책을 읽어봐".format(student)) #출석한 친구 이름을 프린트해줘


# 출석번호가 1 2 3 4, 앞에 100을 붙이기로 함 -> 101, 102, 103, 104,,,
# student = [1, 2, 3, 4, 5]
# print(student)
# student = [100+i for i in student] #100+i을 해주는데 i는 student의 원소들이야.
# print(student)

# 학생 이름을 길이로 변환
# student = ["iron man", "Thor", "i am groot"]
# student = [len(i) for i in student]
# print(student)

#학생 이름을 대문자로 변환
# student = ["iron man", "Thor", "i am groot"]
# student = [i.upper() for i in student]
# print(student)

from random import *
customer = 0 #조건이 맞는 손님수, 0명부터 시작!
for i in range(1,51): #1번 승객부터 50번 승객까지
    time = randrange(5,51) #5분 부터 50분 까지 무작위로 선별
    if 5 <= time <= 15: #소요시간이 이범위 안일때
        print("[o] {0} 번째 손님 (소요시간: {1})". format(i,time)) #이걸 프린트해줘
        customer += 1 #customer을 하나씩 증가시켜줘
    else: #그외의 모든 시간은 
        print("[ ]{0} 번째 손님 (소요시간: {1})".format(i, time)) #이걸 프린트해줘
print ("총 탑승 승객수: {0}".format(customer))    # 총 탑승수를 계산해줘
