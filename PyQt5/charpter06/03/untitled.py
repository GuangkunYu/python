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

        # 创建一个水平布局管理器，主要用来防止显示文字的label
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(180, 170, 561, 261))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # 创建label控件，用来显示文字
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setAlignment(QtCore.Qt.AlignCenter)  # 设置文字居中对齐
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)     # 将label添加到水平布局管理器中

        # 创建垂直滑块
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(130, 180, 18, 259))
        self.verticalSlider.setMinimum(8)   # 设置最小值为8
        self.verticalSlider.setMaximum(72)  # 设置最大值为72
        self.verticalSlider.setOrientation(QtCore.Qt.Vertical)  # 设置滑块为垂直滑块
        self.verticalSlider.setInvertedAppearance(True)     # 设置刻度反向显示
        self.verticalSlider.setTickPosition(QtWidgets.QSlider.TicksLeft)   # 设置滑块左侧显示刻度
        self.verticalSlider.setTickInterval(3)  # 设置刻度的间隔
        self.verticalSlider.setObjectName("verticalSlider")

        # 创建水平滑块
        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(140, 150, 291, 18))
        self.horizontalSlider.setMinimum(8)  # 设置最小值为8
        self.horizontalSlider.setMaximum(72)  # 设置最大值为72
        self.horizontalSlider.setSingleStep(1)  # 设置通过鼠标拖动时的步长值
        self.horizontalSlider.setPageStep(1)    # 设置通过鼠标点击时的步长值
        self.horizontalSlider.setProperty("value", 8)   # 设置默认值为8
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)  # 设置滑块为水平滑块
        self.horizontalSlider.setTickPosition(QtWidgets.QSlider.TicksAbove) # 设置在滑块上方显示刻度
        self.horizontalSlider.setTickInterval(3)    # 设置刻度的间隔
        self.horizontalSlider.setObjectName("horizontalSlider")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.valueChanged.connect(self.setfontsize)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "敢想敢为，注重细节！"))

    def setfontsize(self):
        """
        定义槽函数：根据水平滑块的值改变垂直滑块的值和label控件的字体大小
        :return:
        """
        value = self.horizontalSlider.value()
        self.verticalSlider.setValue(value)
        self.label.setFont(QtGui.QFont("楷体", value))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
