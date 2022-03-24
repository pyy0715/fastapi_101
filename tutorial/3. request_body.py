# A request body is data sent by the client to your API. A response body is the data your API sends to the client.
# Your API almost always has to send a response body. But clients don't necessarily need to send request bodies all the time.
# To declare a request body, you use Pydantic models with all their power and benefits.

from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

# Import Pydantic's BaseModel
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    return item


# Use the model
## Inside of the function, you can access all the attributes of the model object directly:
@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


# Request body + path + query parameters
@app.put("/items/{item_id}")
async def create_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result
