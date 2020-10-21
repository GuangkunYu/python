from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get('/')
def read_root():
    return {'hello': 'world'}


@app.get('/items/{item_id}')
def read_item(item_id: int, q: Optional[str] = None):
    return {'item_id': item_id, 'q': q}


# if __name__ == '__main__':
#     import uvicorn
#
#     uvicorn.run(app, host='127.0.0.1', port=8000)
