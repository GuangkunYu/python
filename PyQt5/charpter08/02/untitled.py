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

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 111, 41))
        self.pushButton.setObjectName("pushButton")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 761, 511))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.binList)

    def binList(self):
        """
        定义槽函数：用来使用qfiledialog类创建一个文件对话框，在该文件对话框中可以设置选择多个文件，并且只能显示图片文件，
        选择完之后，会将选择的文件显示到listwidget列表中
        :return:
        """
        from PyQt5.QtWidgets import QFileDialog
        # dir = QFileDialog()  # 创建文件对话框
        # dir.setFileMode(QFileDialog.ExistingFiles)  # 设置多选
        # dir.setDirectory('C:\\')  # 设置初始路径为C盘
        # dir.setNameFilter('图片文件(*.jpg *.png *.bmp *.ico *.gif)')  # 设置值显示图片文件
        # if dir.exec_():  # 判断是否选择了文件
        #     self.listWidget.addItems(dir.selectedFiles())  # 将选择的文件显示到列表中

        files, filetype = QFileDialog.getOpenFileNames(None, '打开', 'C:\\', '图片文件(*.jpg *.png *.bmp *.ico *.gif)')
        self.listWidget.addItems(files)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "选择文件"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
