from fastapi import FastAPI

app = FastAPI()

fake_items_db = [
    {'item_name': 'Foo'},
    {'item_name': 'Bar'},
    {'item_name': 'Baz'}
]


# 三、查询参数
# 声明不属于路径参数的其他函数参数时，他们将被自动解释为“查询字符串”参数
# 查询字符串是键值对的集合，这些键值对位于URL的？之后，并以&符号分割
# 例如：http://127.0.0.1:8000/items/?skip=0&limit=10
# @app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


# 可选参数
# 可以将他们的默认值设为None来声明可选查询参数
from typing import Optional


# @app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {'item_id': item_id, 'q': q}
    return {'item_id': item_id}


# 查询参数类型转换
# 声明bool类型，他们将会被自动转换
# @app.get('/items/{item_id}')
async def read_item(item_id: str, q: Optional[str] = None, short: bool = False):
    item = {'item_id': item_id}
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {'description': 'this is an amazing item that has a long description'}
        )
    return item


# 多个路径和查询参数
# @app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(
        user_id: int,
        item_id: str,
        q: Optional[str] = None,
        short: bool = False
):
    item = {
        "item_id": item_id,
        "owner_id": user_id,
    }
    if q:
        item.update({'q': q})
    if not short:
        item.update(
            {
                'description': 'this is an amazing item that has a long description'
            }
        )
    return item


# 必须查询参数
# 为非路径参数声明了默认值时（目前仅查询参数），则该参数不是必须的
# 参数是可选的时候，则将默认值设为None
# 让查询参数成为必须的，不声明任何默认值即可
# @app.get('/items/{item_id}')
async def read_user_item(item_id: str, needy: str):
    item = {
        "item_id": item_id,
        "needy": needy
    }
    return item


# 可以定义一些参数是必须的，一些事可选的
@app.get('/items/{item_id}')
async def read_user_item(
        item_id: str, needy: str, skip: int = 0, limit: Optional[int] = None
):
    item = {
        "item_id": item_id,
        "needy": needy,
        "skip": skip,
        "limit": limit
    }
    return item
