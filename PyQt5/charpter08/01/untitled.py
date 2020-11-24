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
        MainWindow.resize(851, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(320, 60, 161, 41))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 140, 161, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 220, 161, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(320, 300, 161, 41))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(320, 380, 161, 41))
        self.pushButton_5.setObjectName("pushButton_5")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.info)
        self.pushButton_2.clicked.connect(self.warn)
        self.pushButton_3.clicked.connect(self.question)
        self.pushButton_4.clicked.connect(self.critical)
        self.pushButton_5.clicked.connect(self.about)

    def info(self):
        select = QtWidgets.QMessageBox.information(None, '消息', '这是一个消息对话框',
                                                   QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if select == QtWidgets.QMessageBox.Yes:
            QtWidgets.QMessageBox.information(MainWindow, '提醒', '您同意了本次请求...')

    def warn(self):
        QtWidgets.QMessageBox.warning(None, '警告', '这是一个警告对话框', QtWidgets.QMessageBox.Ok)

    def question(self):
        QtWidgets.QMessageBox.question(None, '问答', '这是一个问答对话框', QtWidgets.QMessageBox.Ok)

    def critical(self):
        QtWidgets.QMessageBox.critical(None, '错误', '这是一个错误对话框', QtWidgets.QMessageBox.Ok)

    def about(self):
        QtWidgets.QMessageBox.about(None, '关于', '这是一个关于对话框')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "消息框"))
        self.pushButton_2.setText(_translate("MainWindow", "警告框"))
        self.pushButton_3.setText(_translate("MainWindow", "问答框"))
        self.pushButton_4.setText(_translate("MainWindow", "错误框"))
        self.pushButton_5.setText(_translate("MainWindow", "关于框"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
