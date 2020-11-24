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
        MainWindow.resize(656, 503)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 创建MDI窗口区域
        self.mdiArea = QtWidgets.QMdiArea(self.centralwidget)
        self.mdiArea.setGeometry(QtCore.QRect(0, 0, 656, 471))
        self.mdiArea.setObjectName("mdiArea")

        MainWindow.setCentralWidget(self.centralwidget)

        # 创建菜单栏
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 656, 30))
        self.menubar.setObjectName("menubar")
        # 设置主菜单
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)

        # 设置新建菜单项
        self.actionxinjian = QtWidgets.QAction(MainWindow)
        self.actionxinjian.setObjectName('actionxinjian')
        self.actionxinjian.setText('新建')
        # 设置平铺菜单项
        self.actionpinpu = QtWidgets.QAction(MainWindow)
        self.actionpinpu.setObjectName('actionpingpu')
        self.actionpinpu.setText('平铺显示')
        # 设置级联菜单项
        self.actionjilian = QtWidgets.QAction(MainWindow)
        self.actionjilian.setObjectName('actionjilian')
        self.actionjilian.setText('级联显示')

        # 将新建的三个菜单加到主菜单中
        self.menu.addAction(self.actionxinjian)
        self.menu.addAction(self.actionpinpu)
        self.menu.addAction(self.actionjilian)

        # 将设置完成的主菜单添加到菜单栏中
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 为菜单项关联信号
        self.menubar.triggered[QtWidgets.QAction].connect(self.action)

    count = 0

    def action(self, m):
        """
        自定义槽函数：根据选择的菜单执行相应操作
        :param m:
        :return:
        """
        if m.text() == '新建':
            sub = QtWidgets.QMdiSubWindow()
            self.count = self.count + 1
            sub.setWindowTitle('子窗口' + str(self.count))
            sub.setWidget(QtWidgets.QLabel(f'这是第 {self.count} 个子窗口'))
            self.mdiArea.addSubWindow(sub)      #　将新建的子窗口添加到MDI区域
            sub.show()  # 显示子窗口
        elif m.text() == '平铺显示':
            self.mdiArea.tileSubWindows()   # 对子窗口平铺排列
        elif m.text() == '级联显示':
            self.mdiArea.cascadeSubWindows()    # 对子窗口级联排列

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MDI窗口"))
        self.menu.setTitle(_translate("MainWindow", "子窗体操作"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
