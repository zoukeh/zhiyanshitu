from PyQt5 import QtCore, QtWidgets
import sys


##########################################
# ui界面设置
class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        # 主窗口参数设置
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(848, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 设置按键参数
        self.file = QtWidgets.QPushButton(self.centralwidget)
        self.file.setGeometry(QtCore.QRect(57, 660, 175, 28))
        self.file.setObjectName("file")
        self.file.setStyleSheet("background-color:rgb(111,180,219)")
        self.file.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        # 设置显示窗口参数
        self.fileT = QtWidgets.QPushButton(self.centralwidget)
        self.fileT.setGeometry(QtCore.QRect(300, 660, 480, 28))
        self.fileT.setObjectName("file")
        self.fileT.setStyleSheet("background-color:rgb(111,180,219)")
        self.fileT.setStyleSheet(
            "QPushButton{background-color:rgb(111,180,219)}"  # 按键背景色
            "QPushButton:hover{color:green}"  # 光标移动到上面后的前景色
            "QPushButton{border-radius:6px}"  # 圆角半径
            "QPushButton:pressed{background-color:rgb(180,180,180);border: None;}"  # 按下时的样式
        )

        # 主窗口及菜单栏标题栏设置
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 848, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ################button按钮点击事件回调函数################

        self.file.clicked.connect(self.msg)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deecamp_Eurus"))
        self.file.setText(_translate("MainWindow", "选择文件"))
        self.fileT.setText(_translate("MainWindow", ""))

    #########选择图片文件夹#########

    def msg(self, Filepath):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.fileT.setText(m)

