from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import json
from pyecharts.globals import ThemeType
from pyecharts.charts import Bar
from pyecharts import options as opts
import pandas as pd
import numpy as np
from pyecharts.options import LabelOpts

DF = None
TITLE = None
DATE = None
LABLES = None
OPT = None
AVG = 1


def bootstrap(request):
    if request.method == "GET":

        return render(request, "bootstrap.html")

    elif request.method == "POST":
        global OPT
        files_get = request.FILES.get("myfile")

        opt = request.POST.get('value')
        if opt is None:
            OPT = 0

        # 获取主标题、时间副标题、标签列表对象
        df, title, date, labels = file_handle(files_get)
        # if opt is None:
        # 标签列表对象转换成list
        label_list = labels.values.tolist()
        # 获取图表标签头，x轴数据，平均值
        y_sub, time_x, avg = get_data(df, label_list, step=AVG)
        # 绘图
        c = drawing(time_x, y_sub, avg, title, date)

        return render(request, "bootstrap.html", locals())


def file_handle(file):
    global DF, TITLE, DATE, LABLES

    if file is not None:
        # 读取数据
        df = pd.read_excel(file)
        DF = df
        title = df.columns[0]
        TITLE = title
        date = df.iloc[0, 0]
        DATE = date
        labels = df.iloc[1, 1:]
        LABLES = labels
    elif file is None:
        df = DF
        title = TITLE
        date = DATE
        labels = LABLES

    return df, title, date, labels


def get_avg_api(request):
    global OPT, AVG
    avg = request.POST.get("avg")
    opt = OPT
    if avg is None:
        avg = AVG
    else:
        AVG = int(avg)
    df = DF
    title = TITLE
    date = DATE
    labels = LABLES
    # 获取主标题、时间副标题、标签列表
    label_list = labels.values.tolist()

    # 获取图表标签头，x轴数据，平均值
    y_sub, time_x, avg = get_data(df, label_list, num=int(opt), col=int(opt) + 1, step=AVG)

    # 绘图
    c = drawing(time_x, y_sub, avg, title, date)

    dic = {
        "suss": 100,
        "opt": opt,
        "avg": AVG,
        "c": c
    }

    return JsonResponse(dic)


def get_opt_api(request):
    global OPT, AVG
    opt = request.POST.get('value')
    avg = request.POST.get('avg')
    OPT = opt
    if avg is None:
        avg = AVG
    else:
        AVG = AVG

    df = DF
    title = TITLE
    date = DATE
    labels = LABLES
    # 获取主标题、时间副标题、标签列表
    label_list = labels.values.tolist()

    # 获取图表标签头，x轴数据，平均值
    y_sub, time_x, avg = get_data(df, label_list, num=int(opt), col=int(opt)+1, step=AVG)

    # 绘图
    c = drawing(time_x, y_sub, avg, title, date)

    dic = {
        "suss": 100,
        "opt": opt,
        "avg": AVG,
        "c": c
    }
    return JsonResponse(dic)




def drawing(time_x, y_sub, avg, title, date):
    """
    绘制柱状图
    :param time_x: x轴标签数据
    :param y_sub: 该列的标签头
    :param avg: 平均值
    :param title: 主标题
    :param date: 时间副标题
    :return:
    """
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(time_x)
            .add_yaxis(y_sub, avg)
            .set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=date),
            datazoom_opts=opts.DataZoomOpts(type_="inside")
        )
            .set_series_opts(LabelOpts(is_show=False))
    ).render_embed()

    return c


def get_data(df, labels, num=0, raw=6, col=1, step=1):
    """
    获取图表标签头，x轴数据，平均值的数据值
    :param df: 上传得到的excel文件转换成的dataframe对象
    :param labels: 整个excel最上面每一列的列头 labels列表
    :param num: 列标签的第几个值
    :param raw: 行
    :param col: 列
    :param step: 步数
    :return: 获取该列的标签头 y_sub, 获取x轴标签数据 time_x, 平均值 avg
    """
    y_sub = labels[num]
    time_x = df.iloc[6:, 0].values.tolist()[step:-1:step]
    val_y = df.iloc[raw:, col].values.reshape((-1, step))  # y轴
    avg = np.mean(val_y, axis=1).tolist()

    return y_sub, time_x, avg
