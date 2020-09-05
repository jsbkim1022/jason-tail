# beautifulsoup4
# lxml

import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title.get_text())
# print(soup.a) #soup 에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # element attrs
# print(soup.a["href"]) # get href text from element

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) # find
# print(soup.find(attrs={"class": "Nbtn_upload"}))

# print(soup.find("li", attrs={"class": "rank01"}))
rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a)
# print(rank1.a.get_text())
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling
# print(rank2.a.get_text())

# rank2 = rank1.find_next_sibling("li")
# rank1 = rank2.find_previous_sibling("li")
# print(rank2.a.get_text())

ranks = rank1.find_next_siblings("li")

webtoon = soup.find("a", text="열렙전사-2부 58화 - 유다의 혀 (2)")
print(webtoon)