# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/ybg4828/work/AllDownloader/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 10)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.text_url = QtWidgets.QTextEdit(self.centralwidget)
        self.text_url.setObjectName("text_url")
        self.horizontalLayout_2.addWidget(self.text_url)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 10, 0, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_location = QtWidgets.QLabel(self.centralwidget)
        self.label_location.setMinimumSize(QtCore.QSize(230, 0))
        self.label_location.setObjectName("label_location")
        self.horizontalLayout.addWidget(self.label_location)
        self.btn_location = QtWidgets.QToolButton(self.centralwidget)
        self.btn_location.setMinimumSize(QtCore.QSize(50, 0))
        self.btn_location.setToolTip("")
        self.btn_location.setWhatsThis("")
        self.btn_location.setObjectName("btn_location")
        self.horizontalLayout.addWidget(self.btn_location)
        self.chbx_subtitle = QtWidgets.QCheckBox(self.centralwidget)
        self.chbx_subtitle.setMaximumSize(QtCore.QSize(60, 16777215))
        self.chbx_subtitle.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.chbx_subtitle.setObjectName("chbx_subtitle")
        self.horizontalLayout.addWidget(self.chbx_subtitle)
        self.cmbx_format = QtWidgets.QComboBox(self.centralwidget)
        self.cmbx_format.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmbx_format.setObjectName("cmbx_format")
        self.cmbx_format.addItem("")
        self.cmbx_format.addItem("")
        self.cmbx_format.addItem("")
        self.cmbx_format.addItem("")
        self.cmbx_format.addItem("")
        self.horizontalLayout.addWidget(self.cmbx_format)
        self.btn_download = QtWidgets.QPushButton(self.centralwidget)
        self.btn_download.setObjectName("btn_download")
        self.horizontalLayout.addWidget(self.btn_download)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setMinimumSize(QtCore.QSize(700, 50))
        self.toolBar.setInputMethodHints(QtCore.Qt.ImhNone)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.option = QtWidgets.QAction(MainWindow)
        self.option.setObjectName("option")
        self.help = QtWidgets.QAction(MainWindow)
        self.help.setObjectName("help")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.option)
        self.toolBar.addAction(self.help)

        self.retranslateUi(MainWindow)
        self.btn_location.clicked.connect(MainWindow.btn_loc_clicked)
        self.btn_download.clicked.connect(MainWindow.btn_down_clicked)
        self.cmbx_format.currentIndexChanged["QString"].connect(
            MainWindow.cmbx_format_choiced
        )
        self.chbx_subtitle.toggled["bool"].connect(MainWindow.chbx_sub_clicked)
        self.text_url.textChanged.connect(MainWindow.text_url_input)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_location.setText(_translate("MainWindow", "다운로드 경로가 여기에 표시됩니다.!"))
        self.btn_location.setText(_translate("MainWindow", "위치"))
        self.chbx_subtitle.setText(_translate("MainWindow", "자막"))
        self.cmbx_format.setItemText(0, _translate("MainWindow", "mp3"))
        self.cmbx_format.setItemText(1, _translate("MainWindow", "mp4"))
        self.cmbx_format.setItemText(2, _translate("MainWindow", "원본"))
        self.cmbx_format.setItemText(3, _translate("MainWindow", "mp4[고화질]"))
        self.cmbx_format.setItemText(4, _translate("MainWindow", "mp4[저화질]"))
        self.btn_download.setText(_translate("MainWindow", "다운로드 시작"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.option.setText(_translate("MainWindow", "옵션"))
        self.help.setText(_translate("MainWindow", "도움말"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
