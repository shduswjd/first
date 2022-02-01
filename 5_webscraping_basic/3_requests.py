import requests
res = requests.get("http://www.google.com")
# res = requests.get("http://www.nadocoding.tistory.com")
res.raise_for_status() #저 if문 이랑 똑같은 함수
# 이렇게 쌍으로 쓴다는걸 기억해줭!
# print('웹 스크래핑을 진행합니다.')

# print('응답코드: ',res.status_code) #200이면 정상

# if res.status_code == requests.codes.ok:
#     print("정상입니다")
# else : 
#     print("문제가 생겼어요. [에러코드: ",res.status_code, "]")

print(len(res.text))
print(res.text)

with open("mygoogle.html", "w", encoding = "utf8") as f:
    f.write(res.text)
