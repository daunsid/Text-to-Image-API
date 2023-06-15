from fastapi import FastAPI
from pydantic import BaseModel


# create an instance of the app
app = FastAPI()

#create a root route path
@app.get('/')
def read_root():
    #return json response
    return {"Hello":"world"}


@app.get("/items/{item_id}")
def read_item(item_id: int):

    return {"item_id":item_id, "message":"ML app"}


class Item(BaseModel):
    name: str
    price: float
    tags: list[str]

@app.post("/items/")
def create_item(item: Item):
    return item