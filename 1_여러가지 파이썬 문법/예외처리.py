# try: 
#     print("나누기 전용 계산기입니다.")
#     num1 = int(input("첫 번째 숫자를 입력하세요: "))
#     num2 = int(input("두 번째 숫자를 입력하세요: "))
#     print("{0} / {1} = {2}".format(num1, num2, int(num1/num2)))
# except ValueError:
#     print("에러! 잘못된 값을 입력하였습니다.")

#나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요: 6
# 두 번째 숫자를 입력하세요: 삼
# 에러! 잘못된 값을 입력하였습니다.

# except ZeroDivisionError as err:
#     print(err)
#나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요: 6
# 두 번째 숫자를 입력하세요: 0
# division by zero

# try: 
#     print("나누기 전용 계산기입니다.")
#     nums = []
#     nums.append(int(input("첫 번째 숫자를 입력하세요: ")))
#     nums.append(int(input("두 번째 숫자를 입력하세요: ")))
#     # nums.append(int(nums[0]/nums[1]))
#     print("{0} / {1} = {2}".format(nums[0], nums[1], nums[2]))
# except Exception as err:
#     print("알 수 없는 에러가 발생하였습니다.")
#     print(err)
# 만약 나누는 식을 깜빡했다면..이렇게 뜰거임
# 나누기 전용 계산기입니다.
# 첫 번째 숫자를 입력하세요: 6
# 두 번째 숫자를 입력하세요: 3
# 알 수 없는 에러가 발생하였습니다. # except: 하고 print("알수없는~") 이라고만 썼을때
#list index out of range #except Exception as err 하고 print(err)까지 썼을때

#에러 발생시키기
# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요:"))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     if num1>=10 or num2>=10: #만약 num1 또는 num2가 두자리라면 에러임
#         raise ValueError
#     print("{0} / {1} = {2}". format(num1, num2, num1/num2))    
# except ValueError: #에러 뜨게 해줘
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") #에러를 프린트해
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:10
# 두번째 숫자를 입력하세요: 5
# 잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.

#사용자 정의 예외처리
# class BigNumberError(Exception):
#     pass

# try:
#     print("한 자리 숫자 나누기 전용 계산기입니다.")
#     num1 = int(input("첫번째 숫자를 입력하세요:"))
#     num2 = int(input("두번째 숫자를 입력하세요: "))
#     if num1>=10 or num2>=10: #만약 num1 또는 num2가 두자리라면 에러임
#         raise BigNumberError
#     print("{0} / {1} = {2}". format(num1, num2, num1/num2))    
# except ValueError: #에러 뜨게 해줘
#     print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") #에러를 프린트해
# except BigNumberError:
#     print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요. ")
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:10
# 두번째 숫자를 입력하세요: 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요. 

class BigNumberError(Exception):
    def __init__(self, msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 = int(input("첫번째 숫자를 입력하세요:"))
    num2 = int(input("두번째 숫자를 입력하세요: "))
    if num1>=10 or num2>=10: #만약 num1 또는 num2가 두자리라면 에러임
        raise BigNumberError("입력값: {0}, {1}".format(num1, num2))
    print("{0} / {1} = {2}". format(num1, num2, num1/num2))    
except ValueError: #에러 뜨게 해줘
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요.") #에러를 프린트해
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세요. ")
    print(err)
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:10
# 두번째 숫자를 입력하세요: 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요. 
# 입력값: 10, 5
# finally:
#     print("계산기를 이용해 주셔서 감사합니다.") #위에 코드가 에러가 프린트히던 잘 계산하던 항상 마지막에 이거 써줌
# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:10
# 두번째 숫자를 입력하세요: 5
# 에러가 발생하였습니다. 한 자리 숫자만 입력하세요. 
# 입력값: 10, 5
# 계산기를 이용해 주셔서 감사합니다.

# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:6
# 두번째 숫자를 입력하세요: 2
# 6 / 2 = 3.0
# 계산기를 이용해 주셔서 감사합니다.

# 한 자리 숫자 나누기 전용 계산기입니다.
# 첫번째 숫자를 입력하세요:5
# 두번째 숫자를 입력하세요: 0
# 계산기를 이용해 주셔서 감사합니다.
# Traceback (most recent call last):
#   File "/Users/noyeonjeong/Desktop/python workspace/.vscode/예외처리.py", line 85, in <module>
#     print("{0} / {1} = {2}". format(num1, num2, num1/num2))    
# ZeroDivisionError: division by zero


#퀴즈 #쌤이 알려준대로... 거의 다 맞췄는데 아쉽!!
class SoldOUtError(Exception):
    pass

chicken = 10
waiting = 1
while(True):
    try: #try 를 꼭 써줘야해!!
        print(" [남은 치킨: {0}] ".format(chicken))
        order = int(input("치킨 몇 마리 주문하시겠습니까? "))
        if order > chicken: # 남은 치킨보다 주문량 많을때
            print("재료가 부족합니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting,order))
            waiting += 1
            chicken -= order

        if chicken == 0:
            raise SoldOUtError
    except ValueError:
        print("잘못된 값을 입력했습니다.")
    except SoldOUtError:
        print("재고가 소진되어 더이상 주문을 받지 않습니다.") 
        break
