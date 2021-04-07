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

#입력 파라메터 처리
#텍스트박스(GUI, Web Page)에서 입력을 받아서 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNumber))
#다중의 레코드(행, row)를 입력받는 경우: 2차원 행열데이터(0행의 0열, 0행의 1열...)
datalist = (("tom", "010-123"),("dsp", "010-567")) #list안에 list가 들어가있음
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

#검색
cur.execute("select * from PhoneBook;") # select * : *는 모든 컬럼 몽땅 가져와라
for row in cur:
    print(row)