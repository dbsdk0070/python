#DemoDB1.py
#SQLite를 사용하는 데모(로컬 데이터베이스)
import sqlite3

#처음에는 데이터베이스파일(또는 메모리)를 생성
con = sqlite3.connect(":memory:")  # : : 사이에 메모리를 임시로 저장한다. 작업끝나면 날라감
#SQL구문을 실행하는 것은 대부분 커서 객체
cur = con.cursor()
#저장소(테이블)을 만들기: 테이블스키마 뼈대구조만들기
cur.execute("create table PhoneBook (Name text, PhoneNum text);")
#1건 입력
cur.execute("insert into PhoneBook values ('derick', '010-111');")
#검색
cur.execute("select * from PhoneBook;") # select * : *는 모든 컬럼 몽땅 가져와라
for row in cur:
    print(row)