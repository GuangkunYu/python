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
        MainWindow.resize(507, 421)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 140, 72, 15))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(220, 140, 113, 21))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(180, 180, 72, 15))
        self.label_2.setObjectName("label_2")

        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 180, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(180, 230, 72, 15))
        self.label_3.setObjectName("label_3")

        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 230, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(180, 280, 72, 15))
        self.label_4.setObjectName("label_4")

        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 280, 113, 21))
        self.lineEdit_4.setObjectName("lineEdit_4")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.lineEdit.returnPressed.connect(self.getname)
        self.lineEdit_2.returnPressed.connect(self.getage)
        self.lineEdit_3.returnPressed.connect(self.getgrade)
        self.lineEdit_4.returnPressed.connect(self.getscore)

    def getname(self):
        """
        自定义槽函数：获取姓名，弹出可以输入字符串的输入框
        :return:
        """
        name, ok = QtWidgets.QInputDialog.getText(MainWindow, "姓名", '请输入姓名', QtWidgets.QLineEdit.Normal,
                                                  '明日科技')
        if ok:
            self.lineEdit.setText(name)

    def getage(self):
        """
        自定义槽函数：获取年龄，弹出可以选择或输入年龄的输入框
        :return:
        """
        age, ok = QtWidgets.QInputDialog.getInt(MainWindow, '年龄', '请选择年龄', 20, 1, 100, 1)
        if ok:
            self.lineEdit_2.setText(str(age))

    def getgrade(self):
        """
        自定义槽函数：获取班级，弹出可以选择班级的输入框
        :return:
        """
        grade, ok = QtWidgets.QInputDialog.getItem(MainWindow, '班级', '请选择班级', ('三年一班', '三年二班', '三年三班'),
                                                   0, False)
        if ok:
            self.lineEdit_3.setText(grade)

    def getscore(self):
        """
        自定义槽函数：获取成绩，弹出可以选择或输入分数的输入框，保留两位小数
        :return:
        """
        score, ok = QtWidgets.QInputDialog.getDouble(MainWindow, '成绩', '请选择成绩', 0.01, 0, 100, 2)
        if ok:
            self.lineEdit_4.setText(str(score))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "姓名："))
        self.label_2.setText(_translate("MainWindow", "年龄："))
        self.label_3.setText(_translate("MainWindow", "班级："))
        self.label_4.setText(_translate("MainWindow", "分数："))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
