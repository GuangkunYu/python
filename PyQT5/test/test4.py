def set_options(self):
    if not self.view:
        return
    if not self.echarts:
        # 初始化echarts
        self.view.page().runJavaScript(
            '''
                var myChart = echarts.init(document.getElementById('container'), 'light', {renderer: 'canvas'});
            '''
        )
        self.echarts = True
    options = self.get_options()
    if not options:
        return
    self.view.page().runJavaScript(
        f'''
            var option = eval({options});
            myChart.setOption(option);
        '''
    )


def get_options(self):
    v1, v2, v3, v4, v5, v6 = self.spinbox1.value(), self.spinbox2.value(), self.spinbox3.value(), self.spinbox4.value(), \
                             self.spinbox5.value(), self.spinbox6.value()
    v = [v1, v2, v3, v4, v5, v6]
    if self.combobox_type.currentIndex() == 0:
        # 饼图
        options = self.create_pie(v)
    elif self.combobox_type.currentIndex() == 1:
        # 柱状图
        options = self.create_bar(v)
    elif self.combobox_type.currentIndex() == 2:
        # 折线图
        options = self.create_line(v)
    elif self.combobox_type.currentIndex() == 3:
        # 折线、柱状图
        options = self.create_line_bar(v)
    else:
        return
    return options


