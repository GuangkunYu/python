# 一、使用步骤

# 1.导入FastAPI
from fastapi import FastAPI

# 2.创建一个FastAPI实例
# 这个实例是创建所有API的主要交互对象
# app同样在启动服务时被引用
app = FastAPI()


# 3.创建一个路径操作
# 路径指的是URL中从第一个/起的后半部分
# url    https://127.0.0.1/items/foo
# 路径   /items/foo
# 路径通常也被称为端点或路由
# 开发API时，路径是用来分离关注点和资源的主要手段
# 操作：是指http方法 --- post创建数据、get读取数据、put更新数据、delete删除数据 以及options、head、patch、trace
# 定义一个路径操作装饰器
# @app.get('/')告诉FastAPI在它下方的函数负责处理如下访问请求
# 请求路径为 /
# 使用get操作
# @app.get()  @app.post()   @app.put()   @app.delete()
@app.get('/')
# 4.定义路径操作函数   路径：/  操作：get   函数：位于装饰器下方
async def first():
    # 5.返回内容
    return {'first': 'FastAPI创建步骤'}


"""
FastAPI使用步骤总结：
    1.导入FastAPI
    2.创建一个app实例
    3.编写一个路径操作装饰器（如：@app.get('/')）
    4.编写一个路径操作函数（如：async def first()）
    5.运行开发服务器（如：uvicorn main:app --reload）
"""
