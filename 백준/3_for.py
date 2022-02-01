# import sys
# ip = sys.stdin.read().split().splitlines() # 인풋 넣기

# 1. 
# cases = int(input())
# for case in range(cases):
#     a, b = map(int, input().split())
#     print(a+b)

# 2. 
# a = int(input())
# ans = 0

# for i in range(1, a+1):
#     ans += i
# print(ans)

# 3. 
# import sys
# cases = int(input())

# for case in range(cases):
#     a, b = map(int, sys.stdin.readline().split())
#     print(a+b)

# 4. 
# a = int(input())
# for i in range(1, a+1):
#     print(i)

# 5. 
# a = int(input())
# for i in range(a, 0, -1):
#     print(i)

# 6. 
# import sys
# cases = int(input())

# for case in range(1, cases+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f"Case #{case}: {a+b} ")

# 7. 
# import sys
# cases = int(input())

# for case in range(1, cases+1):
#     a, b = map(int, sys.stdin.readline().split())
#     print(f'Case #{case}: {a} + {b} = {a+b}')

# 8. 
# a = int(input())

# for i in range(1, a+1):
#     print('*' * i)

# 9.
# a = int(input())

# size = a
# for i in range(size):
#     for j in range(1, size - i):
#         print(" ", end="")
#     for k in range(0, i + 1):
#         print("*", end="")
#     print()

# 10.
# n, x = map(int, input().split())

# lst = list(map(int, input().split()))

# for i in lst:
#     if i < x:
#         print(i, end=" ")