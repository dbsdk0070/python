#web2.py
#웹서버에 요청
import urllib.request
#크롤링에 필요
from bs4 import BeautifulSoup

#웹서버에 요청해서 결과물을 문자열로 받기
#패키지명. 모듈명. 함수명

#검색이 용이한 객체
soup = BeautifulSoup(data, "html")

#다중라인주석 처리: ctrl + /
#<td class="title">
#<a href="/webtoon/detail.nhn">마음의 소리 49화 <지혜></a>
#</td>