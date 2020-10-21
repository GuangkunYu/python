from pyecharts.charts import Bar
from pyecharts import options as opts

bar = Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.add_yaxis("商家B", [15, 6, 45, 20, 35, 66])

# 全局配置项可通过set_global_options方法设置
bar.set_global_opts(
    # 标题配置项 TitleOpts
    title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"),
    # 图例配置项 LegendOpts
    # 工具箱配置项 ToolboxOpts
    # 视觉映射配置项 VisualMapOpts
    # 提示框配置项 TooltipOpts
    # 区域缩放配置项 DataZoomOpts
)

bar.render("html/全局配置项.html")
