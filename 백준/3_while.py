# 1. 
# while True:
#     a, b = map(int, input().split())
    
#     if a == 0 and b == 0:
#         break
#     else:
#         print(a + b)

# 2. 
# while True:
#     try:
#         a, b = map(int, input().split())
#     except:
#         break
#     print(a+b)

# 3. 
# 인터넷에서 보고 쓴 코드
my_num = int(input())
check_num = my_num
count = 0
while True:
    tens = my_num//10
    ones = my_num%10
    total = (tens + ones)%10 #8
    my_num = (ones * 10) + total #68
    count += 1
    if my_num == check_num:
        break
print(count)


# 내가 이해하면서 쓴 코드
num = int(input())
check = num # 확인할 숫자 저장
count = 0 # 사이클수
cycle = True

while cycle:
    ten = num // 10 #2
    one = num % 10 #6
    ans = (ten + one) % 10 # 숫자 더해서 일의 자리 숫자 저장
    count += 1
    num = (one * 10) + ans
    if check == num:
        cycle = False
print(count)
