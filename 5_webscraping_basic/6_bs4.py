import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday"
res=requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title) #<title>네이버 만화 &gt; 요일별  웹툰 &gt; 전체웹툰</title>
# print(soup.title.get_text()) #네이버 만화 > 요일별  웹툰 > 전체웹툰
# print(soup.a) : soup객체에서 처음 발견되는 a element 출력
# print(soup.a.get_text()) # 메인 메뉴로 바로가기
# print(soup.a.attrs) # attrs : a element의 속성정보를 출력
# {'href': '#menu', 'onclick': "document.getElementById('menu').tabIndex=-1;document.getElementById('menu').focus();return false;"}
# print(soup.a["href"]) # ["(속성)"] : a element 의 href 속성 '값'정도를 출력 
# menu


print(soup.find("a", attrs = {"class" : "Nbtn_upload"}))
# class = "Nbtn_upload"인 a element를 찾아줘
print(soup.find(attrs = {"class" : "Nbtn_upload"}))
# class" = "Nbtn_upload"인 어떤 element를 찾아줘
# 어차피 웹툰 올리기의 버튼은 한개밖에 없어서 a태그를 안써줘도 출력은 같음

# print(soup.find("li", attrs = {"class" : "rank01" }))
rank1 = soup.find("li", attrs = {"class" : "rank01" })
print(rank1.a.get_text()) #여신강림-173화
print(rank1.next_sibling.next_sibling) #다음 랭킹 rank2
rank2 = rank1.next_sibling.next_sibling
rank3 = rank2.next_sibling.next_sibling
print(rank3.a.get_text())

rank2 = rank3.previous_sibling.previous_sibling
print(rank2.a.get_text())

#부모
print(rank1.parent)

rank2 = rank1.find_next_sibling("li")
print(rank2.a.get_text())

rank3 = rank2.find_next_sibling("li")
print(rank3.a.get_text())

rank2 = rank3.find_previous_sibling("li")
print(rank2.a.get_text())

ranks = rank1.find_next_siblings("li")

webtoon = soup.find("a", text = "여신강림-173화")
print(webtoon)

