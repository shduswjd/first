# 1.
def solve(a: list):
    return(sum(a))

print(solve([1, 2, 3, 4, 5]))
### 백준 템플릿
def solve(a):
    ans = sum(a)
    return ans

# 2. (내가 리스트로 써본거 물론 답지 먼저 봄)
lst = list(range(1, 10001))
gens = []
not_gens = []
for i in lst:
    for j in str(i):
        i += int(j)
    gens.append(i)

self_num = set(lst).difference(gens)
for num in sorted(self_num):
    print(num)

# 2. 답지
sets = set(range(1, 10001))
gens = set()
for i in sets:
    for j in str(i):
        i += int(j)
    gens.add(i)

self_num = sorted(sets - gens)
for i in self_num:
    print(i)

    

# 3. (c언어 답지로 봄...)
n = int(input())
count = 0 
for i in range(1, n+1):
    if i < 100: #두자리 수
        count += 1
    
    if i >= 100: #세자리수
        one = i % 10
        ten = (i % 100) // 10
        hund = i // 100
        if (hund - ten) == (ten - one):
            count += 1
print(count)