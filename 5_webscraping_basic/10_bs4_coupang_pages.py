
import requests
from bs4 import BeautifulSoup
import re

headers = {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}

for i in range(1, 6):
    print("현재 페이지: ", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)

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
            # print("광고 상품 제외합니다.")
            continue

        # 제품명
        name = item.find("div", attrs = {"class" : "name"}).get_text()

        # 애플 제품 제외
        if "Apple" in name:
            # print(" <Apple 상품 제외합니다.> ")
            continue

        # 가격 정보
        price = item.find("strong", attrs = {"class" : "price-value"}).get_text() 
        
        # 리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회

        # 평점
        rate = item.find("em", attrs = {"class" : "rating"})
        if rate: 
            rate = rate.get_text()
        else: 
            # print(" <평점 없는 상품 제외합니다.> ")
            continue

        # 평점수
        rate_cnt = item.find("span", attrs = {"class" : "rating-total-count"})
        if rate_cnt: 
            rate_cnt = rate_cnt.get_text() # 출력 예시: (26)
            rate_cnt = rate_cnt[1:-1] # 혹은 [1:3]까지 적어도 됨
        else: 
            # print(" <평점 수 없는 상품 제외합니다.> ")
            continue    

        link = item.find("a", attrs = {"class" : "search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_cnt) >= 100 :
            # print(name,price,rate,rate_cnt)
            print(f"제품명 : {name}")
            print(f"가격 : {price}")
            print(f"평점 : {rate}점, ({rate_cnt})개")
            print("바로가기: {}".format("http://www.coupang.com" + link))
            print("_"*100) #줄긋기
