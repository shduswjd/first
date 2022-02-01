# print("python", "java", sep = ",")
# print("python", "java", "javascript", sep = " vs " )

# print("python", "java", sep = ",", end = "?") #뒤에 들어오는 문장을 한줄에 붙여서 #python,java? 무엇이 더 재밌을까요?
# print(" 무엇이 더 재밌을까요?")

# import sys
# print("python", "java", file = sys.stdout) #sys. stdout? #python java
# print("python", "java", file = sys.stderr) #sys. stderr? #python java

# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items(): #for 과목명, 성적 in score 라는 사전
#     # print(subject,score) #프린트해줘 (과목명, 성적) 이렇개
#     #수학 0
#     #영어 50
#     #코딩 100
#     print(subject.ljust(8), str(score).rjust(4), sep = " : ") #프린트해줘(과목명.(왼쪽에 8칸띄고), 성적.(오른쪽에 4칸띄고))
    # 수학       :    0
    # 영어       :   50
    # 코딩       :  100

#은행 대기 순번표
# 001, 002, 003 ,...
# for num in range(1,21):
#     # print("대기번호: " + str(num)) # 이러면 대기번호: 1, 대기번호: 2, 대기번호: 3,....
#     print("대기번호: " + str(num).zfill(3)) #이러면 대기번호: 001, 대기번호: 002, ...#zfill(자릿수) = ??? 세자리의 숫자를 만들건데
    #비어있는 자리는 0으로 채워줘

# answer = input("아무 값이나 입력하세요: ")
# print(type(answer)) #숫자를 써도 string으로 표시가 됨
# print("입력하신 값은 {} 입니다.".format(answer))

#빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) #{0: 먼저 10자리공간 확보후 -> 빈공간 에서 오른쪽으로 숫자까지 띄어줘} =(       )500
# #양수일땐 +로 표시, 음수일땐 -로 표시
# print("{0: >+10}".format(500)) # {0: 먼저 10자리 공간 확보후 -> 빈공간에서 오른쪽으로 숫자까지 앞에 부호붙여줘}(      )+500
# print("{0: >+10}".format(-500)) # {0: 먼저 10자리 공간 확보후 -> 빈공간에서 오른쪽으로 숫자까지 앞에 부호 붙여줘}(      )-500
# #왼쪽 정렬하고, 빈칸으로 _로 채움
# print("{0:_<+10}".format(500)) #10자리 공간 확보후 -> 왼쪽에서 오른쪽으로 글을 써줘. = +500______
# # 3자리마다 콤마를 찍어주기
# print("{0:,}".format(1000000000)) #그냥 콤마 찍어주면 될듯... #1,000,000,000
# # 3자리 마다 콤마르 찍어주기, + -부호도 붙이기
# print("{0:+,}".format(10000000000)) # +10,000,000,000
# print("{0:+,}".format(-10000000000)) # -10,000,000,000
# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 돈이 많으면 행복하니까 빈 자리는 ^ 로 채워주기
# print("{0:^<+30,}".format(10000000000000)) #+10,000,000,000,000^^^^^^^^^^^
# # 30만큼 공간 확보 -> 부호 붙여서, 3 자리 수만큼 콤마 붙여서 숫자적어 -> 왼쪽부터 빈자리는 ^로 채워줘

# #소수점 출력
# print("{0:f}".format(5/3)) #1.666667
# # 소수점 특정 자리수 까지만 표시
# print("{0:.2f}".format(5/3)) #1.67 #소수점 둘째자리까지만 표시


# score_file = open("score.txt","w",encoding="utf8") #파일추가 할거야 (score파일) = (이름 = score.txt, 목적 = write , 인코딩 잘부탁)
# print("수학: 0", file = score_file) #옆에 파일 추가된거 보일거임 확인 ㄱ
# print("영어:50", file = score_file)
# score_file.close() # 그 파일 닫아줘

# score_file = open("score.txt","a",encoding="utf8") # "a" = 저 텍스트 파일에 이어서 쓸거라는 의미 (append)
# score_file.write("과학: 80")
# # score_file.write("코딩: 100") #이렇게 쓰면 과학:80 코딩:100 이어서 써질거야
# score_file.write("\n코딩:100") #이렇게 쓰면 과학 80 (줄바꿈) 코딩:100 
# score_file.close() 
# score_file = open("score.txt", "r", encoding = "utf8") #"r" = read의 약자
# print(score_file.read())
# score_file.close()

# score_file = open("score.txt", "r", encoding = "utf8")
# # print(score_file.readline()) # 한줄씩 읽기 그럼 한줄 쓰고 -> 한줄 띄고 -> 한줄쓰고 -> 한줄 띄고
# # print(score_file.readline())
# # print(score_file.readline())
# # print(score_file.readline())
# print(score_file.readline(), end = " ") # 한줄씩 읽기 그럼 한줄 쓰고 -> 한줄쓰고 -> 한줄 쓰고
# print(score_file.readline(), end = " ")
# print(score_file.readline(), end = " ")
# print(score_file.readline(), end = " ")
# score_file.close()

# (방법1) 만약 몇줄인지 모르고 그냥 한줄씩 불러오고 글이 없으면 닫히는거 
# score_file = open("score.txt", "r", encoding = "utf8")
# while True:
#     line = score_file.readline()
#     print(line)
#     if not line:
#         break
# score_file.close()

# (방법 2) 만약 몇줄인지 모르고 그냥 한줄씩 불러오고 글이 없으면 닫히는거 
# score_file = open("score.txt", "r", encoding = "utf8")
# lines = score_file.readlines()
# for line in lines:
#     print(line, end =" ")

# import pickle
#저장 하는법
# profile_file = open("profile.pickle", "wb") #피클은 뒤에 .pickle 써주고 "wb"처럼 b를 써줘야해
# profile = {"이름": "박명수", "나이": 30, "취미": ["축구", "코딩", "골프"]}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

#저장한걸 받아오는 방법
# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# import pickle
# with open("profile.pickle", "rb") as profile_file: # profile_file = open("profile.pickle", "rb")랑 같은 말
#     print(pickle.load(profile_file))
# #close 필요 없음

# with open("study.txt", "w", encoding = "utf8") as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어요.")

# with open("study.txt", "r", encoding = "utf8") as study_file:
#     print(study_file.read())

#quiz (내가쓴거)
for report in range(1,51):
    with open("%d주차.txt" %report, "w", encoding = "utf8") as report_file:
        report_file.write(" - %d주차 주간보고 -" %report)
        report_file.write("\n부서: ")
        report_file.write("\n이름: ")
        report_file.write("\n업무 요약: ")

#quiz (선생님이 쓰신거) -안나오는디??? 내가쓴걸 다 지워서 그런가
for i in range(1,51):
    with open(str(i) + "주차.txt", "w", encoding = "utf8") as report_file:
        report_file.write(" - {0}주차 주간보고 - ".format(i))
        report_file.write("\n부서:")
        report_file.write("\n이름:")
        report_file.write("\n업무 요약:")


# 어쩄든 내가 쓴 코드도 성공!!