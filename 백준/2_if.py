# 1. 
# a, b = map(int, input().split())

# if a < b : 
#     print('<')
# if a > b : 
#     print('>')
# if a == b:
#     print('==')

# 2. 
# a = int(input())

# if a >=90:
#     print('A')
# elif a >= 80:
#     print('B')
# elif a >= 70:
#     print('C')
# elif a >= 60:
#     print('D')
# else:
#     print('F')

# 3. 
# year = int(input())

# if ((year%4 == 0) and (year%100 != 0)):
#     print(1)
# elif ((year%4 == 0) and (year%400 == 0)):
#     print(1)
# else:
#     print(0)

# 4. 
# a = int(input())
# b = int(input())

# if a>=0 and b>=0:
#     print(1)
# elif a<0 and b>=0:
#     print(2)
# elif a<0 and b<0:
#     print(3)
# else:
#     print(4)

# 5.
h, m = map(int, input().split())

# if a>0:
#     if 0<=b<45:
#         print(a-1, 60-45+b)
#     if 45<b and b<=59:
#         print(a, b-45)
# if a == 0:
#     if 0<=b<45:
#         print(23, 60-45+b)
#     if 45<b and b<=59:
#         print(23, 6-45)

if m > 44:
    print(h, m-45)
elif m<45 and h>0:
    print(h-1, m+15)
else: #0시
    print(23, m+15)

