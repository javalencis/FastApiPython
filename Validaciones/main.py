from fastapi import FastAPI, Query
from typing import Union
app = FastAPI()


#Query parameters and String Validations
@app.get("/items/")
async def read_items(q: Union[str,None] = Query(default=None, min_length=1,max_length=50,regex="^<[a-zA-Z]$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results

