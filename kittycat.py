from fastapi import FastAPI

from pydantic import BaseModel


class Items(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "kittycat World"}

@app.post("/items/")
async def create_item(item: Items):
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict
    