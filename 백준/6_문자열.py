# 1.
a = input() # ord(문자) :아스키 코드를 반환해준다.
# a = int(input()) chr(숫자) : 숫자에 맞는 아스키 코드를 반환한다.
print(ord(a))

# 2.
n = int(input())
nums = list(str(input()))
adding = 0
for num in nums:
    num = int(num)
    adding += num
print(adding)


# 3.
import string
n = list(input())
alpha = string.ascii_lowercase
for albet in alpha: #a부터 시작
    if albet in n:
        print('{0}'.format(n.index(albet)), end=' ')
    else: # 알파벳이 없을때
        print(-1, end=' ')

# 4.
cases = int(input())
for case in range(cases):
    num, strings = input().split()
    num = int(num)
    strings = list(strings)
    for st in strings:
        print(st * num, end='')
    print()

# 5. (답지 봄....)
strings = input().lower()
count_lst = []
strings_set = list(set(strings))
for i in strings_set:
    count = strings.count(i)
    count_lst.append(count)
# print(count_lst)
if count_lst.count(max(count_lst)) >= 2:
    print('?')
else:
    print(strings_set[count_lst.index(max(count_lst))].upper())

# 6.
word_lst = list(input().split())
print(len(word_lst))


# 7. (이건 내가 한건데...)
a, b = map(int, input().split())
a = list(str(a))
a.reverse()
b = list(str(b))
b.reverse()

for i, j in zip(a, b):
    i = int(i)
    j = int(j)
    # print(i ,j)
    if i > j:
        a = list(map(int,a))
        for com in a:
            print(int(com), end='')
        print()
        break
    else:
        b - list(map(b))
        for com in b:
            print(int(com), end='')
        print()
        break

# 7. (이건 답지... 와 개쉬웠네)
num1, num2 = input().split()
num1 = int(num1[::-1])
num2 = int(num2[::-1])
if num1 > num2:
    print(num1)
else:
    print(num2)

# 8.  (이것도 어려웠음...ㅜㅜ)
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

strings = input()
for st in strings: # w
    for i in dial: 
        if st in i:
            time += dial.index(i) + 3
print(time)
        

# 9. (이것도 개어려웁)
word_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for w in word_list:
    word = word.replace(w, '*')
print(len(word))

# 10.
cases = int(input())
for i in range(cases):
    word = input().rstrip() #happy

    for j in range(len(word)-1): #h
        if word[j] != word[j+1]: # h != a
            if word[j] in word[j+1:]:
                cases -= 1
                break
print(cases)

