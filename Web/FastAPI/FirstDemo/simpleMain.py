from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {'message': 'hello FastAPI'}


"""
uvicorn main:app --reload
    main: main.py文件（一个Python模块）
    app：在main.py文件中通过app = FastAPI()创建的对象
    --reload：让服务器在更新代码后重新启动。仅在开发时使用该选项
"""
