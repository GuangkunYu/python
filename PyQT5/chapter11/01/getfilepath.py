from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("获取文件信息")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.setFont(font)

        grid = QGridLayout()    # 创建网格布局

        # 创建标签
        label_word = QLabel()
        label_word.setText('选择路径：')
        grid.addWidget(label_word, 0, 0, QtCore.Qt.AlignLeft)

        # 创建显示选中文件的文本框
        self.text_path = QLineEdit()
        self.text_path.setFixedWidth(300)
        self.text_path.setFixedHeight(30)
        grid.addWidget(self.text_path, 0, 1, 1, 3, QtCore.Qt.AlignLeft)

        # 创建选择按钮
        btn = QPushButton()
        btn.setText("选择")
        btn.setFixedHeight(32)
        btn.clicked.connect(self.getInfo)
        grid.addWidget(btn, 0, 4, QtCore.Qt.AlignCenter)

        # 创建显示文件信息的文本浏览器
        self.text_brower = QTextBrowser()
        self.text_brower.setFixedWidth(506)
        grid.addWidget(self.text_brower, 1, 0, 1, 5, QtCore.Qt.AlignLeft)

        # 设置网格布局
        self.setLayout(grid)

    def getInfo(self):
        file = QFileDialog()        # 创建文件对话框
        file.setDirectory('c:\\')   # 设置初始路径为c盘
        if file.exec_():    # 判断是否选择了文件
            filename = file.selectedFiles()[0]  # 获取选择的文件
            self.text_path.setText(filename)    # 将选择的文件显示在文本框
            import os, time
            fileinfo = os.stat(filename)    # 获取文件信息
            self.text_brower.setText("文件完整路径：" + os.path.abspath(filename) +
                                     "\n文件大小：" + str(fileinfo.st_size) + " 字节"
                                     "\n最后一次访问时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fileinfo.st_atime)) +
                                     "\n最后一次修改的时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fileinfo.st_mtime)) +
                                     "\n最后一次状态变换的时间：" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(fileinfo.st_ctime)))


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())

