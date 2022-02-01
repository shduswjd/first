# 문자열
sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """  
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)#(" " ")하고 한줄쓰고 단락 바꿔서 한줄쓰고 (" " ")
# 나오는 코드: 
# 나는 소년이고,
# 파이썬은 쉬워요

#슬라이싱 배우기
jumin = "990120-1234567" # 프로그래밍 언어는 0부터 시작하니까 9는 0번째 자리
print("성별: " +jumin[7]) #1 #저 숫자들중 7번쨰 숫자를 써줘 
print("연:" +jumin[0:2]) #99 #0번째부터 1번째 자리까지인데 [0:2]의 뜻은 0번째부터 2번째 직전까지니까 99임
print("월: " +jumin[2:4]) #01
print("일:" +jumin[4:6]) #20
print("생년월일:" +jumin[0:6]) #990120 #[:6]으로도 쓸수 있어
print("뒤 7자리:" +jumin[7:14]) #1234567
print("뒤 7자리 (뒤에서부터):" +jumin[-7:]) #1234567 #맨뒤에서부터 가져오는거라서 7이 0번째, 6이 -1번째, 5가 -2번째...

#문자열처리함수
python = "Python is Amazing"
print(python.lower()) #python is amazing
print(python.upper()) #PYTHON IS AMAZING
print(python[0].isupper()) #True #python의 첫번째 값이 대문자야? 응
print(len(python)) #17 #len = 길이 #python이 몇글자임? 17임
print(python.replace("Python", "Java")) #Java is amazing #python의 "Python" dmf "Java" 로 고쳐서 나타내줘

index = python.index("n") #python 값중에 n이 들어가는 자리가 몇번째야? 5
print(index) #5
index = python.index("n", index +1) #첫번째 n이 5번째였잖아 이제 index +1이 5+1 이니까 6번째 자리부터 세서 두번째 n을 찾아줘
print(index) #15

print(python.find("n")) #이것도 비슷해 첫번째 n이 5니까 답은 5
print(python.find("Java")) #-1 #원하는 값이 없으니까 -1로 생성이되
#print(python.index("Java")) #에러가 뜰거야 
# #저 문장에는 Java가 없잖아. 그러니까 그냥 에러를 띈거야
print(python.count("n")) #python 값중에서 n이 총 몇번 등장해? 2번

#문자열포맷
print("a"+"b") #ab
print("a","b") #a b
#방법1
print("나는 %d 살입니다" % 20) #%d (int형) = 값을 넣어줄거야, 뒤에 %쓰고 정수형 변수를 넣어
print("나는 %s을 좋아해요." % "파이썬") # %s = 문자열형
print("Apple은 %c로 시작해요." % "A") # %c = 문자형
# %s는 사실 정수형이든 문자형이든 다 출력 가능해
print("나는 %s 살입니다" % 20)
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))
#방법2
print("나는 {}살입니다." .format(20)) #{}안에 뒤에 format값을 넣는거야
print("나는 {}색과 {}색을 좋아해요." .format("파란", "빨간")) #나는 파란색과 빨간색을 좋아해요.
print("나는 {0}색과 {1}색을 좋아해요." .format("파란", "빨간")) #나는 파란색과 빨간색을 좋아해요.
print("나는 {1}색과 {0}색을 좋아해요." .format("파란", "빨간")) #나는 빨간색과 파란색을 좋아해요.
#방법3
print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
# #나는 20살이며, 빨간색을 좋아해요
print("나는 {age}살이며, {color}색을 좋아해요".format( color = "빨간", age = 20))
#나는 20살이며, 빨간색을 좋아해요
#방법4
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")
#나는 20살이며, 빨간색을 좋아해요

#탈출문자 \n: 줄바꿈
print("백문이 불여일견 \n백견이 불여일타")

# #쓰고싶은 문장: 저는 "나도코딩" 입니다.
# #print("저는 "나도코딩" 입니다") 라고쓰면 error!
print("저는 '나도코딩' 입니다")
#저는 '나도코딩' 입니다
print('저는 "나도코딩" 입니다')
#저는 "나도코딩" 입니다
print("저는 \"나도코딩\" 입니다")
#저는 "나도코딩" 입니다
print("저는 \'나도코딩\' 입니다")
# 저는 '나도코딩' 입니다

# \\: 문장 내에서 \
# print("red\blue\black") #이러면 안되 에러남
print("red\\blue\\black") #red\blue\black

# \r: 커서를 맨앞으로 이동
print("Red Apple\rPine") #Pine이라는 단어를 앞에다 끌어와서 PineApple이 됨

# # \b: 백스페이스 (앞에 한글자 지우기)
print("Redd\bApple") #RedApple

# #\t: 탭
print("Red\tApple") #Red     Apple




#quiz3 :사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오.

#예) http://naver.com
#규칙1: http:// 부분은 제외 -> naver.com
#규칙2: 처음 만나는 점(.) 이후 부분은 제외 -> naver
#규칙3: 남은 글자중 처음 세자리 + 글자갯수 + 글자 내'e' 갯수 + "!" 로 구성
 # = (nav) + (5) + (1) +(!)
 #생성된 비밀번호: nav51!

#쌤이 한거
addr = "http://naver.com" 
first = addr.replace("http://", "") #저 문장을 빈칸으로 바꿀거야
print(first)
first = first[:first.index(".")]
print(first)
password = first[:3] + str(len(first)) + (str(first.count("e"))) +"!"
print(password)
print("{}의 비밀번호는 {}입니다.".format(addr,password))

#내가 다시 해본거.. 어려었어
url = "http://naver.com"
url2 = "http://damn.com"
url3 = "http://google.com"
rule = url3[7:17]
print(rule)
rule = rule[:rule.index(".")]
print(rule)
new = rule[:3] + str(len(rule)) + str(rule.count("e")) +"!"
print(new)
print(f"{url3}의 비밀번호는 {new}입니다")


