import sys
from PyQt5.QtWidgets import *
import urllib.request
from bs4 import BeautifulSoup
import webbrowser   #브라우저로 넘기는 경우 
import re 

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #창의 시작위치와 폭, 높이(x,y,width,height) 
        self.setGeometry(200, 200, 800, 800)
        
        #입력 텍스트 : TextBox, <Input type="text">
        self.lineEdit = QLineEdit("아이폰", self)
        self.lineEdit.move(20, 20)

        #버튼
        self.btn = QPushButton("검색", self)
        self.btn.move(120, 20)
        #버튼 clicked시그널(이벤트) --> setTableWidgetData메서드(슬롯)
        self.btn.clicked.connect(self.setTableWidgetData)

        #다중의 행과 열(엑셀) : 웹페이지<table><tr><td>...</td></tr><table>
        #       0열    1열    (컬럼 2개)
        #0행   (0,0)  (0,1)    (행,열)
        #1행   (1,0)  (1,1)
        #2행   (2,0)  (2,1)
        #3행 2열 --> 6개의 셀이 있는 2차원 배열
    
        self.tableWidget = QTableWidget(self)
        self.tableWidget.move(20, 70)
        self.tableWidget.resize(800, 600)
        self.tableWidget.setRowCount(50)  #행의 갯수 
        self.tableWidget.setColumnCount(2)  #컬럼의 갯수 
        #컬럼의 폭을 지정한다. 0번 1번 
        self.tableWidget.setColumnWidth(0, 300)
        self.tableWidget.setColumnWidth(1, 300)
        
        #self.setTableWidgetData()
        #컨트롤. 시그널명 --> doubleClicked 슬롯메서드 연결
        self.tableWidget.doubleClicked.connect(self.doubleClicked)

    def setTableWidgetData(self):
        #사용자가 어떤 행을 클릭했는지를 검색해서 웹브라우저로 보내기
        row = 0
        #User-Agent를 조작하는 경우 
        hdr = {'User-agent':'Mozila/5.0 (compatible; MSIE 5.5; Windows NT)'}
        for n in range(0,5):
            #클리앙의 중고장터 주소 
            data ='https://www.clien.net/service/board/sold?&od=T31&po=' + str(n)
            req = urllib.request.Request(data, 
                headers = hdr)
            data = urllib.request.urlopen(req).read()
            page = data.decode('utf-8', 'ignore')
            soup = BeautifulSoup(page, 'html.parser')
            list = soup.find_all('a', attrs={'class':'list_subject'})

            f = open("clien.txt", "a+", encoding="utf-8")
            for item in list:
                try:
                    span = item.contents[3]
                    title = item.text.strip()
                    #라인에디터에 입력된 문자열 받아서 검색
                    if (re.search(self.lineEdit.text(), title)):
                        title = title.replace("\t", "")
                        title = title.replace("\n", "")
                        print(title)
                        link = 'https://www.clien.net'  + item['href'] 
                        print(link.strip())
                        f.write(title+"\n")
                        f.write(link + "\n")
                        #행데이터로 출력 
                        self.tableWidget.setItem(row, 0, QTableWidgetItem(title))
                        self.tableWidget.setItem(row, 1, QTableWidgetItem(link))
                        row += 1
                        print("row: ", row) 
                except:
                    pass
             
            f.close()

    def doubleClicked(self):
        url = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()
        webbrowser.open(url) 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = Form()
    mywindow.show()
    app.exec_()



