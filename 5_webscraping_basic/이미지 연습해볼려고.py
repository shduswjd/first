import requests
from bs4 import BeautifulSoup
import re

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=&backgroundColor="
headers= {"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36" }
res = requests.get(url, headers = headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

laptops = soup.find_all("li", attrs = {"class" : re.compile("^search-product")})
# print(laptops[0].find("div", attrs = {"class" : "name"}).get_text())
images = soup.find_all("img", attrs = {"class" : "searc-product-wrap"})

for idx,image in images:
    image_url = image["src"]
    if image_url.startswith("//"):
        image_url = "http:" + image_url

    image_res = requests.get(image_url)
    image_res.raise_for_status()

    with open("couapang_laptop{}.jpg".format(idx), "wb") as couapngImage_file:
        couapngImage_file.write(image_res.content)
    if idx >= 4:
        break



# for laptop in laptops:
    
#     # 노트북 이름
#     name = laptop.find("div", attrs = {"class" : "name"}).get_text()
#     # 평점
#     rate= laptop.find("em", attrs = {"class" : "rating"}).get_text()
#     # 리뷰수
#     review = laptop.find("span", attrs = {"class" : "rating-total-count"}).get_text()
#     # 링크
#     link = laptop.find("a", attrs = {"class" : "search-product-link"})["href"]
#     # 이미지
#     image = laptop.find("img", attrs = {"class" : "search-product-wrap-img"})["src"]

#     # print(f"랭킹 : {rank}")
#     print("영화 이름 : ", name)
#     print("관객 수 : ", people)
#     print("---------------------------")


