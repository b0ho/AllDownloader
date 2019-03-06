import sys
import subprocess
import os.path
from PyQt5.QtWidgets import *
import csv
import getpass
import atexit
import main_window
from PyQt5 import uic

csv_name = "option.csv"

form_class = uic.loadUiType("mainwindow.ui")[0]

#class Alldownloader(QMainWindow, main_window.Ui_MainWindow):

class Alldownloader(QMainWindow, form_class):
    # 옵션을 위한 변수들
    opt_loc = ""
    opt_sub = 0
    opt_format = ""
    options = []
    os_name = 1

    # 초기화
    def __init__(self):
        print("초기화")
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setOS()
        self.setOption()
        self.setUi()

        # 프로그램 종료 시 수행 기능
        def func_exit():
            global opt_loc, opt_sub, opt_format
            print("프로그램 종료", opt_sub)

            os.remove(csv_name)
            f = open(csv_name, "w", encoding="utf-8", newline="")
            wr = csv.writer(f)
            # 생성할 기본 옵션 값들
            wr.writerow([opt_loc, opt_sub, opt_format])
            f.close()

            #
            f = open(csv_name, "r", encoding="utf-8")
            rdr = csv.reader(f)
            for line in rdr:
                print(line)
            f.close()

        # 프로그램 종료시 실행
        atexit.register(func_exit)

    # 윈도우 인지 맥 인지 확인
    def setOS(self):
        global os_name
        if os.name == 'nt':
            os_name = 0
            print("윈도우입니다.")
        else:
            os_name = 1
            print("맥 입니다.")

    # 옵션 파일 생성 or 로드
    def setOption(self):
        global opt_loc, opt_sub, opt_format, options, os_name

        # 옵션 파일이 있을 경우 로드
        if os.path.exists(csv_name):
            print("옵션파일 존재함")
            f = open(csv_name, "r", encoding="utf-8")
            rdr = csv.reader(f)

            for line in rdr:
                options = line

            opt_loc = options[0]
            opt_sub = options[1]
            opt_format = options[2]

            print(options)

            f.close()

        # 옵션 파일이 없을 경우 생성
        else:
            print("옵션파일 없음 새로 생성")

            loc_win = "C:/Users/" + getpass.getuser() + "/Downloads/"
            loc_mac = "/users/" + getpass.getuser() + "/Downloads/"
            loc = loc_win if (os_name == 0) else loc_mac

            f = open(csv_name, "w", encoding="utf-8", newline="")
            wr = csv.writer(f)
            # 생성할 기본 옵션 값들
            wr.writerow([loc, 0, "mp3"])
            f.close()

    # Ui 로드
    def setUi(self):
        global opt_sub, opt_loc
        print("setUi 실행 - 가져온 옵션 값으로 프로그램을 세팅")

        # 자막 체크 여부확인 및 결정
        if int(opt_sub) is 1:
            print("opt_sub = ", opt_sub, "자막 옵션 켜짐")
            self.chbx_subtitle.setChecked(True)
        else:
            print("opt_sub = ", opt_sub, "자막 옵션 꺼짐")
            self.chbx_subtitle.setChecked(False)

        # 경로 확인
        self.label_location.setText(opt_loc)

    # 툴바-옵션 이벤트
    def tbr_opt_clicked(self):
        print("옵션 화면 실행")

    # 툴바-도움말 이벤트
    def tbr_help_clicked(self):
        print("도움말 화면 실행")

    # 버튼-위치 이벤트
    def btn_loc_clicked(self):
        global opt_loc
        print("fileDialog 오픈")
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.label_location.setText(fname)
        opt_loc = fname+"/"

    # 체크박스-자막 이벤트
    def chbx_sub_clicked(self):
        global opt_sub
        if self.chbx_subtitle.isChecked() == True:
            print("자막 선택")
            opt_sub = 1
        else:
            print("자막 선택 해제")
            opt_sub = 0

    # 콤보박스-포맷 이벤트
    def cmbx_format_choiced(self):
        print("포맷 결정함", self.cmbx_format.setText)


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
            n = "https://www.youtube.com/watch?v=eTIOh7vhdN8"
            print(
                "테스트",
                os.system(

                    'youtube-dl --extract-audio --audio-format mp3 -o "' + opt_loc + '%(title)s.%(ext)s" "' + n + '"'
                    # 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o "'+opt_loc+'%(title)s.%(ext)s" "'+n+'"'
                    # 'youtube-dl --extract-audio --audio-format mp3 -o "/Users/', getpass.getuser(),'/Downloads/%(title)s.%(ext)s" "', n, '"',
                    # mac 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o "/Users/ybg4828/Downloads/%(title)s.%(ext)s" "https://www.youtube.com/watch?v=eTIOh7vhdN8"'

                )
            )
            # event.ignore()

    # 다운로드 수행 기능
    def func_down(self):
        print("다운로드 시작")

        # text로부터 url 배열 생성
        text = self.text_url.toPlainText()
        urls = text.splitlines()
        while "" in urls:
            urls.remove("")
        print(urls)

        # 가져온 url로부터 명령어 생성
        for n in urls:
            url = 'youtube-dl --extract-audio --audio-format mp3 -o "' + opt_loc + '%(title)s.%(ext)s" "' + n + '"'
            # 'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o "'+opt_loc+'%(title)s.%(ext)s" "'+n+'"'
            print(url)

            print(
                os.system(url)

                #'youtube-dl --extract-audio --audio-format mp3 -o "/Users/',getpass.getuser(),'/Downloads/%(title)s.%(ext)s" "',n,'"',
                #'youtube-dl -f "bestvideo[ext=mp4]+bestaudio[ext=m4a]" -o "/Users/'+ getpass.getuser()+ '/Downloads/%(title)s.%(ext)s" "' + n+ '"'
                # youtube-dl -f "bestvideo+bestaudio" --merge-output-format "mkv" -o "C:/Users/ybg48/Downloads/%(title)s.%(ext)s" --sub-lang ko ""
            )
            # https://www.youtube.com/watch?v=eTIOh7vhdN8
            # cmd = ["powershell.exe","Start-Process","youtube-dl","/Users/ybg4828/work/Alldownloader/youtube-dl-master/bin/youtube-dl","-Verb","runAs",]
            # print(subprocess.run(cmd, shell=True))



# 프로그램 실행
if __name__ == "__main__":
    print("main 실행")
    app = QApplication(sys.argv)
    myApp = Alldownloader()
    myApp.show()
    app.exec_()
