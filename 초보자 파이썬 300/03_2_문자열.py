# 31.
# a = '3'
# b = '4'
# print(a+b) #34

# 32.
print('Hi' * 3)

# 33.
print('-' * 80)

# 34.
t1 = 'python'
t2 = 'java'
print((t1 + '  '+ t2 + '  ') * 4)

# 35.
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13

print('이름: %s 나이: %d' % (name1, age1))
print('이름: %s 나이: %d' % (name2, age2))

# 36.
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13

print('이름: {0} 나이: {1}'.format(name1, age1))
print('이름: {0} 나이: {1}'.format(name2, age2))

# 37.
name1 = '김민수'
age1 = 10
name2 = '이철희'
age2 = 13

print(f'이름: {name1} 나이: {age1}')
print(f'이름: {name2} 나이: {age2}')

# 38.
상장주식수 = "5,969,782,550"
상장주식수 = 상장주식수.replace(',', '')
상장주식수 = int(상장주식수)
print(상장주식수)
print(type(상장주식수))

# 39.
분기 = '2020/03(E) (IFRS연결)'
print(분기[:7])

# 40.
data = "   삼성전자    "
data = data.replace(' ', '')
print(data)

# 40.
# 문자열에서 strip() 메서드를 사용하면 좌울의 공백을 제거할수 있다.
# 이때 원본 문자열은 그대로 유지되고 공백이 제거된 문자열이 반환된다.
data = "   삼성전자    "
data1 = data.strip()
print(data1)
