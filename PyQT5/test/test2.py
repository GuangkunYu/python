import datetime
import time

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from pyecharts.charts import Pie
from pyecharts_javascripthon.api import TRANSLATOR


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()
        self.echarts = False
        self.browser.load(QUrl("file:///bar.html"))
        # self.browser.loadFinished.connect(self.set_options)

    def initUI(self):
        self.setWindowTitle("我的窗口")

        grid = QGridLayout()
        self.browser = QWebEngineView()
        self.browser.setContextMenuPolicy(Qt.NoContextMenu)
        grid.addWidget(self.browser, 0, 0, Qt.AlignLeft)
        self.setLayout(grid)



    def create_pie(self, v=None):
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        print('create_pie')
        bar = Bar("test", 'TITLE_SUBTEXT')
        bar.add('商家1', ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], ['12','50','20','25','10'], is_more_utils=True)
        bar.add('商家2', ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], ['12','50','20','25','10'], is_more_utils=True)
        snippet = TRANSLATOR.translate(bar.options)
        options = snippet.as_snippet()

        return options


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
