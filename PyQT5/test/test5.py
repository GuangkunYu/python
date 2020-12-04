import os
import random

from PyQt5.QtCore import *
from PyQt5.QtNetwork import QNetworkProxyFactory
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from pyecharts.charts import Pie, Bar, Bar3D
from pyecharts_javascripthon.api import TRANSLATOR
from pyecharts.globals import CurrentConfig
from pyecharts import options as opt

# CurrentConfig.ONLINE_HOST = 'https://cdn.jsdelivr.net/npm/echarts@latest/dist/'
# CurrentConfig.ONLINE_HOST = '/js/'

class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("我的窗口")

        grid = QGridLayout()
        self.browser = QWebEngineView()
        self.browser.setContextMenuPolicy(Qt.NoContextMenu)
        self.bar1()
        self.browser.load(QUrl('file:///bar1.html'))
        # self.draw_bar()
        grid.addWidget(self.browser, 0, 0, Qt.AlignLeft)


        self.setLayout(grid)

    def bar1(self):
        from pyecharts import options as opts
        from pyecharts.charts import Bar
        from pyecharts.commons.utils import JsCode
        from pyecharts.globals import ThemeType

        list2 = [
            {"value": 12, "percent": 12 / (12 + 3)},
            {"value": 23, "percent": 23 / (23 + 21)},
            {"value": 33, "percent": 33 / (33 + 5)},
            {"value": 3, "percent": 3 / (3 + 52)},
            {"value": 33, "percent": 33 / (33 + 43)},
        ]

        list3 = [
            {"value": 3, "percent": 3 / (12 + 3)},
            {"value": 21, "percent": 21 / (23 + 21)},
            {"value": 5, "percent": 5 / (33 + 5)},
            {"value": 52, "percent": 52 / (3 + 52)},
            {"value": 43, "percent": 43 / (33 + 43)},
        ]

        c = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT, js_host="js2/"))
                .add_xaxis([1, 2, 3, 4, 5])
                .add_yaxis("product1", list2, stack="stack1", category_gap="50%")
                .add_yaxis("product2", list3, stack="stack1", category_gap="50%")
                .set_series_opts(
                label_opts=opts.LabelOpts(
                    position="right",
                    formatter=JsCode(
                        "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
                    ),
                )
            )
                .render("bar1.html")
        )


    def draw_bar(self):

        c = (
            Bar(init_opts=opt.InitOpts(js_host="js2/"))
                .add_xaxis(
                [
                    "名字很长的X轴标签1",
                    "名字很长的X轴标签2",
                    "名字很长的X轴标签3",
                    "名字很长的X轴标签4",
                    "名字很长的X轴标签5",
                    "名字很长的X轴标签6",
                ]
            )
                .add_yaxis("商家A", [10, 20, 30, 40, 50, 40])
                .add_yaxis("商家B", [20, 10, 40, 30, 40, 50])
            .render('bar1.html')
        )
        print(c)
        return c

    def draw_bar3D(self):
        from pyecharts.faker import Faker
        from pyecharts import options as opts

        data = [(i, j, random.randint(0, 12)) for i in range(6) for j in range(24)]
        c = (
            Bar3D(init_opts=opt.InitOpts(js_host="js2/"))
                .add(
                "",
                [[d[1], d[0], d[2]] for d in data],
                xaxis3d_opts=opts.Axis3DOpts(Faker.clock, type_="category"),
                yaxis3d_opts=opts.Axis3DOpts(Faker.week_en, type_="category"),
                zaxis3d_opts=opts.Axis3DOpts(type_="value"),
            )
                .set_global_opts(
                visualmap_opts=opts.VisualMapOpts(max_=20),
                title_opts=opts.TitleOpts(title="Bar3D-基本示例"),
            ).render('bar3d1.html')
        )
        print(c)
        return c


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())
