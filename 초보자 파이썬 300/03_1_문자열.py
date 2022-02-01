# 21.
letters = 'python'
print(letters[0], letters[2])

# 22.
license_plate = '24가 2210'
print(license_plate[4:])

# 23.
string = '홀짝홀짝홀짝'
for i in string:
    if i == '홀':
        print(i, end='')

# 23 또다른 답:
string = '홀찍홀찍홀찍'
print(string[::2])

# 24
string = 'PYTHON'
print(string[::-1])

# 25.
phone_number = '010-1111-2222'
print(phone_number.replace('-', ' '))

# 26.
phone_number = '010-1111-2222'
phone_number_new = phone_number.replace('-', '')
print(phone_number_new)

# 27.
url = 'http://sharebook.kr'
print(url[-2:])

# 27 또다른 답
url = 'http://sharebook.kr'
con = url.split('.')
print(con[-1])

# 28. 
lang = 'python'
lang[0] = 'P'
print(lang) #에러가 뜸. 문자열은 수정할 수 없다

# 29.
string = 'abcdfe2a354a32a'
string_cap = string.replace('a', 'A')
print(string_cap)

# 30.
string = 'abcd'
string.replace('b', 'B')
print(string) # abcd가 그대로 출력됨. 왜냐면 문자열은 변경할수 없는 자료형. 
# replace메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴


