from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUI(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 300)
        MainWindow.setWindowTitle("遍历文件夹")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # 添加表格
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 40, 501, 270))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)  # 设置列数

        # 设置第一列的标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("文件名")

        # 设置第二列的标题
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("详细信息")
        self.tableWidget.setColumnWidth(0, 100) # 设置第一列的宽度
        # 设置最后一列自动填充容器
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        # 创建选择路径按钮
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 75, 23))
        # 为按钮设置字体
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("选择路径")

        MainWindow.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.getinfo)

    def getinfo(self):
        try:
            import os
            self.dir_path = QFileDialog.getExistingDirectory(None, '选择路径', os.getcwd())
            if self.dir_path != '':
                self.list = os.listdir(self.dir_path)
                flag = 0
                for i in range(0, len(self.list)):
                    filepath = os.path.join(self.dir_path, self.list[i])
                    self.tableWidget.insertRow(flag)
                    self.tableWidget.setItem(flag, 0, QtWidgets.QTableWidgetItem(self.list[i]))
                    self.tableWidget.setItem(flag, 1, QtWidgets.QTableWidgetItem(filepath))
                    flag += 1
        except Exception as e:
            print(e)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUI(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

