from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建网格布局
        grid = QGridLayout()

        # 创建并设置标签文本
        label1 = QLabel()
        label1.setText("用户名：")
        # 创建输入文本框
        text1 = QLineEdit()

        # 创建并设置标签文本
        label2 = QLabel()
        label2.setText("密码：")
        # 创建输入文本框
        text2 = QLineEdit()

        # 创建登录和取消按钮
        btn1 = QPushButton()
        btn1.setText("登录")
        btn2 = QPushButton()
        btn2.setText("取消")

        # 第一行第一列添加标签控件，并设置左对齐
        grid.addWidget(label1, 0, 0, QtCore.Qt.AlignLeft)
        # 第一行第二列添加输入文本框控件，并设置左对齐
        grid.addWidget(text1, 0, 1, QtCore.Qt.AlignLeft)

        # 第二行第一列添加标签控件，并设置左对齐
        grid.addWidget(label2, 1, 0, QtCore.Qt.AlignLeft)
        # 第二行第二列添加输入文本框控件，并设置左对齐
        grid.addWidget(text2, 1, 1, QtCore.Qt.AlignLeft)

        # 第三行第一列添加标签控件，并设置左对齐
        grid.addWidget(btn1, 2, 0, QtCore.Qt.AlignCenter)
        # 第三行第二列添加输入文本框控件，并设置左对齐
        grid.addWidget(btn2, 2, 1, QtCore.Qt.AlignCenter)

        self.setLayout(grid)  # 设置网格布局


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
