from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="Sustain Backend API", version="0.1.0")

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

@app.get("/")
async def root():
    return {"message": "Welcome to Sustain Backend API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/items/")
async def create_item(item: Item):
    return {"item": item, "message": "Item created successfully"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, "item": item, "message": "Item updated successfully"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "message": "Item deleted successfully"}