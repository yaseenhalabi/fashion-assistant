from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import scrape
import match
import sample_data
#
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)


@app.post("/api/getProductMatches")
def getProductMatches(
        selected_images: list[str], 
        num_of_items: int = Query(None, title="num_of_items"),
        top_size: str = Query(None, title="top_size"),
        bot_size: int = Query(None, title="bot_size"),
        color: str = Query(None, title="color"),
        min_condition: str = Query(None, title="min_condition"),
        min_price: str = Query(None, title="min_price"),
        max_price: str = Query(None, title="max_price")
    ):
    
    available_products = sample_data.getData()
    matches = []
    preferences = {
        'num_of_items': num_of_items, 
        'top_size': top_size,
        'bot_size': bot_size,
        'color': color,
        'min_condition': min_condition,
        'min_price': min_price,
        'max_price': max_price
    }

    matches = match.getMatches(preferences=preferences, selected_images=selected_images, available_products=available_products)
    return matches

# This will likely not be used for real time product searching, only to get data for storing
@app.get("/api/getProducts")
def getAvailableProducts(
        num_of_items: int = Query(title="num_of_items")
    ):
    try:
        productObjects = scrape.getAllClothingData(num_of_items) 
    except:
        raise HTTPException(status_code=500, detail="There was an error scraping")

    return productObjects

@app.get("/")
def home():
    return {"message": "hello world"}

    
