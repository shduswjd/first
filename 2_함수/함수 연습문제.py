# 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수 is_odd를 작성해라
# def is_odd(num):
#     if num%2 == 0:
#         print("{0}은(는) 짝수입니다.".format(num))
#     else:
#         print("{0}은(는) 홀수입니다.".format(num))
# is_odd(2)
# is_odd(3)
# is_odd(11)

# 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자(입력으로 들어오는 수의 개수는 정해져 있지 않다.)
# args랑 *args는 처음 써보네...아무튼 답지 참고해서 씀
# def mean(*a13,4,5)

# 3과 6을 입력했을 때 9가 아닌 36이라는 결과값을 돌려주었다. 이 프로그램의 오류를 수정해봐
# input1 = input("첫번째 숫자를 입력하세요: ")
# input2 = input("두번째 숫자를 입력하세요: ")
# input1 = int(input1)
# input2 = int(input2)
# total = input1 + input2
# print("두수의 합은 {0}입니다.".format(total))

# 다음 중 출력 결과가 다른 것 한개를 골라 보자.
# print("you" "need" "python") #youneedpython
# print("you" +"need" +"python") #youneedpython
# print("you", "need", "python") #you need python
# print("".join(["you", "need", "python"])) #youneedpython

# 다음은 "test.txt"라는 파일에 "Life is too short" 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# f1 = open("test.txt",'w',encoding = "utf8")
# f1.write("Life is too short")
# f2 = open("test.txt",'r')
# print(f2.read())
# f2.close() 를 써주면 터미널에 프린트 됨
with open("test.txt", 'w', encoding = "utf8") as test_file:
    test_file.write("Life is too short.")
# with open("test.txt", 'r', encoding = "utf8") as test_file:
#     print(test_file.read())

# 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
# new_text = input("새로운 내용을 입력하세요: ")
# with open("test.txt", 'a', encoding = "utf8") as test_file:
#     test_file.write("\n"+new_text)

#Q7 다음과 같은 내용을 지닌 파일 test.txt가 있다. 이 파일의 내용 중 "java" 라는 문자열을 "python"으로 바꾸어서 저장하셈
# 답지 참조함
test_file = open("test.txt", 'a', encoding = "utf8")
test_file.write("\nyou need java")
test_file = open("test.txt", 'r', encoding="utf8")
body = test_file.read()
test_file.close()
body = body.replace("java", "python")
test_file = open("test.txt", 'w', encoding="utf8")
test_file.write(body)
test_file.close()





