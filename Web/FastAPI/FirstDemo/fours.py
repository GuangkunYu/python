# 四、请求体
from fastapi import FastAPI
from typing import Optional
# 1.导入Pydantic的BaseModel
from pydantic import BaseModel


# 创建数据模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


# 声明为参数
# @app.post('/items/')
async def create_item(item: Item):
    # 使用模型
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# 请求体+路径参数
# @app.put('/items/{item_id}')
async def create_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


# 请求体+路径参数+查询参数
@app.put('/items/{item_id}')
async def create_item(
        item_id: int,
        item: Item,
        q: Optional[str] = None
):
    result = {
        "item_id": item_id,
        **item.dict()
    }
    if q:
        result.update({'q': q})
    return result
