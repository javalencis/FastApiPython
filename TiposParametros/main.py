from typing import Union
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get('/')
async def root():
    return {"message":"Este es el root"}

@app.get('/users')
async def get_users():
    return {"users":
    [{
        "id":1,
        "name":"Jonathan"
    },{
        "id":2,
        "name":"Alexis"
    }]}

@app.get('/users/{user_id}')
async def get_user_id(user_id:int):
    return{"user_id":user_id}



#Se pasan los valores skip y limit por medio de la url
@app.get("/items/")
async def read_item(skip:int = 0,limit:int = 10):
    return fake_items_db[skip: skip+limit]

@app.get("/items/{item_id}")
async def read_item_id(item_id:str,q: Union[str,None] = None,short:bool=False):
    item = {"item_id":item_id} 
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"}) 

    return item

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(user_id:int,item_id:str,q: Union[str,None] = None,short:bool=False):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q":q})
    if not short:
        item.update({"description":"This is an amazing item that has a long description"}) 

    return item


@app.get("/item/{item_id}")
async def read_item_req(item_id:str,needy:str,skip:int=0,limit: Union[int,None]=None):
    item = {"item_id":item_id,"needy":needy,"skip":skip,"limit":limit}
    return item