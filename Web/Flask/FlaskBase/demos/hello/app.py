# 从flask包导入Flask类，这个类表示一个Flask程序
import click
from flask import Flask

# 实例化Flask类,得到程序实例app
app = Flask(__name__)


# 注册路由
@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


# 绑定多个url到同一个视图函数
@app.route('/hi')
@app.route('/hello')
def say_hello():
    return '<h1>Hi Flask!</h1>'


@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return f'<h1>Hi {name}!</h1>'


# @app.route('/greet')
# @app.route('/greet/<name>')
# def greet(name='Programmer'):
#     return f'<h1>Hi {name}!</h1>'


# 创建自定义命令
@app.cli.command()
def hello():
    click.echo('hello, human!')
