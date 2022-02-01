# 1.
n = int(input())
nums = list(map(int, input().split()))
print(min(nums), max(nums))

# 2. 
n = 9
nums = [int(input()) for i in range(n)]
max_num = max(nums)
print(max_num)
print(nums.index(max_num)+1)

# 3.
n = 3
a, b, c = [int(input()) for i in range(n)]
ans = list(str(a * b * c ))#17037300

for i in range(10):
    print(ans.count(str(i)))

# 4.
nums = [int(input()) for i in range(10)]
last = [i%42 for i in list(nums)]
last_set = set(last)
print(len(last_set))


# 5.
n = int(input())
scores = list(map(int, input().split()))
max_score = max(scores) # 최고점 저장
new_score_lst = []

for score in scores:
    new_score = (score/max_score) * 100
    new_score_lst.append(new_score)

mean = sum(new_score_lst)/ len(new_score_lst)
print(mean)

# 6. (답지 봤음...)
n = int(input())
for i in range(n):
    q = list(input())
    score = 0
    count = 0 #o의 개수 ()

    for j in q:
        if j == 'O':
            count += 1
            score += count
        if j == 'X':
            count = 0
    print(score)
        
# 7.
c = int(input()) # case수
for case in range(c):
    nums = list(map(int, input().split()))
    num_score = nums[0]
    score_lst = nums[1:]
    mean = sum(score_lst)/len(score_lst)
    top_score = []
    for score in score_lst:
        if score > mean:
            top_score.append(score)
    pct = (len(top_score) / len(score_lst)) * 100
    print(f'{pct:.3f}%')


