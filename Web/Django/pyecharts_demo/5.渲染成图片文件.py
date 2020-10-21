from pyecharts.charts import Bar
from pyecharts.render import make_snapshot

# 使用snapshot_selenium渲染图片
from snapshot_selenium import snapshot

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])

make_snapshot(snapshot, bar.render('html/渲染图片文件.html'), "html/bar.png")
