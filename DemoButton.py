# DemoButton.py
#100%코드로만 작업: 디자인파일 + 로직파일
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class DemoWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        #버튼 인스턴스 추가
        btn1 = QPushButton("닫기", self)
        #왼쪽 상당(X축, Y축)
        btn1.move(50, 20)
        #시그널과 슬롯을 연결
        btn1.clicked.connect(QCoreApplication.instance().quit)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    demoWindow = DemoWindow()
    demoWindow.show()
    app.exec_() 