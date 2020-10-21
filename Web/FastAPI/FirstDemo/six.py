# 六、路径参数和数值校验
from typing import Optional
from fastapi import FastAPI, Path, Query

app = FastAPI()


# 与使用Query为查询参数声明更多的校验和元数据的方式相同，
# 也可以使用path为路径参数声明相同类型的校验和元数据
@app.get('/items/{item_id}')
async def read_item(
        item_id: int = Path(..., title='The ID of the item to get'),
        q: Optional[str] = Query(None, alias='item-query')
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
