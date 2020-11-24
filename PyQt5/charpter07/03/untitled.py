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
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 添加状态栏
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        # 向状态栏中添加控件
        self.label = QtWidgets.QLabel()
        self.label.setText("版权所有：吉林明日科技有限公司")
        # self.statusBar.addWidget(self.label)
        self.statusBar.addPermanentWidget(self.label)
        # 在状态栏中显示或删除临时信息
        self.statusBar.showMessage("当前登录用户： mr", 0)
        # 删除临时信息
        self.statusBar.clearMessage()

        # 在状态栏中显示实时当前时间
        timer = QtCore.QTimer(MainWindow)   # 创建一个qtimer计时器对象
        timer.timeout.connect(self.showtime)    # 发射timeout信号，与自定义槽函数关联
        timer.start()   # 启动计时器

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def showtime(self):
        datetime = QtCore.QDateTime.currentDateTime()   # 获取当前日期时间
        text = datetime.toString("yyyy-MM-dd HH:mm:ss") # 对日期时间进行格式化
        self.statusBar.showMessage("当前日期时间：" + text, 0)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
