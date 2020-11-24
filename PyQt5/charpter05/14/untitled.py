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
        MainWindow.resize(605, 512)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(5, 1, 591, 461))
        # 设置列表中可以多选
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        # 设置选中方式为整行选中
        self.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        # 设置以列表形式显示数据
        self.listWidget.setViewMode(QtWidgets.QListView.ListMode)
        # 设置自动换行
        self.listWidget.setWordWrap(True)
        # 字典默认无需，可借助collections模块的OrderedDict类来使字典有序
        from collections import OrderedDict
        # 定义有序字典，作为list列表的数据源
        dict = OrderedDict({'第1名': '战狼2,2017年上映，票房56.83亿',
                            '第2名': '哪吒之魔童降世，2019年上映，票房50.12亿',
                            '第3名': '流浪地球，2019年上映，票房46.86亿',
                            '第4名': '复仇者联盟：终局之战，2019年上映，票房42.50亿',
                            '第5名': '红海行动，2018年上映，票房36.51亿',
                            '第6名': '唐人街探案2，2018年上映，票房33.98亿',
                            '第7名': '美人鱼，2016年上映，票房33.86亿',
                            '第8名': '我和我的祖国，2019年上映，票房31.71亿',
                            '第9名': '我不是药神，2018年上映，票房31.00亿',
                            '第10名': '中国机长，2019年上映，票房29.13亿'})
        # 遍历字典，并分别获取键值
        for key, value in dict.items():
            # 创建列表项
            self.item = QtWidgets.QListWidgetItem(self.listWidget)
            # 设置项文本
            self.item.setText(key + ": " + value)
            # 设置提示文字
            self.item.setToolTip((value))
        self.listWidget.setObjectName("listWidget")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 605, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.listWidget.itemClicked.connect(self.gettext)
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def gettext(self, item):
        """
        定义槽函数：获取列表选中项中的值
        :return:
        """
        if item.isSelected():
            from PyQt5.QtWidgets import QMessageBox
            QMessageBox.information(MainWindow, "提示", "您选择的是：" + item.text(), QMessageBox.Ok)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())