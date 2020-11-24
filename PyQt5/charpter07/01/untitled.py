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

        # 一、添加菜单栏
        # self.menubar = MainWindow.menuBar()
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menubar.setObjectName("menubar")

        # 添加文件菜单
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("文件")
        self.menu.setObjectName("menu")
        # 添加编辑菜单
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setTitle("编辑")
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)

        # 添加新建菜单
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        # 设置菜单可用
        self.actionxinjian.setEnabled(True)
        # 为菜单设置图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/new.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionxinjian.setIcon(icon)
        # 设置菜单为Windows快捷键
        self.actionxinjian.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.actionxinjian.setIconVisibleInMenu(True)   # 设置图标可见
        self.actionxinjian.setObjectName("actionxinjian")
        self.actionxinjian.setText("新建(&N)")    # 设置菜单文本
        self.actionxinjian.setIconText("新建")    # 设置图标文本
        self.actionxinjian.setToolTip("新建")     # 设置提示文本
        self.actionxinjian.setShortcut("Ctrl+N")    # 设置快捷键

        # 添加打开菜单
        self.actiondakai = QtWidgets.QAction(MainWindow)
        # 为菜单设置图标
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/open.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiondakai.setIcon(icon1)
        self.actiondakai.setObjectName("actiondakai")
        self.actiondakai.setText("打开(&O)")  # 设置菜单文本
        self.actiondakai.setIconText("打开")  # 设置图标文本
        self.actiondakai.setToolTip("打开")   # 设置提示文本
        self.actiondakai.setShortcut("Ctrl+O")  # 设置快捷键

        # 添加关闭菜单
        self.actionclose = QtWidgets.QAction(MainWindow)
        # 为菜单设置图标
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/close.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionclose.setIcon(icon2)
        self.actionclose.setObjectName("actionclose")
        self.actionclose.setText("关闭(&C)")
        self.actionclose.setIconText("关闭")
        self.actionclose.setToolTip("关闭")
        self.actionclose.setShortcut("Ctrl+M")

        # 在文件菜单中添加新建菜单项
        self.menu.addAction(self.actionxinjian)
        self.menu.addAction(self.actiondakai)
        self.menu.addSeparator()    # 添加分割线
        self.menu.addAction(self.actionclose)

        # 将文件菜单的菜单项添加到菜单栏中
        self.menubar.addAction(self.menu.menuAction())
        # 将编辑菜单的菜单项添加到菜单栏中
        self.menubar.addAction(self.menu_2.menuAction())

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为菜单栏中的QAction绑定triggered信号
        self.menu.triggered[QtWidgets.QAction].connect(self.getmenu)

    def getmenu(self, m):
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.information(MainWindow, '提示', '您选择的是 ' + m.text(), QMessageBox.Ok)

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
