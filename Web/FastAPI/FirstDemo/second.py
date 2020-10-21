from fastapi import FastAPI

app = FastAPI()


# 二、路径参数

# 1.使用与Python格式化字符串相同的语法来申明路径参数或变量
# 路径参数item_id的值将作为参数item_id传递给函数
# 访问：http://127.0.0.1:8000/items/second
@app.get('/items/{item_id}')
async def second(item_id):
    return {'item_id': item_id}


# 2.有类型的路径参数
@app.get('/items_int/{item_id}')
async def second_1(item_id: int):
    return {'item_id': item_id}


# 创建路径操作时，顺序很重要
# 如下面两个接口，/users/me用来获取当前用户数据，/users/{user_id}用来通过用户ID获取特定用户的数据
# 路径操作时按顺序运行的，所以需要确保/users/me申明在/users/{user_id}之前
# 否则/users/{user_id}还将会与/users/me相匹配，接收一个值为me的user_id参数
@app.get('/users/me')
async def read_user_me():
    return {'user_id': 'the current user'}


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return {'user_id': user_id}


# 3.预设值
# 希望预先设定可能的有效参数值，则可以使用标准的Python Enum类型
# 创建一个Enum类
# 导入Enum并创建一个继承自str和Enum的子类
# 通过从str继承，API文档将能够知道这些值必须为string类型并且能够正确的展示出来
# 然后创建具有固定值的类属性，这些固定值将是可用的有效值
from enum import Enum


class ModelName(str, Enum):
    alexnet = 'alexnet'
    resnet = 'resnet'
    lenet = 'lenet'


@app.get('/model/{model_name}')
async def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {'model_name': model_name, 'message': 'Deep Learning FTW!'}
    if model_name.value == 'lenet':
        return {'model_name': model_name, 'message': 'LeCNN all the images'}
    return {'model_name': model_name, 'message': 'Hava some residuals'}


# 路径转换器
@app.get('/files/{file_path:path}')
async def read_file(file_path: str):
    return {'file_path': file_path}
