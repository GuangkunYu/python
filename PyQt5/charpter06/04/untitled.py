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

        self.treeView = QtWidgets.QTreeView(self.centralwidget)     # 创建树对象
        self.treeView.setGeometry(QtCore.QRect(10, 10, 781, 521))   # 设置坐标位置和大小
        # 设置垂直滚动条为按需显示
        self.treeView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # 设置水平滚动条为按需显示
        self.treeView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # 设置双击或者按下回车键时，使树节点可编辑
        self.treeView.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.EditKeyPressed)
        # 设置树节点为单选
        self.treeView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        # 设置选中节点时为整行选中
        self.treeView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 设置自动展开的延时为-1，表示自动展开不可用
        self.treeView.setAutoExpandDelay(-1)
        # 设置是否可以展开项
        self.treeView.setItemsExpandable(True)
        # 设置单击头部可排序
        self.treeView.setSortingEnabled(True)
        # 设置自动换行
        self.treeView.setWordWrap(True)
        # 设置不影藏头部
        self.treeView.setHeaderHidden(False)
        # 设置双击可以展开节点
        self.treeView.setExpandsOnDoubleClick(True)
        # 设置显示头部
        self.treeView.header().setVisible(True)
        self.treeView.setObjectName("treeView")

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

        # 创建存储文件系统的模型
        model = QtWidgets.QDirModel()
        # 为树控件设置数据模型
        self.treeView.setModel(model)

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