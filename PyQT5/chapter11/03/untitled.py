# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFile, QFileInfo, QIODevice, QTextStream
import os
import datetime


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 分组框
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 781, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(0, 0, 255);")
        self.groupBox.setObjectName("groupBox")

        # 选择文件标签
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 40, 90, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")

        # 显示选择的文件路径
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(120, 40, 530, 31))
        self.lineEdit.setObjectName("lineEdit")

        # 点击选择按钮
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(670, 40, 93, 31))
        self.pushButton.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton.setObjectName("pushButton")

        # 输入创建路径标签
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 132, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_2.setObjectName("label_2")

        # 输入创建路径的文本框
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(150, 110, 500, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")

        # 创建按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 110, 93, 31))
        self.pushButton_2.setStyleSheet("color: rgb(0, 0, 0);")
        self.pushButton_2.setObjectName("pushButton_2")

        # 显示创建的文件列表及大小
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 180, 781, 411))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        # 设置第一列的标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("文件名")
        self.tableWidget.setColumnWidth(0, 200)
        # 设置第二列
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("文件大小")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.getfile)
        self.pushButton_2.clicked.connect(self.getpath)

    def getfile(self):
        dir = QFileDialog()
        dir.setDirectory("c:\\")
        dir.setNameFilter('文本文件(*.txt)')
        if dir.exec_():
            self.lineEdit.setText(dir.selectedFiles()[0])

    def getpath(self):
        try:
            path = self.lineEdit_2.text()
            if self.lineEdit_2.text() != "":
                list = []
                file = QFile(self.lineEdit.text())
                if file.open(QIODevice.ReadOnly):
                    read = QTextStream(file)
                    read.setCodec('utf-8')
                    while not read.atEnd():
                        list.append(read.readLine())
                if not os.path.exists(path):
                    os.makedirs(path)
                for i in range(len(list)):
                    mytime = str(datetime.datetime.utcnow().strftime("%Y%m%d%H%M%S"))
                    files = path + mytime + str(i) + ".txt"
                    file = QFile(files)
                    file.open(QIODevice.ReadWrite | QIODevice.Text)
                    file.write(bytes(list[i], encoding="utf8"))
                    file.close()
                filelist = os.listdir(path)
                flag = 0
                for f in filelist:
                    file = QFileInfo(f)
                    if file.fileName().endswith(".txt"):
                        self.tableWidget.insertRow(flag)
                        self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(file.fileName()))
                        self.tableWidget.setItem(flag, 1, QtWidgets.QTableWidgetItem(str(file.size()) + "B"))
                        flag += 1
        except Exception as e:
            print(e)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "将现有问题存放到不同的文件中"))
        self.groupBox.setTitle(_translate("MainWindow", "基础设置"))
        self.label.setText(_translate("MainWindow", "选择文件："))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.label_2.setText(_translate("MainWindow", "输入创建路径："))
        self.pushButton_2.setText(_translate("MainWindow", "创建"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())