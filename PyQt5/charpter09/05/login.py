from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建表单布局
        form = QFormLayout()

        # 创建并设置标签文本
        label1 = QLabel()
        label1.setText('用户名：')
        # 创建输入框
        text1 = QLineEdit()

        # 创建并设置标签文本
        label2 = QLabel()
        label2.setText('密码：')
        # 创建输入框
        text2 = QLineEdit()

        # 创建登录和取消按钮
        btn1 = QPushButton()
        btn1.setText("登录")
        btn2 = QPushButton()
        btn2.setText("取消")

        # 将上面创建的6个控件分为3行添加到列表布局中
        form.addRow(label1, text1)
        form.addRow(label2, text2)
        form.addRow(btn1)
        form.addRow(btn2)

        # 设置表单布局
        form.setRowWrapPolicy(QFormLayout.WrapAllRows)
        self.setLayout(form)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
