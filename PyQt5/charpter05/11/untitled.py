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
        MainWindow.resize(531, 464)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(160, 130, 91, 19))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(160, 180, 91, 19))
        self.checkBox_2.setObjectName("checkBox_2")

        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(160, 230, 91, 19))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(300, 130, 91, 19))
        self.checkBox_4.setObjectName("checkBox_4")

        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(300, 180, 91, 19))
        self.checkBox_5.setObjectName("checkBox_5")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 300, 93, 28))
        self.pushButton.setObjectName("pushButton")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 531, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.getvalue)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "设置用户权限"))
        self.checkBox.setText(_translate("MainWindow", "基本信息管理"))
        self.checkBox_2.setText(_translate("MainWindow", "销售管理"))
        self.checkBox_3.setText(_translate("MainWindow", "系统管理"))
        self.checkBox_4.setText(_translate("MainWindow", "进货管理"))
        self.checkBox_5.setText(_translate("MainWindow", "库存管理"))
        self.pushButton.setText(_translate("MainWindow", "设置"))

    def getvalue(self):
        """
        自定义槽函数，用来根据CheckBox控件的选中状态记录相应的权限
        :return:
        """
        oper = ""
        if self.checkBox.isChecked():
            oper += self.checkBox.text()
        if self.checkBox_2.isChecked():
            oper += '\n' + self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            oper += "\n" + self.checkBox_3.text()
        if self.checkBox_4.isChecked():
            oper += "\n" + self.checkBox_4.text()
        if self.checkBox_5.isChecked():
            oper += '\n' + self.checkBox_5.text()

        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(MainWindow, "提示", "您选择的权限如下：\n" + oper, QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
