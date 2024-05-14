from fastapi import FastAPI #, Header, Response #, Query
# from typing import Annotated
# from pydantic import BaseModel
# from typing import Union
import asyncio

app = FastAPI()

# @app.get("/sample")
# def read_root():
#     return {"message":"鈴木"}

# @app.get("/items/{item_id}")
# def read_item(item_id):
#     return {"item_id": item_id, "item_name": "Tシャツ"}


# items = ["Tシャツ","スカート","ブーツ","コート"]
# @app.get("/items")
# def read_item(skip: int = 0, limit: Annotated[int, Query(ge=1, le=10)] = 10):
#     return {"items": items[skip : skip + limit]}

# class Item(BaseModel):
#     name: str
#     price: float
#     description: Union[str,None]= None
    
# @app.post("/items/")
# def create_item(item: Item):
#     print(f"データを登録します: {item.name},{item.price},{item.description}")
#     return item

# @app.get("/sample/")
# def read_sample(
#     response: Response,
#     authorization: Union[str, None] = Header(default = None)
# ):
#     print(authorization)
#     response.headers["custom-header"] = "12345"
#     return {"message": "ヘッダー情報を取得しました"}

@app.get("/sleep_time/")
async def sleep_time(sec: int):
    await asyncio.sleep(sec)
    return{"message":f"{sec}秒"}