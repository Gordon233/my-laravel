from typing import Union
from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def process_excel(data: dict):
    # 模拟长时间处理
    time.sleep(10)
    # 这里应该是你的pandas处理逻辑
    print(f"Processing excel data: {data}")


@app.get("/")
def read_root():
    return {"Hello": "World!!!!!"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/hello")
def hello_from_fastapi():
    return {"message": "Hello from FastAPI"}


# 新增的异步处理端点
@app.post("/process-excel")
async def process_excel_endpoint(data: dict, background_tasks: BackgroundTasks):
    background_tasks.add_task(process_excel, data)
    return {"message": "Excel processing started"}
