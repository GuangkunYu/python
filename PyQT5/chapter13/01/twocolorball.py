from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer
import PyQt5.sip
import random


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 294)
        MainWindow.setWindowTitle("双色球彩票选号器")
        # 设置窗口背景图片
        MainWindow.setStyleSheet("#MainWindow{border-image: url(images/双色球彩票选号器.jpg)}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 创建第一个红球数字的标签
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(97, 178, 31, 31))
        # 设置标签字体
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setWeight(75)
        self.label.setFont(font)
        # 设置标签的文字颜色
        self.label.setStyleSheet("color:rgb(255,255,255)")
        self.label.setObjectName("label")
        self.label.setText("00")
        self.label.setAttribute(QtCore.Qt.WA_TranslucentBackground) # 设置显示双色球数字label标签背景透明

        # 创建第2个红球数字的标签
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(153, 178, 31, 31))
        # 设置标签字体
        self.label_2.setFont(font)
        # 设置标签的文字颜色
        self.label_2.setStyleSheet("color:rgb(255,255,255)")
        self.label_2.setObjectName("label_2")
        self.label_2.setText("00")
        self.label_2.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建第3个红球数字的标签
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(209, 178, 31, 31))
        # 设置标签字体
        self.label_3.setFont(font)
        # 设置标签的文字颜色
        self.label_3.setStyleSheet("color:rgb(255,255,255)")
        self.label_3.setObjectName("label_3")
        self.label_3.setText("00")
        self.label_3.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建第4个红球数字的标签
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(265, 178, 31, 31))
        # 设置标签字体
        self.label_4.setFont(font)
        # 设置标签的文字颜色
        self.label_4.setStyleSheet("color:rgb(255,255,255)")
        self.label_4.setObjectName("label_4")
        self.label_4.setText("00")
        self.label_4.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建第5个红球数字的标签
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(321, 178, 31, 31))
        # 设置标签字体
        self.label_5.setFont(font)
        # 设置标签的文字颜色
        self.label_5.setStyleSheet("color:rgb(255,255,255)")
        self.label_5.setObjectName("label_5")
        self.label_5.setText("00")
        self.label_5.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建第6个红球数字的标签
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(377, 178, 31, 31))
        # 设置标签字体
        self.label_6.setFont(font)
        # 设置标签的文字颜色
        self.label_6.setStyleSheet("color:rgb(255,255,255)")
        self.label_6.setObjectName("label_6")
        self.label_6.setText("00")
        self.label_6.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建蓝球数字的标签
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(97, 240, 31, 31))
        # 设置标签字体
        self.label_7.setFont(font)
        # 设置标签的文字颜色
        self.label_7.setStyleSheet("color:rgb(255,255,255)")
        self.label_7.setObjectName("label_7")
        self.label_7.setText("00")
        self.label_7.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # 创建开始按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310,235,51,51))
        # 设置开始的背景图片
        self.pushButton.setStyleSheet("#pushButton{border-image: url(images/开始.jpg)}")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")

        # 创建开始按钮
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 235, 51, 51))
        # 设置开始的背景图片
        self.pushButton_2.setStyleSheet("#pushButton_2{border-image: url(images/停止.jpg)}")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.start)
        self.pushButton_2.clicked.connect(self.stop)

    def start(self):
        self.timer = QTimer(MainWindow)
        self.timer.start()
        self.timer.timeout.connect(self.num)    # 设计计时器要执行的槽函数

    def num(self):
        self.label.setText(f"{random.randint(1, 33)}")
        self.label_2.setText(f"{random.randint(1, 33)}")
        self.label_3.setText(f"{random.randint(1, 33)}")
        self.label_4.setText(f"{random.randint(1, 33)}")
        self.label_5.setText(f"{random.randint(1, 33)}")
        self.label_6.setText(f"{random.randint(1, 33)}")
        self.label_7.setText(f"{random.randint(1, 16)}")

    def stop(self):
        self.timer.stop()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())