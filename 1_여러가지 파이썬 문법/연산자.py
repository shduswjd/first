#연산자
# print(1+1) #2
# print(3-2) #1
# print(5*2) #10
# print(6/3) #2

# print(2**3) #2^3=8
# print(5%3)#나머지 구하기
# print(10%3) #1

# print(5//3) #몫구하기 = 1
# print(10//3) #3

# print(10>3) #true
# print(4>=7) #false
# print(10<3) #false
# print(5<=5)#true

# print(3 == 3) #앞에 내용과 뒤의 내용이 같은가를 비교 #true
# print(4 == 2) #false
# print(3+4 == 7) #true

# print(1 != 3) #true # (!=)이 기호는 같지 않다
# print(not (1!=3)) #false

# print((3>0) and (3<5)) #true #둘중 하나라도 다르면 false, 두개 다 같아야지 true
# print((3>0) & (3<5)) #true #shift+7누르면 &나옴

# print((3>0) or (3<5))#true #둘중 하나만 맞아도 true
# print((3>0) | (3>5) ) #true # |는 키보드에 있음(엔터위에)

# print(5>4>3) #true
# print(5>4>7)#false

#간단한 수식
# print(2+3*4) #14
# print((2+3)*4) #20
# number = 2 + 3 *4 #14
# print(number)
# number = number +2 #16 #아까 넘버에다 2를 더해서 새로운 넘버가 탄생하는거야
# print(number)
# number +=2 #18  #number = number +2랑 완전 똑같은식
# print(number)
# number *= 2 #36
# print(number)
# number /= 2 #18
# print(number)
# number -= 2 #16
# print(number)
# number %= 5
# print(number) #1

#숫자처리함수
# print(abs(-5))
# print(pow(4,2)) #4^2 = 4*4 = 16
# print(max(5,12))
# print(min(5,12))
# print(round(3.14)) #3 #반올림
# print(round(4.99)) #5

# from math import* #수학 라이브러리를 모두 사용하겠다 라는 의미
# print(floor(4.99)) #4 #내림
# print(ceil(3.14)) #4 올림
# print(sqrt(16)) #4 제곱근

#랜덤함수
from random import*
# print(random()) #0.0 이상 1.0 미만의 임의의 값 생성
# print(random()*10)
print(int(random()*10)) #0~10 미만의 임의의 값을 생성
# print(int(random()*10) +1) #1 ~ 10 이하의 임의의 값 생성

#로또가 이렇게 생기는 거임
# print(int(random() *45) +1) #1~45 이햐의 임의의 값 생성
# print(int(random() *45) +1)
# print(int(random() *45) +1)
# print(int(random() *45) +1)
# print(int(random() *45) +1)
# print(int(random() *45) +1)

# print(randrange(1,46)) #1~46 미민의 임의의 값 생성
# print(randrange(1,46)) #randrange는 끝점 포함 x
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))
# print(randrange(1,46))

# print(randint(1,45)) #1~45 이하의 임의의 값 생성
# print(randint(1,45)) #randint는 양끝점 모두 포함
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))
# print(randint(1,45))

#quiz2
# 당신은 최근에 코딩 스터디 모임을 새롤 만들었습니다. 
#월4회 스터디를 하는데 3번은 온라인으로 하고 1번은 오프라인으로 하기로 함
# 아래 조건에 맞는 오프라인 모임 날짜를 정해주는 프로그램 작성하시오
# 조건1: 랜덤으로 날짜를 뽑아야함
# 조건2: 월별 날짜는 다름을 감안하여 최소 일수인 28일 이내로 정함
# 조건3: 매월 1~3일은 스터디 준비를 해야하므로 제외
# 출력문 예제: 오프라인 스터디 모임 날짜는 매월 x일로 선정되었습니다. 

# from random import*
# date = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월" +str(date)+ "일로 선정되었습니다.")

#내가 만든 랜덤숫자 놀이
# from random import*
# num1 = randint(1,99)
# num2 = randint(1,99)
# num3 = randint(1,99)
# num4 = randint(1,99)
# num5 = randint(1,99)
# num6 = randint(1,99)
# print("오늘의 로또 번호: " +str(num1), str(num2), str(num3), str(num4), str(num5), str(num6))