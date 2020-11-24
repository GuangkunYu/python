from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # 创建表单布局
        form = QFormLayout()

        # 创建并设置标签文本
        label_username = QLabel()
        label_username.setText('用户名：')
        # 创建输入文本框
        text_username = QLineEdit()

        # 创建并设置标签文本
        label_password = QLabel()
        label_password.setText('密码：')
        # 创建输入文本框
        text_password = QLineEdit()

        # 创建登录取消按钮
        btn_login = QPushButton()
        btn_login.setText('登录')
        btn_cancle = QPushButton()
        btn_cancle.setText('取消')

        # 将创建的控件加入到表单布局中
        form.addRow(label_username, text_username)
        # 创建垂直布局管理器
        vlayout = QVBoxLayout()
        vlayout.addWidget(text_password)
        vlayout.addWidget(QLabel('密码只能输入8位'))
        form.addRow(label_password, vlayout)
        form.addRow(btn_login, btn_cancle)

        # 设置表单布局
        self.setLayout(form)



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())