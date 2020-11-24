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

        # 添加工具栏
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        self.toolBar.setMovable(True)   # 设置工具栏可移动
        self.toolBar.setOrientation(QtCore.Qt.Horizontal)   # 设置工具栏为水平工具栏
        # MainWindow.addToolBar("toolBar")

        # 为工具栏添加图标按钮
        # 设置工具栏中按钮的显示方式为：文字显示在图标的下方
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.addAction(QtGui.QIcon("images/new.ico"), "新建")

        # 一次为工具栏添加多个图标按钮
        # 创建打开按钮对象
        self.open = QtWidgets.QAction(QtGui.QIcon("images/open.ico"), "打开")
        # 创建关闭按钮对象
        self.close = QtWidgets.QAction(QtGui.QIcon("images/close.ico"), "关闭")
        self.toolBar.addActions([self.open, self.close])

        # 向工具栏中添加标准控件
        # 创建一个combobox下拉列表控件
        self.combobox = QtWidgets.QComboBox()
        list = ['总经理', '副总经理', '人事经理', '财务经理', '部门经理', '普通员工']
        self.combobox.addItems(list)
        self.toolBar.addWidget(self.combobox)

        # 设置工具栏按钮的大小
        self.toolBar.setIconSize(QtCore.QSize(16, 16))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # 将combobox控件的选项更改信号与自定义槽函数关联
        self.combobox.currentIndexChanged.connect(self.showinfo)
        self.toolBar.actionTriggered[QtWidgets.QAction].connect(self.getvalue)

    def showinfo(self):
        QtWidgets.QMessageBox.information(MainWindow, '提示', '您选择的职位是：' + self.combobox.currentText(),
                                          QtWidgets.QMessageBox.Ok)

    def getvalue(self, m):
        QtWidgets.QMessageBox.information(MainWindow, '提示', '您单击了' + m.text(),
                                          QtWidgets.QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())