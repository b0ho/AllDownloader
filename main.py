import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *

# 메인 윈도우 폼
form_class = uic.loadUiType("mainwindow.ui")[0]


class MyWindow(QMainWindow, form_class):
    # 초기화
    def __init__(self):
        super().__init__()
        self.setUi()


    # Ui 로드
    def setUi(self):
        self.setupUi(self)

        # 버튼-위치 에 대한 이벤트 연결
        self.btn_location.clicked.connect(self.btn_loc_clicked)

        #


    # 버튼-위치 이벤트
    def btn_loc_clicked(self):
        print("ss")
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])



# 프로그램 실행
if __name__ == "__main__":
    print("start")
    app = QApplication(sys.argv)
    myApp = MyWindow()
    myApp.show()
    app.exec_()