import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

# 读取excel数据
df = pd.read_excel("648(1)(1).xls")
# print(df)

#　获取ｘ数据
time_x = df.iloc[6:, 0].values.tolist()[0:-1:5]
# print(time_x)
# print(len(time_x))

# 获取y轴数据
val_y = df.iloc[6:, 1].values.reshape((5, -1))
avg = np.mean(val_y, axis=0).tolist()
# print(avg)
# # print(val_y)
# print(len(avg))

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis(time_x)
    .add_yaxis("第一列", avg)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="第一列"),
        datazoom_opts=opts.DataZoomOpts(type_="inside"),
    )
    .set_series_opts(LabelOpts(is_show=False))
    .render("html/bar_datazoom_inside.html")
)