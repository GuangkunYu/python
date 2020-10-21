from pyecharts.charts import Bar
from pyecharts import options as opts
# from pyecharts.globals import ThemeType

# bar = Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.set_global_opts(title_opts={"text": "主标题", "subtext": "副标题"})

bar.render('html/不使用链式的options.html')