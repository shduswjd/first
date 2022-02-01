# 1.
# a, b, c = map(int, input().split())

# if b >= c:
#     print(-1)
# else:
#     print(int(a//(c-b)+1))

# 2.
# 1개 - 1
# 방 6개 = 2~7
# 방 12개 = 8~19
# 방 18개 = 20~37
# 방 6*n(칸)
# i = int(input())
# first = 1
# count = 1
# while i > first:
#     first += 6 * count
#     count += 1
# print(count)

# 3.
n = int(input())
# total_list = []
# new_list = []
# for i in range(1, n+1):
#     if n%2 == 0:
#         make_frac = f'{i}/{n+1-i}'
#         new_list.append(make_frac)
#     else:
#         make_frac = f'{n+1-i}/{i}'
#         new_list.append(make_frac)

line = 0
max_num = 0
while n > max_num: #3
    line += 1
    max_num += line
gap = max_num - n

if line%2 == 0:
    top = line - gap
    under = gap + 1
else:
    top = gap + 1
    under = line - gap
print(f'{top}/{under}')






