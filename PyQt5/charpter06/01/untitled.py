# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(796, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 150, 300, 50))
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)  # 设置进度条的布局方向
        self.progressBar.setProperty("value", -1)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)   # 设置对齐方式
        self.progressBar.setTextVisible(True)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)   # 设置进度条的显示方向
        self.progressBar.setTextDirection(QtWidgets.QProgressBar.TopToBottom)   # 设置进度条文本显示方向
        self.progressBar.setFormat("")
        self.progressBar.setObjectName("progressBar")

        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(250, 400, 300, 50))
        self.progressBar_2.setLayoutDirection(QtCore.Qt.RightToLeft)  # 设置进度条的布局方向
        self.progressBar_2.setProperty("value", -1)
        self.progressBar_2.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignHCenter)
        self.progressBar_2.setTextVisible(True)
        self.progressBar_2.setOrientation(QtCore.Qt.Horizontal)  # 设置进度条的显示方向
        self.progressBar_2.setTextDirection(QtWidgets.QProgressBar.TopToBottom)  # 设置进度条文本显示方向
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")

        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(200, 150, 50, 300))
        self.progressBar_3.setLayoutDirection(QtCore.Qt.LeftToRight)  # 设置进度条的布局方向
        self.progressBar_3.setProperty("value", -1)
        self.progressBar_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.progressBar_3.setTextVisible(True)
        self.progressBar_3.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_3.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_3.setObjectName("progressBar_3")

        self.progressBar_4 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_4.setGeometry(QtCore.QRect(550, 150, 50, 300))
        self.progressBar_4.setLayoutDirection(QtCore.Qt.LeftToRight)  # 设置进度条的布局方向
        self.progressBar_4.setProperty("value", -1)
        self.progressBar_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.progressBar_4.setTextVisible(True)
        self.progressBar_4.setOrientation(QtCore.Qt.Vertical)
        self.progressBar_4.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.progressBar_4.setObjectName("progressBar_4")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(330, 500, 150, 50))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 796, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.running)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # 创建计时器对象
        self.timer = QtCore.QBasicTimer()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "跑马灯效果"))
        self.pushButton.setText(_translate("MainWindow", "开始"))

    def running(self):
        """
        定义槽函数：控制进度条滚动效果
        :return:
        """
        # 判断计时器是否开启
        if self.timer.isActive():
            self.timer.stop()   # 停止计时器
            self.pushButton.setText("开始")
            # 设置4个进度条的最大值为100
            self.progressBar.setMaximum(100)
            self.progressBar_2.setMaximum(100)
            self.progressBar_3.setMaximum(100)
            self.progressBar_4.setMaximum(100)
        else:
            # 启动计时器
            self.timer.start(100, MainWindow)
            self.pushButton.setText('停止')
            # 将4个进度条的最大值和最小值都设置为0，以便显示循环滚动效果
            self.progressBar.setMaximum(0)
            self.progressBar.setMinimum(0)
            self.progressBar_2.setMaximum(0)
            self.progressBar_2.setMinimum(0)
            self.progressBar_3.setMaximum(0)
            self.progressBar_3.setMinimum(0)
            self.progressBar_4.setInvertedAppearance(True)
            self.progressBar_4.setMaximum(0)
            self.progressBar_4.setMinimum(0)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
