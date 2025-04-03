from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

#  database 
items = []

#  model for item data
class Item(BaseModel):
    name: str
    description: str

# Add an item
@app.post("/items/", response_model=Item)
async def add_item(item: Item):
    items.append(item)
    return item

#get item 
@app.get("/items/{id}", response_model=Item)
async def get_item(id: int):
    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    return items[id]

#update item 
@app.put("/items/{id}", response_model=Item)
async def update_item(id: int, item: Item):
    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    items[id] = item
    return item

#delete item

@app.delete("/items/{id}", response_model=Item)
async def delete_item(id: int):
    if id < 0 or id >= len(items):
        raise HTTPException(status_code=404, detail="Item not found")
    
    deleted_item = items.pop(id)
    return deleted_item