import sys
import os.path
from PyQt5.QtWidgets import *
import csv
import atexit
import mainwindow

csv_name = "option.csv"


class Alldownloader(QMainWindow, mainwindow.Ui_MainWindow):
    # 옵션을 위한 변수들
    opt_loc = ""
    opt_sub = False
    opt_format = ""
    options = []

    # 초기화
    def __init__(self):
        print("초기화")
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOption()
        self.setUi()

        # 프로그램 종료 시 수행 기능
        def func_exit():
            print("프로그램 종료", opt_sub)

            f = open("tmp", "w", encoding="utf-8", newline="")
            wr = csv.writer(f)
            # 생성할 기본 옵션 값들
            wr.writerow([opt_loc, opt_sub, opt_format])
            f.close()
            os.rename("tmp", csv_name)

            #
            f = open(csv_name, "r", encoding="utf-8")
            rdr = csv.reader(f)
            for line in rdr:
                print(line)
            f.close()

        # 프로그램 종료시 실행
        atexit.register(func_exit)

    # 옵션 파일 생성 or 로드
    def setOption(self):
        global opt_loc, opt_sub, opt_format, options

        # 옵션 파일이 있을 경우 로드
        if os.path.exists(csv_name):
            print("옵션파일 존재함")
            f = open(csv_name, "r", encoding="utf-8")
            rdr = csv.reader(f)

            for line in rdr:
                options = line
                print(line, options)

            opt_loc = options[0]
            opt_sub = options[1]
            opt_format = options[2]

            print(opt_loc, opt_sub, opt_format)

            f.close()

        # 옵션 파일이 없을 경우 생성
        else:
            print("옵션파일 없음 새로 생성")
            f = open(csv_name, "w", encoding="utf-8", newline="")
            wr = csv.writer(f)
            # 생성할 기본 옵션 값들
            wr.writerow(["/users/ybg4828/Downloads/", True, "mp3"])
            f.close()

    # Ui 로드
    def setUi(self):
        print("setUi 실행")
        if opt_sub == True:
            self.chbx_subtitle = True
        else:
            self.chbx_subtitle = False

    # 툴바-옵션 이벤트
    def tbr_opt_clicked(self):
        print("옵션 화면 실행")

    # 툴바-도움말 이벤트
    def tbr_help_clicked(self):
        print("도움말 화면 실행")

    # 텍스트-URL 이벤트
    def text_url_input(self):
        print("url 입력됨")

    # 버튼-위치 이벤트
    def btn_loc_clicked(self):
        print("fileDialog 오픈")
        fname = QFileDialog.getOpenFileName(self)
        self.label.setText(fname[0])

    # 체크박스-자막 이벤트
    def chbx_sub_clicked(self):
        global opt_sub
        if self.chbx_subtitle.isChecked() == True:
            print("자막 선택")
            opt_sub = True
        else:
            print("자막 선택 해제")
            opt_sub = False

    # 콤보박스-포맷 이벤트
    def cmbx_format_choiced(self):
        print("포맷 결정함")

    # 버튼-다운시작 이벤트
    def btn_down_clicked(self, event):
        print("다운 확인 다이얼 오픈")
        reply = QMessageBox.question(
            self,
            "다운시작",
            "다운로드를 시작하시겠습니까?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )
        if reply == QMessageBox.Yes:
            self.func_down()
            # event.accept()
        else:
            print("취소")
            # event.ignore()

    # 다운로드 수행 기능
    def func_down(self):
        print("다운로드 시작")


# 프로그램 실행
if __name__ == "__main__":
    print("main 실행")
    app = QApplication(sys.argv)
    myApp = Alldownloader()
    myApp.show()
    app.exec_()
