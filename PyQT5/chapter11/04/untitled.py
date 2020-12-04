# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDir
import os


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 41))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 20, 571, 41))
        self.lineEdit.setObjectName("lineEdit")

        # 确定按钮，根据判断输入路径是否存在，如果不存在，则创建，如果存在，获取其中的所有文件夹
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(700, 20, 93, 41))
        self.pushButton.setObjectName("pushButton")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 781, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("路径")
        self.tableWidget.verticalHeader().setVisible(False) # 隐藏垂直标题栏
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch) # 设置自动填充容器

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 550, 170, 41))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 550, 410, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(610, 550, 93, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(712, 550, 81, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.getpath)
        self.pushButton_2.clicked.connect(self.rename)
        self.pushButton_3.clicked.connect(self.delete)
        self.tableWidget.itemClicked.connect(self.getItem)

    def getItem(self, item):
        self.select = item.text()

    def getpath(self):
        self.tableWidget.setRowCount(0)
        path = self.lineEdit.text()
        if path != "":
            dir = QDir()
            if not dir.exists(path):
                dir.mkdir(path)
            dir = QDir(path)
            flag = 0
            for d in dir.entryList(QDir.Dirs | QDir.NoDotAndDotDot):
                self.tableWidget.insertRow(flag)
                self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(os.path.join(path, d)))
                flag += 1

    def rename(self):
        newname = self.lineEdit_2.text()
        if newname != "":
            if self.select != "":
                dir = QDir()
                dir.rename(self.select, os.path.join(self.lineEdit.text(), newname))
                QtWidgets.QMessageBox.information(MainWindow, '提示', '重命名文件夹成功！')
                self.getpath()

    def delete(self):
        if self.select != "":
            dir = QDir()
            dir.rmdir(self.select)
            QtWidgets.QMessageBox.information(MainWindow, '提示', '删除文件夹成功！')
            self.getpath()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QDir应用"))
        self.label.setText(_translate("MainWindow", "输入路径："))
        self.pushButton.setText(_translate("MainWindow", "确定"))
        self.label_2.setText(_translate("MainWindow", "设置新文件夹名称："))
        self.pushButton_2.setText(_translate("MainWindow", "重命名"))
        self.pushButton_3.setText(_translate("MainWindow", "删除"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())