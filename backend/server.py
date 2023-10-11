
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import scrape
from pydantic import BaseModel

class PrefererredClothes(BaseModel):
    opinion: str
    name: str
    price: str 
    tags: str
    size: str
    color: str
    description: str 
    image: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
@app.post("/findNewProducts{depth}")
def findNewProducts(depth: int, prefererred_clothes: list[PrefererredClothes]): 
    dataList = scrape.getAllClothingData(depth)
    
    for clothing_item in prefererred_clothes:
        print("preference noted")
    return prefererred_clothes 

@app.get("/api/getAvailableProducts")
def getAvailableProducts():
    try:
        dataList = scrape.getAllClothingData(0)
        print(len(dataList))
    except:
        return "there was an error scraping clothes"
    return dataList

@app.get("/")
def home():
    return "HOME ROUTE"
