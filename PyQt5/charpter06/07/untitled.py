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

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 81, 31))
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(480, 10, 81, 31))
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 51, 31))
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 220, 51, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 370, 51, 31))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 470, 41, 31))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(590, 470, 51, 31))
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(680, 470, 51, 31))
        self.label_8.setObjectName("label_8")

        # 添加水平分割线，并设置显示样式sunken，表示有下沉显示的边框阴影
        self.line_1 = QtWidgets.QFrame(self.centralwidget)
        self.line_1.setGeometry(QtCore.QRect(80, 80, 251, 80))
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken) # 设置分割线显示样式
        self.line_1.setLineWidth(8)
        self.line_1.setMidLineWidth(8)
        self.line_1.setFrameShape(QtWidgets.QFrame.HLine)  # 设置水平分割线
        self.line_1.setObjectName("line_1")

        # 添加水平分割线，并设置显示样式plain，表示无阴影
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(80, 200, 251, 80))
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(8)
        self.line_2.setMidLineWidth(8)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")

        # 添加水平分割线，并设置显示样式raised，表示有凸起显示的边框阴影
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(80, 350, 251, 80))
        self.line_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_3.setLineWidth(8)
        self.line_3.setMidLineWidth(8)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setObjectName("line_3")

        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(389, -1, 21, 571))
        self.frame_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")

        # 添加垂直分割线，并设置显示样式sunken，表示有下沉显示的边框阴影
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(500, 79, 31, 381))
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setLineWidth(8)
        self.line_5.setMidLineWidth(8)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setObjectName("line_5")

        # 添加垂直分割线，并设置显示样式plain，表示无阴影
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(590, 79, 31, 391))
        self.line_6.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_6.setLineWidth(8)
        self.line_6.setMidLineWidth(8)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setObjectName("line_6")

        # 添加垂直分割线，并设置显示样式raised，表示有凸起显示的边框阴影
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(680, 79, 31, 391))
        self.line_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.line_7.setLineWidth(8)
        self.line_7.setMidLineWidth(8)
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setObjectName("line_7")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "水平分割线"))
        self.label_2.setText(_translate("MainWindow", "垂直分割线"))
        self.label_3.setText(_translate("MainWindow", "Sunken"))
        self.label_4.setText(_translate("MainWindow", "Plain"))
        self.label_5.setText(_translate("MainWindow", "Raised"))
        self.label_6.setText(_translate("MainWindow", "Sunken"))
        self.label_7.setText(_translate("MainWindow", "Plain"))
        self.label_8.setText(_translate("MainWindow", "Raised"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())