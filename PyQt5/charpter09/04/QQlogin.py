from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()   # 初始化窗口

    def initUI(self):
        self.setWindowTitle("QQ登录窗口")
        grid = QGridLayout()    # 创建网格布局

        # 创建顶部图片
        label1 = QLabel()
        label1.setPixmap(QtGui.QPixmap('images/top.png'))

        # 创建并设置用户名标签文本
        label2 = QLabel()
        label2.setPixmap(QtGui.QPixmap('images/qq1.png'))
        # 创建用户名输入文本框
        text1 = QLineEdit()

        # 创建并设置标签文本
        label3 = QLabel()
        label3.setPixmap(QtGui.QPixmap('images/qq2.png'))
        # 创建输入文本框
        text2 = QLineEdit()

        # 创建安全登录按钮
        btn1 = QPushButton()
        btn1.setText('安全登录')

        # 第1行第1列到第3行第4列添加标签控件，并设置居中对齐
        grid.addWidget(label1, 0, 0, 3, 4, QtCore.Qt.AlignCenter)
        # 第4行第2列添加标签框控件，并设置右对齐
        grid.addWidget(label2, 3, 1, QtCore.Qt.AlignRight)
        # 第4行第3列添加输入文本框控件，并设置左对齐
        grid.addWidget(text1, 3, 2, QtCore.Qt.AlignLeft)
        # 第5行第2列添加标签框控件，并设置右对齐
        grid.addWidget(label3, 4, 1, QtCore.Qt.AlignRight)
        # 第5行第3列添加输入文本框控件，并设置左对齐
        grid.addWidget(text2, 4, 2, QtCore.Qt.AlignLeft)
        # 第6行第2列到第3列添加按钮控件，并设置居中对齐
        grid.addWidget(btn1, 5, 1, 1, 2, QtCore.Qt.AlignCenter)

        # 设置网格布局
        self.setLayout(grid)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
