import sys
import pyautogui
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        # 툴바 1 상세모드 ! --------------------------------------------------------
        toolbar_mode = QAction(QIcon('mode.png'), '상세모드', self)
        toolbar_mode.setShortcut('Ctrl+D')
        toolbar_mode.setStatusTip('상세 모드입니다.')

        self.toolbar = self.addToolBar('상세모드')
        self.toolbar.addAction(toolbar_mode)
        # ------------------------------------------------------------

        # 툴바 2 옵션 --------------------------------------------------------
        toolbar_option = QAction(QIcon('option.png'), '옵션', self)
        toolbar_option.setShortcut('Ctrl+O')
        toolbar_option.setStatusTip('자세한 옵션입니다.')

        self.toolbar = self.addToolBar('옵션')
        self.toolbar.addAction(toolbar_option)
        # ------------------------------------------------------------

        # 툴바 3 도움말 --------------------------------------------------------
        toolbar_help = QAction(QIcon('help.png'), '도움말', self)
        toolbar_help.setShortcut('Ctrl+Q')
        toolbar_help.setStatusTip('사용방법 입니다.')

        self.toolbar = self.addToolBar('도움말')
        self.toolbar.addAction(toolbar_help)
        # ------------------------------------------------------------

        # 라인입력 1 URL ----------------------------------------------------
        line_url = QLineEdit(self)
        line_url.setGeometry(10, 50, 570, 200)

        line_url.textChanged[str].connect(self.input_url)
        # -------------------------------------------------------------

        # 라벨 1 다운 경로 표시 ------------------------------------------------------------
        self.label_location = QLabel('다운로드 위치', self)
        self.label_location.setGeometry(10, 260, 200, 30)
        # ------------------------------------------------------------

        # 버튼 1 다운 경로 지정 ------------------------------------------------------------
        btn_fileload = QPushButton('다운로드 위치', self)
        btn_fileload.setGeometry(250, 260, 100, 30)

        btn_fileload.clicked.connect(self.dialog_load)
        # ------------------------------------------------------------

        # 콤보박스 1 포맷 설정 ------------------------------------------------------------
        combo_format = QComboBox(self)
        combo_format.addItem('mp3')
        combo_format.addItem('mp4')
        combo_format.addItem('mkv')
        combo_format.addItem('mp4-1080')
        combo_format.setGeometry(360, 260, 70, 30)

        combo_format.activated[str].connect(self.input_format)
        # ------------------------------------------------------------

        # 버튼 2 다운로드 ------------------------------------------------------------
        btn_download = QPushButton('다운로드 시작', self)
        btn_download.setGeometry(470, 260, 100, 30)

        btn_download.clicked.connect(self.dialog_down)
        # ------------------------------------------------------------


        # ------------------------------------------------------------


        # ------------------------------------------------------------


        self.setWindowTitle('AllDownloader')
        self.setGeometry(400, 400, 600, 400)
        self.show()


    # 이벤트 ----------------------------------------------
    def input_url(self, text):
        return
    # ----------------------------------------------------------------

    # 이벤트 파일 로드 ----------------------------------------------
    def dialog_load(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            pixmap = QPixmap(fname[0])
            self.label.append(QLabel())
            self.label[-1].setPixmap(pixmap.scaledToWidth(pixmap.width()*1.1))
            self.fname.append(fname[0])
            self.hbox_label.addWidget(self.label[-1])
    # ----------------------------------------------------------------

    # 이벤트 콤보 박스----------------------------------------------------------------
    def input_format(self, text):
        return
    # ----------------------------------------------------------------

    # 이벤트 다운 로드 ----------------------------------------------
    def dialog_down(self):
        return
    # ----------------------------------------------------------------





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
