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

        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(140, 80, 551, 281))
        # 设置默认选中的日期
        self.calendarWidget.setSelectedDate(QtCore.QDate(2020, 3, 23))
        # 设置最小日期
        self.calendarWidget.setMinimumDate(QtCore.QDate(1752, 9, 14))
        # 设置最大日期
        self.calendarWidget.setMaximumDate(QtCore.QDate(9999, 12, 31))
        # 设置每周的第一天为星期一
        self.calendarWidget.setFirstDayOfWeek(QtCore.Qt.Monday)
        # 设置网格线可见
        self.calendarWidget.setGridVisible(True)
        # 设置可以选中单个日期
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        # 设置水平表头为简短模式，即周一形式
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        # 设置垂直表头为周数
        self.calendarWidget.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.ISOWeekNumbers)
        # 设置显示导航栏
        self.calendarWidget.setNavigationBarVisible(True)
        # 设置日期可编辑
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.calendarWidget.selectionChanged.connect(self.getdate)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def getdate(self):
        """
        自定义槽函数：获取calendarwidget控件中选中的日期，并转换为 年-月-日 形式，显示在弹出框中
        :return:
        """
        # 获取当前选中的日期对的qdate对象
        date = QtCore.QDate(self.calendarWidget.selectedDate())
        year = date.year()
        month = date.month()
        day = date.day()
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(MainWindow, "提示", str(year) + "-" + str(month) + "-" + str(day), QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
