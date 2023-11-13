from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import scrape
import aimagic
import sample_data1
import sample_data2

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)




class PrefererredClothes(BaseModel):
    url: str
    price: str 
    tags: str
    condition: str
    size: str
    color: str
    description: str 
    image: str



@app.post("/api/getProductMatches")
def getProductMatches(
        prefererred_clothes: list[PrefererredClothes], 
        num_of_items: int = Query(None, title="num_of_items"),
        top_size: str = Query(None, title="top_size"),
        bot_size: int = Query(None, title="bot_size"),
        color: str = Query(None, title="color"),
        min_condition: str = Query(None, title="min_condition"),
        min_price: str = Query(None, title="min_price")
        
    ):
    
    return num_of_items


@app.get("/api/getProducts")
def getAvailableProducts(
        num_of_items: int = Query(title="num_of_items")
    ):

    try:
        dataList = scrape.getAllClothingData(num_of_items) 
        # dataList = sample_data2.getData()[:num_of_items]

    except:
        return "there was an error scraping clothes"

    return dataList

@app.get("/")
def home():
    return {"message": "hello world"}


