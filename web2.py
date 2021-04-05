#web2.py
#웹서버에 요청
import urllib.request
#크롤링에 필요
from bs4 import BeautifulSoup

#웹서버에 요청해서 결과물을 문자열로 받기
#패키지명. 모듈명. 함수명
data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
#검색이 용이한 객체
soup = BeautifulSoup(data, "html.perser")

#다중라인주석 처리: ctrl + /
#<td class="title">
#   <a href="/webtoon/detail.nhn">마음의 소리 49화 <지혜></a>       #실제 웹툰의 주소
#</td>
#리스트 객체를 리턴(갯수 10개)cartoons[0], cartoons[1]....
cartoons = soup.find("td", class_="title")
#첫번째만 슬라이싱(10개)
title = cartoons[0].find("a").text
link = cartoons[0].find("a")["href"]
print(title)
print(link)

#반복구문
print("=====반복구문=====")
for item in cartoons:
    title = item.find("a").text
    print(title)

