# url의 2가지 형태
# 1. get: 누구나 알아볼수 있도록 하는 url의 형식 -> 데이터 제한이 있어서 큰 데이터 x
# 예시) http://www.coupang.com/np/search?minPrice = 1000 & maxPrice = 100000 & page = 1
# 2. post: http메세지의 바디에 숨겨서 보내는 방식 ->아이디와 비번을 누루고 하는 웹페이지
# 예시) 한번 누를때마다 계속 url을 바뀌어지는 것

import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get(url, headers= headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# print(res.text)

# 광고가 붙여진 건 search-prodcut-ads~이렇게 뒤에 뭐 붙여져있고
# 광고가 없는건 search-product만 있기때문에
# 정규식을 이용해서 앞에 search-product로 된 제품을 다 찾아줘 하면 나오겠지?!

# print(res.text)
items = soup.find_all("li", attrs = {"class": re.compile("^search-product")})
# print(items[0].find("div", attrs = {"class": "name"}).get_text())

for item in items:

    # 광고 제품은 제외
    ad_badge = item.find("span", attrs={"class" : "ad-badge-text"})
    if ad_badge:
        print("광고 상품 제외합니다.")
        continue
    # 제품명
    name = item.find("div", attrs = {"class" : "name"}).get_text()

    # 애플 제품 제외
    if "Apple" in name:
        print(" <Apple 상품 제외합니다.> ")
    # 가격 정보
    price = item.find("strong", attrs = {"class" : "price-value"}).get_text() 
    
    # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회

    # 평점
    rate = item.find("em", attrs = {"class" : "rating"})
    if rate: 
        rate = rate.get_text()
    else: 
        print(" <평점 없는 상품 제외합니다.> ")
        continue

    # 평점수
    rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})
    if rate_cnt: 
        rate_cnt = rate_cnt.get_text() # 출력 예시: (26)
        rate_cnt = rate_cnt[1:-1] # 혹은 [1:3]까지 적어도 됨
        # print("리뷰 수:", rate_cnt)
    else: 
        print(" <평점 수 없는 상품 제외합니다.> ")
        continue    

    if float(rate) >= 4.5 and int(rate_cnt) >= 100 :
        print(name,price,rate,rate_cnt)
