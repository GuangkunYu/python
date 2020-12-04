# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QBrush, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import imageMark


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)

        # 设置菜单栏
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 30))
        self.menuBar.setObjectName("menuBar")

        # 添加 主菜单 菜单
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")

        # 添加 关于 菜单
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setObjectName("menu_2")

        # 添加 添加水印 子菜单
        self.actionMark = QtWidgets.QAction(MainWindow)
        # 设置子菜单图标
        icon = QtGui.QIcon()  # 创建图标对象
        icon.addPixmap(QtGui.QPixmap('img\\mark.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 设置图标文件
        self.actionMark.setIcon(icon)  # 为 添加水印 子菜单设置图标
        self.actionMark.setObjectName("actionMark")
        self.menu.addAction(self.actionMark)  # 将 添加水印 子菜单添加到 主菜单中

        # 添加 批量重命名 子菜单
        self.actionRename = QtWidgets.QAction(MainWindow)
        # 设置子菜单图标
        icon_2 = QtGui.QIcon()  # 创建图标对象
        icon_2.addPixmap(QtGui.QPixmap('img\\rename.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 设置图标文件
        self.actionRename.setIcon(icon_2)  # 为 批量重命名 子菜单设置图标
        self.actionRename.setObjectName("actionRename")
        self.menu.addAction(self.actionRename)  # 将 批量重命名 子菜单添加到 主菜单中

        # 菜单栏中添加主菜单
        self.menuBar.addAction(self.menu.menuAction())

        # 添加  关于本软件 子菜单
        self.actionAbout = QtWidgets.QAction(MainWindow)
        # 设置子菜单图标
        icon_3 = QtGui.QIcon()  # 创建图标对象
        icon_3.addPixmap(QtGui.QPixmap('img\\about.ico'), QtGui.QIcon.Normal, QtGui.QIcon.Off)  # 设置图标文件
        self.actionAbout.setIcon(icon_3)  # 为 关于本软件 子菜单设置图标
        self.actionAbout.setObjectName("actionAbout")
        self.menu_2.addAction(self.actionAbout)  # 将 关于本软件 子菜单添加到 主菜单中

        # 菜单栏中添加主菜单
        self.menuBar.addAction(self.menu_2.menuAction())
        MainWindow.setMenuBar(self.menuBar)

        # 设置窗体背景
        palette = QtGui.QPalette()
        # 设置窗体背景自适应
        palette.setBrush(MainWindow.backgroundRole(),
                         QBrush(QPixmap('img\\back.png').scaled(MainWindow.size(),
                                                                QtCore.Qt.IgnoreAspectRatio,
                                                                QtCore.Qt.SmoothTransformation)))
        MainWindow.setPalette(palette)
        MainWindow.setAutoFillBackground(True)  # 设置自动填充背景
        # 禁止显示最大化按钮及调整窗体大小
        MainWindow.setFixedSize(800, 600)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.actionMark.triggered.connect(self.openMark)
        self.actionRename.triggered.connect(self.openRename)
        self.actionAbout.triggered.connect(self.about)

    # 打开水印窗体
    def openMark(self):
        self.another = imageMark.Ui_MainWindow()
        self.another.show()

    # 打开重命名窗体
    def openRename(self):
        pass

    # 打开关于本软件
    def about(self):
        QMessageBox.information(None,
                                '关于本软件',
                                "图片批量处理器是一款提供日常工作的工具软件，"
                                "通过该软件，您可以方便的为图片添加文字水印和图片水印，"
                                "而且可以自定义添加位置，以及透明度；另外，您还可以通过。"
                                "该软件对图片文件进行重命名，支持文件名大写、小写，以及，"
                                "根据自定义模板对图片文件进行编号。",
                                QMessageBox.Ok)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "明日图片助手"))
        self.menu.setTitle(_translate("MainWindow", "主菜单"))
        self.menu_2.setTitle(_translate("MainWindow", " ||  关于"))
        self.actionMark.setText(_translate("MainWindow", "添加水印"))
        self.actionRename.setText(_translate("MainWindow", "批量重命名"))
        self.actionAbout.setText(_translate("MandoinWiw", "关于本软件"))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
