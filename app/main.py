from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()

@app.get("/")
async def home():
    """ Home Route for the application """
    return {"message": "Welcome to the API!"}

class Item(BaseModel):
    """ Item Model for Request Validation """
    name: str = Field(..., min_length=1, max_length=50, description="The name of the item")
    description: str = Field(..., max_length=200, description="A short description of the item")
    price: float = Field(..., gt=0, description="The price of the item")
    quantity: int = Field(..., ge=1, description="The quantity of the item available")

@app.post("/items/")
async def create_item(item: Item):
    """ Create Item Route """
    if item.quantity > 100:
        raise HTTPException(status_code=400, detail="Quantity cannot exceed 100")
    return {
        "message": "Item created successfully!",
        "item": item
    }

# Run the server using uvicorn
# `uvicorn filename:app --reload` in terminal
