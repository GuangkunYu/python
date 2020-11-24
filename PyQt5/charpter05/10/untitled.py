# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 160, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(200, 230, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(290, 160, 140, 40))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(290, 230, 140, 40))
        # 设置文本框为密码
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        # 设置只能输入8位数字
        self.lineEdit_2.setValidator(QtGui.QIntValidator(1000000, 99999999))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(200, 300, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        # 设置管理员单选按钮默认选中
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(320, 299, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 360, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 360, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # 为登录按钮的clicked信号绑定自定义槽函数
        self.pushButton.clicked.connect(self.login)
        # 为退出按钮的clicked信号绑定MainWindow窗口自带的close槽函数
        self.pushButton_2.clicked.connect(MainWindow.close)
        # 为单选按钮的toggled信号绑定自定义槽函数
        self.radioButton.toggled.connect(self.select)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "系统登录"))
        self.label.setText(_translate("MainWindow", "用户名："))
        self.label_2.setText(_translate("MainWindow", "密  码："))
        self.radioButton.setText(_translate("MainWindow", "管理员"))
        self.radioButton_2.setText(_translate("MainWindow", "普通用户"))
        self.pushButton.setText(_translate("MainWindow", "登录"))
        self.pushButton_2.setText(_translate("MainWindow", "重置"))

    def login(self):
        """
        自定义登录槽函数，使用information方法弹出信息提示框
        :return:
        """
        QMessageBox.information(MainWindow, "登录信息", "用户名：" + self.lineEdit.text() +
                                "密码：" + self.lineEdit_2.text(), QMessageBox.Ok)

    def select(self):
        """
        自定义槽函数，用来判断用户登录身份
        :return:
        """
        if self.radioButton.isChecked():
            QMessageBox.information(MainWindow, "提示", "您选择的是 管理员 登录", QMessageBox.Ok)
        elif self.radioButton_2.isChecked():
            QMessageBox.information(MainWindow, "提示", "您选择的是 普通用户 登录", QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
