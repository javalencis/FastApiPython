from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name:str
    lastname:str
    description: Union[str,None]=None
    price: float
    tax: Union[float,None] = None


app = FastAPI()

@app.post("/items/{item_id}")
async def create_item(item_id:int,item:Item):
    item_dict = item.dict()
    result = {"item_id":item_id,**item_dict}
    if item.tax:
        price_with_tax= item.tax+item.price
        result.update({"price_with_tax":price_with_tax})

    return result
