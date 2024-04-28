from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import match
import sample_data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.post("/api/getProducts")
def getProducts(
    # frontend calls this to get the products that match the user's preferences.
    # Returns: a list of products that match the user's preferences.
        selected_images: list[str], 
        num_of_items: int = Query(None, title="num_of_items"),
        top_size: str = Query(None, title="top_size"),
        bot_size: int = Query(None, title="bot_size"),
        color: str = Query(None, title="color"),
        min_condition: str = Query(None, title="min_condition"),
        min_price: str = Query(None, title="min_price"),
        max_price: str = Query(None, title="max_price")
    ):
    preferences = {
        'num_of_items': num_of_items, 
        'top_size': top_size,
        'bot_size': bot_size,
        'color': color,
        'min_condition': min_condition,
        'min_price': min_price,
        'max_price': max_price
    }
    all_products = sample_data.getData() # whatever data we are tagging
    matched_with_preferences = match.getMatches(preferences=preferences, available_products=all_products)
    return matched_with_preferences

@app.get("/")
def home():
    return {"message": "hello world"}




