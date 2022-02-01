# 구글에서 list of python modules라고 검색

# glob = 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
# import glob
# print(glob.glob("*.py")) # 확장자가 py인 모든 파일
#['자료구조.py', '문자열처리.py', '클래스_퀴즈.py', '나도코딩_코딩퀴즈#3.py', '연산자.py', '모듈과 패키지.py', 'ch2_FromOnline.py', '함수.py', '입출력.py', 'practice.py', '클래스_스타 전반전.py', '함수 연습문제.py', '클래스.py', 'helloworld.py', 'practice_class.py', '제어문.py']

# os : 운영체제에서 제공하는 기본 기능
# import os
# print(os.getcwd()) # 현재 디렉토리
# /Users/noyeonjeong/Desktop/python workspace

# folder = "sample_dir" #folder이름: sample_dir
# if os.path.exists(folder): #만약에 os의 path(경로)에 exist(존재)하면 folder("폴더")가
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder, "폴더를 삭제하였습니다.")
# else: #그렇지 않으면 
#     os.makedirs(folder) #os의 변수를 만들어줘 folder(폴더이름: sample_dir)라는 것을
#     print(folder, "폴더를 생성하였습니다.")

# print(os.listdir()) #위의 golb과 비슷
# ['자료구조.py', 'profile.pickle', 'study.txt', '문자열처리.py', '클래스_퀴즈.py', '나도코딩_코딩퀴즈#3.py', '연산자.py', '모듈과 패키지.py', 'ch2_FromOnline.py', '함수.py', '입출력.py', 'practice.py', '클래스_스타 전반전.py', '함수 연습문제.py', '클래스.py', 'sample_dir', 'test.txt', 'helloworld.py', '.vscode', 'score.txt', 'practice_class.py', 'travel', '제어문.py']

# time : 시간 관련 함수
# import time
# print(time.localtime())
# time.struct_time(tm_year=2021, tm_mon=7, tm_mday=9, tm_hour=19, tm_min=0, tm_sec=40, tm_wday=4, tm_yday=190, tm_isdst=0)
# print(time.strftime("%Y-%m-%d %H:%M:%S"))  #쉽게 알아볼수 있음
# 2021-07-09 19:02:45

import datetime
# print("오늘 날짜는 ", datetime.date.today())
# 오늘 날짜는  2021-07-09

# timedelta : 두 날짜 사이의 간격
today = datetime.date.today() # 오늘 날짜 저장
td = datetime.timedelta(days=100) # 100일 저장
print("우리가 만난지 100일은", today + td) #오늘부터 100일후의 날짜 계산
# 우리가 만난지 100일은 2021-10-17