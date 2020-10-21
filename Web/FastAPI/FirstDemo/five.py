# 五、查询参数和字符串校验
from typing import Optional, List
from fastapi import FastAPI, Query

app = FastAPI()


# 查询参数q的类型是str，默认值为None，因此它是可选的
# @app.get('/items/')
async def read_items(q: Optional[str] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 额外校验
# 打算添加约束条件：即使q是可选的，但只要提供了该参数，则该参数的值不能超过50个字符的长度
# 1.导入Query
# @app.get('/items/')
# 2.使用Query作为默认值, 添加多个参数min_length, 添加正则表达式
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex='^fixedquery$')):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 默认值
# @app.get('/items/')
async def read_items(q: Optional[str] = Query('fixedquery', min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 必须参数
# 一般可不给可选参数赋值即可为必须参数
# Query中声明一个必须参数时，可以将 ... 用作第一个参数值
# @app.get('/items/')
async def read_items(q: str = Query(..., min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 查询参数列表/多个值
# @app.get('/items/')
async def read_items(q: Optional[List[str]] = Query(None)):
    query_items = {"q": q}
    return query_items


# 具有默认值得查询参数列表/多个值
# @app.get('/items/')
async def read_items(q: List[str] = Query(['foo', "bar"])):
    query_items = {"q": q}
    return query_items


# 使用list
# @app.get('/items/')
async def read_items(q: list = Query([])):
    query_items = {"q": q}
    return query_items


# 声明更多元数据
# @app.get('/items/')
async def read_items(q: Optional[str] = Query(None,
                                              title='Query string',
                                              description='Query string for the items to search in the database',
                                              min_length=3)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# 别名参数 alias
# 弃用参数 deprecated = True
@app.get('/items/')
async def read_items(q: Optional[str] = Query(None, alias="item-query", deprecated=True)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
