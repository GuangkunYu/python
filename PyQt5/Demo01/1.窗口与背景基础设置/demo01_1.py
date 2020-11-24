# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'demo01.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPixmap


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # 设置窗口的对象名称

        # 获取屏幕大小、宽、高
        screen = QtWidgets.QDesktopWidget().screenGeometry()    # 获取屏幕大小
        width = screen.width()  # 获取屏幕宽
        height = screen.height()    # 获取屏幕宽

        MainWindow.resize(1000, 800)     # 修改窗口的大小

        # 更换窗口图标
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("图标 (7).ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        # 设置窗口的背景方式一：
        # 设置背景颜色
        # MainWindow.setStyleSheet("#MainWindow{background-color:blue}")
        #  设置背景图片
        # MainWindow.setStyleSheet("#MainWindow{border-image:url(image/back.jpg)}")
        # MainWindow.setStyleSheet("#MainWindow{background-image:url(image/back.jpg)}")   # 背景图平铺

        # 设置窗口的背景方式二：
        palette = QtGui.QPalette()
        # 设置背景颜色
        # palette.setColor(QtGui.QPalette.Background, Qt.red)
        # 设置背景图片
        # palette.setBrush(QtGui.QPalette.Background, QBrush(QPixmap("./image/back.jpg")))    # 背景图平铺
        palette.setBrush(MainWindow.backgroundRole(),
                         QBrush(QPixmap("./image/back.jpg").scaled(MainWindow.size(),
                                                                   QtCore.Qt.IgnoreAspectRatio,
                                                                   QtCore.Qt.SmoothTransformation)))    # 背景图自适应
        MainWindow.setPalette(palette)

        # 设置窗口透明度
        # MainWindow.setWindowOpacity(0.5)

        # 设置窗口样式
        # MainWindow.setWindowFlags(Qt.Widget)    # 默认窗口，有最大化、最小化和关闭按钮
        # MainWindow.setWindowFlags(Qt.Window)    # 普通窗口，有最大化、最小化和关闭按钮
        # MainWindow.setWindowFlags(Qt.Dialog)    # 对话框窗口，有问号（？）和关闭按钮
        # MainWindow.setWindowFlags(Qt.Popup)    # 无边框的弹出窗口
        # MainWindow.setWindowFlags(Qt.ToolTip)    # 无边框的提示窗口，没有任务栏
        # MainWindow.setWindowFlags(Qt.SplashScreen)    # 无边框的闪屏窗口，没有任务栏
        # MainWindow.setWindowFlags(Qt.SubWindow)    # 子窗口，窗口没有按钮，但有标题
        # 自定义顶层窗口外观
        # MainWindow.setWindowFlags(Qt.MSWindowsFixedSizeDialogHint)  # 无法调整大小的窗口
        # MainWindow.setWindowFlags(Qt.FramelessWindowHint)  # 无边框的窗口
        # MainWindow.setWindowFlags(Qt.CustomizeWindowHint)  # 有边框但无标题栏和按钮，不能移动和拖动的窗口
        # MainWindow.setWindowFlags(Qt.WindowTitleHint)  # 添加标题栏和一个关闭按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowSystemMenuHint)  # 添加系统目录和一个关闭按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowMaximizeButtonHint)  # 激活最大化按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowMinimizeButtonHint)  # 激活最小化按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowMinMaxButtonsHint)  # 激活最大小化按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowCloseButtonHint)  # 添加一个关闭按钮的窗口
        # MainWindow.setWindowFlags(Qt.WindowContextHelpButtonHint)  # 添加像对话框一样的问号（？）和关闭按钮
        # MainWindow.setWindowFlags(Qt.WindowStaysOnTopHint)  # 使窗口始终处于顶层位置
        # MainWindow.setWindowFlags(Qt.WindowStaysOnBottomHint)  # 使窗口始终处于低层位置





        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "这里是标题栏"))   # 设置窗口标题栏名称

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
