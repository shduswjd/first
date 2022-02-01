# def open_accout(): # def 함수 = 함수를 정의할거임
#     print("새로운 계좌가 생성되었습니다.") # 프린트 해줘 ("새로운 계좌가 생성되었습니다.")
#     # 여기까지만 쓰면 시스템 돌려도 안뜰거임^^
# open_accout() # 마지막에 함수의 이름을 불러줘야 저 프린트가 뜸

 
# def deposit(balance, money): #함수를 정의할거야: 이름은 "입금" 그안에 원소는(잔액, 보너스)
#     print("입금이 완료되었습니다. 잔액은 {0}입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money): #출금 
#     if balance >= money: #잔액이 출금보다 많으면 -> 출금 가능
#         print("출금이 완료되었습니다. 잔액은 {0}입니다".format(balance - money))
#         return balance - money
#     else: #잔액이 출금보다 적으면 -> 출금 불가능
#         print("출금이 완료되지 않았습니다. 잔액은 {0}입니다".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100 #수수료 100원
#     return commission, balance - money - commission

# balance = 0 #처음 있었던 잔액 = 0원
# balance = deposit(balance, 1000)
# # balance = withdraw(balance,500)
# commission, balance = withdraw_night(balance, 500)
# print("수수료는 {0}원이며, 잔액은 {1}입니다.".format(commission, balance))

# def profile(name, age, main_lang):
#     print("name:{0}\t age:{1}\t main langauage:{2} ".format(name, age, main_lang))

# profile("유재석", 20, "파이썬")
# profile("김태호", 25, "자바")

#같은학교, 같은 학년, 같은반, 같은 수업이라면..
# def profile(name, age = 17, main_lang = "파이썬"):
#     print("name:{0}\t age:{1}\t main langauage:{2} ".format(name, age, main_lang))

# profile("유재석")
# profile("김태호")

# def profile(name, age, main_lang):
#     print(name, age, main_lang)

# profile(name = "유재석", main_lang="파이썬", age = 20) #유재석 20 파이썬
# profile(age = 25, main_lang = "자바", name = "김태호") #김태호 25 자바

# def profile(name, age, lang1, lang2, lang3, lang4, lang5): #할줄아는 언어가 추가되고 빼고 이러면 너무 불편하기 때문에
#     print("name:{0}\t age:{1}\t".format(name, age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# def profile(name, age, *language):
#     print("name:{0}\t age:{1}\t".format(name, age), end = " ")
#     for lang in language:
#         print(lang, end=" ")
#     print()

# profile("유재석", 20, "python", "java", "C", "C++", "C#")
# profile("김태호", 23, "kotlin", "swift")


# gun = 10

# def checkpoint(soldiers):
#     global gun #함수 밖에 있는 gun 값을 끌어와서 쓸거야
#     gun = gun - soldiers
#     print("[함수내] 남은 총: {0}".format(gun))

# def checkpoint(gun, soliders):
#     gun = gun - soliders
#     print("[함수 내] 남은 총: {0}".format(gun))
#     return gun


# print("전체 총:{0}".format(gun))
# # checkpoint(2)
# gun = checkpoint(gun, 2)
# print("남은 총: {0}".format(gun))

#quiz 내가 쓴거...
def std_weight(height, gender):
    # man_weight = (height/100) * (height/100) *22
    # woman_weight = (height/100) * (height/100) *21
    # height, gender = input("키와 성별을 입력해주세요.") -> 안됨
    if gender == "man":
        man_weight = (height/100) * (height/100) *22
        print("키 %dcm 남자의 표준 체중은 %.2fkg 입니다." % (height, man_weight))

    else:
        woman_weight = (height/100) * (height/100) *21
        print("키 %dcm 여자의 표준 체중은 %.2fkg 입니다." % (height, woman_weight))
    
# gender = "man"
std_weight(175,"man")
std_weight(165,"woman")
# gender = input("성별을 입력해주세요:") ->안됨
# height = input("키를 입력해주세요:") -> 안됨


#quiz 선생님이 쓰신거
def std_weight(height, gender):
    if gender == "남자":
        return (height/100) * (height/100) * 22 #이게 약간 x + y = z일때 z를 의미하는듯, 답을 의미함.
                                                # 예를 들면 내가 height = x, gender = y라고 가정하면 z는 std_weight의 답이 되는거임, 즉 공식(?)을 의미한다.  줄 109 번으로 ㄱ
    else:
        return (height/100) * (height/100) * 21

gender = "남자"
height = 175
weight = round(std_weight(height, gender), 2)# 결국 저 식들이 표준 체중 공식이잖아? 그러니까 height와 gender를 입력받아서 아 얘가 남자/여자 구별하고 키를 인식하면, 그제서야 여자면 여자공식, 남자면 남자공식에다 대입하겠지.
# 그리고 대입해서 나온 값이 weight에 저장이 되는거야. 
print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight)) #round(값, 소숫점자리) 까먹고 있었음ㅋㅋ


#다시 새롭게 쓴건데 내가써도 이해가 안감ㅋ
def std_weight(height, gender):
    # man_weight = (height/100) * (height/100) *22
    # woman_weight = (height/100) * (height/100) *21
    if gender == "남자":
        weight =  round((height/100) * (height/100) *22, 2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다." .format(height, gender, weight))
        return weight

        
    else:
        weight = round((height/100) * (height/100) *21, 2)
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, weight))
        return weight

std_weight(177, "남자")
        