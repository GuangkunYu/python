from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('使用表格显示数据库中的数据')
        self.resize(1000, 210)
        vhayout = QHBoxLayout()  # 设置水平布局
        table = QTableWidget()  # 创建表格

        import pymysql
        db = pymysql.connect('192.168.4.192', 'root', 'root', 'ygk-qt5', charset='utf8')
        cursor = db.cursor()
        cursor.execute('select * from books')
        result = cursor.fetchall()
        row = cursor.rowcount
        vol = len(result[0])
        cursor.close()
        db.close()

        table.setRowCount(row)  # 设置表格行数
        table.setColumnCount(vol)  # 设置表格列数

        # 设置表格的标题名称
        table.setHorizontalHeaderLabels(['ID', '图书名称', '图书分类', '图书价格', '出版时间'])
        for i in range(row):  # 遍历行
            for j in range(vol):  # 遍历列
                if j == 4:
                    data = QTableWidgetItem(QtGui.QIcon('date.png'), str(result[i][j])) # 插入文字和图片
                # elif j == 2:
                #     comobox = QComboBox()
                #     comobox.addItems(['Python', 'Java', 'C语言', '.NET'])
                #     comobox.setCurrentIndex(0)
                #     table.setCellWidget(i, 2, comobox)  # 将创建的下拉列表显示在表格中
                else:
                    data = QTableWidgetItem(str(result[i][j]))   # 直接插入文字
                # data = QTableWidgetItem(str(result[i][j]))  # 转换后可插入表格
                # data.setForeground(QtGui.QBrush(QtGui.QColor('green'))) # 设置单元格文本颜色为绿色
                # data.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))

                table.setItem(i, j, data)

        table.resizeColumnsToContents()  # 使列宽跟随内容改变
        table.resizeRowsToContents()  # 使行高度跟随内容改变
        table.setAlternatingRowColors(True)  # 使表格颜色交错显示
        table.verticalHeader().setVisible(False)  # 隐藏垂直标题
        # table.horizontalHeader().setVisible(False)  # 隐藏水平标题
        # table.horizontalHeader().setStretchLastSection(True)    # 设置最后一列自动填充容器
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 设置整个表格按比例自动缩放
        table.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 禁止编辑单元格
        # table.sortItems(4, QtCore.Qt.DescendingOrder)   # 设置降序排序
        table.setSpan(0, 2, 5, 1)   # 合并单元格
        table.setSpan(2, 3, 3, 1)
        table.setSpan(2, 4, 3, 1)

        vhayout.addWidget(table)  # 将表格添加到水平布局中
        self.setLayout(vhayout)  # 设置当前窗口的布局方式


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
