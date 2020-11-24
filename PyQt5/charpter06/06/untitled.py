# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setGeometry(QtCore.QRect(10, 10, 771, 511))
        # 设置树结构中的列数
        self.treeWidget.setColumnCount(2)
        # 设置列标题名
        self.treeWidget.setHeaderLabels(['姓名', '职务'])
        # 创建节点
        root = QTreeWidgetItem(self.treeWidget)
        # 设置顶级节点文本
        root.setText(0, '组织结构')
        # 定义字典，存储树结构中显示的数据
        dict = {
            '任正非': '华为董事长',
            '马云': '阿里巴巴创始人',
            '马化腾': '腾讯CEO',
            '李彦宏': '百度CEO',
            '董明珠': '格力董事长',
        }
        for key, value in dict.items():
            child = QTreeWidgetItem(root)   # 创建子节点
            # 为节点设置图标
            if key == '任正非':
                child.setIcon(0, QtGui.QIcon('images/华为.jpg'))
            elif key == '马云':
                child.setIcon(0, QtGui.QIcon('images/阿里巴巴.jpg'))
            elif key == '马化腾':
                child.setIcon(0, QtGui.QIcon('images/腾讯.png'))
            elif key == '李彦宏':
                child.setIcon(0, QtGui.QIcon('images/百度.jpg'))
            elif key == '董明珠':
                child.setIcon(0, QtGui.QIcon('images/格力.jpeg'))
            child.setCheckState(0, QtCore.Qt.Checked)   # 为节点设置复选框
            child.setText(0, key)   # 设置第一列的值
            child.setText(1, value) # 设置第二列的值
        # 设置隔行变色显示树节点
        self.treeWidget.setAlternatingRowColors(True)
        # 将创建的树节点添加到树控件中
        self.treeWidget.addTopLevelItem(root)
        # 展开所有树节点
        self.treeWidget.expandAll()
        self.treeWidget.setObjectName("treeWidget")
        # self.treeWidget.headerItem().setText(0, "1")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.treeWidget.clicked.connect(self.gettreetext)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def gettreetext(self):
        """
        获取选中节点的文本
        :return:
        """
        item = self.treeWidget.currentItem()    # 获取当前选中项
        # 弹出提示框，显示选中项对的文本
        QtWidgets.QMessageBox.information(MainWindow, '提示',
                                          f'您选择的是：{item.text(0)} -- {item.text(1)}',
                                          QtWidgets.QMessageBox.Ok)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
