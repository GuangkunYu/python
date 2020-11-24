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

        # 创建一个treeview树视图
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(10, 10, 781, 511))
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

        # 创建数据模型
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(['年级', '班级', '姓名', '分数'])
        # 姓名列表
        name = ['马云', '马化腾', '李彦宏', '王兴', '刘强东', '董明珠', '张一鸣', '任正非', '丁磊', '程伟']
        # 分数列表
        score = [65, 89, 45, 68, 90, 100, 99, 76, 85, 73]
        import random
        # 设置数据
        for i in range(0, 6):
            # 一级节点：年级，只设第一列的数据
            grade = QtGui.QStandardItem(f"{i+1}年级")
            model.appendRow(grade)  # 一级节点
            for j in range(0, 4):
                # 二级节点：班级、姓名、分数
                itemClass = QtGui.QStandardItem(f"{j+1}班")
                itemName = QtGui.QStandardItem(name[random.randrange(10)])
                itemScore = QtGui.QStandardItem(str(score[random.randrange(10)]))
                # 将二级节点添加到一级节点上
                grade.appendRow([QtGui.QStandardItem(""), itemClass, itemName, itemScore])
        # 为Treeview设置数据模型
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