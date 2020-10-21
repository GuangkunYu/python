from pyecharts.charts import Bar
from pyecharts import options as opts

# 内置主题类型可查看pyecharts.globals.ThemeType
from pyecharts.globals import ThemeType

bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
bar.set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))

bar.render("html/使用主题.html")


