from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Base de simulate data (en memory)
fake_db = [
    {"id": 1, "name": "Apple", "description": "Fruit amazing", "price": 1.0, "tax": 0.05},
    {"id": 2, "name": "Milk", "description": "The Best Milk", "price": 1.5},
    {"id": 3, "name": "Bread", "description": "One of the best bread", "price": 2.0, "tax": 0.10},
]


class Item(BaseModel): 
    id: int
    name: str
    description: Optional[str] = None 
    price: float
    tax: Optional[float] = None

# = Endpoints = #
@app.get("/")
async def read_root(): 
    """
      Endpoint To Welcome To The API
    """
    return {"message": "Welcome to my New API Application With FastAPI"}

@app.get("/items/", response_model=List[Item])
async def read_items(): 
    """
      Endpoint To Get All Items
    """
    return fake_db

@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: int): 
    """
       Endpoint To Get Item By ID
    """
    item = next((item for item in fake_db if item["id"] == item_id), None)
    if item is None: 
        raise HTTPException(status_code=404, details="Item Not Exist.")