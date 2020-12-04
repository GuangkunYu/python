from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(367, 267)
        MainWindow.setWindowTitle("龟兔赛跑")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName('centralwidget')

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 10, 91, 21))
        self.label.setObjectName("label")
        self.label.setText("兔子的比赛记录")

        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 40, 161, 191))
        self.textEdit.setObjectName("textEdit")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 10, 91, 21))
        self.label_2.setObjectName("label_2")
        self.label_2.setText("乌龟的比赛记录")

        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(190, 40, 161, 191))
        self.textEdit_2.setObjectName("textEdit_2")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(140, 240, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("开始比赛")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.r = Rabbit()
        self.r.sinOut.connect(self.rabbit)
        self.t = Tortoise()
        self.t.sinOut.connect(self.tortoise)
        self.pushButton.clicked.connect(self.start)

    def start(self):
        self.r.start()
        self.t.start()

    def rabbit(self, str):
        self.textEdit.setPlainText(self.textEdit.toPlainText() + str)

    def tortoise(self, str):
        self.textEdit_2.setPlainText(self.textEdit_2.toPlainText() + str)


class Rabbit(QThread):
    sinOut=pyqtSignal(str)
    def __init__(self):
        super(Rabbit, self).__init__()

    def run(self):
        for i in range(1, 11):
            QThread.msleep(500)
            self.sinOut.emit(f"\n  兔子跑了 {i}0 米")
            if i==9:
                self.sinOut.emit("\n  兔子在睡觉")
                QThread.sleep(8)
            if i==10:
                self.sinOut.emit("\n  兔子到达终点")


class Tortoise(QThread):
    sinOut = pyqtSignal(str)

    def __init__(self):
        super(Tortoise, self).__init__()

    def run(self):
        for i in range(1, 11):
            QThread.msleep(1000)
            self.sinOut.emit(f"\n  乌龟跑了 {i}0 米")
            if i == 10:
                self.sinOut.emit("\n  乌龟到达终点")


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



