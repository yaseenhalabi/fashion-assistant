from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import scrape
import aimagic
import data
from pydantic import BaseModel
import json

class PrefererredClothes(BaseModel):
    rating: str
    url: str
    price: str 
    tags: str
    condition: str
    size: str
    color: str
    description: str 
    image: str

def convertToUsableJson(x):
    item = json.loads(x)
    print(item)
    return {
        "rating": item['rating'],
        "url": item['url'],
        "image": item["image"],
        "price": item["price"],
        "tags": item["tags"],
        "size": item["size"],
        "color": item["color"],
        "condition": item["condition"],
        "description": item["description"]
    }


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/api/findNewProducts/{depth}")
def findNewProducts(depth: int, prefererred_clothes: list[PrefererredClothes]):

    untagged = data.getData()
    tagged = [convertToUsableJson(i.json()) for i in prefererred_clothes]

    matches = aimagic.select_top_clothes(tagged_data=tagged, untagged_data=untagged)

    return matches


@app.get("/api/getAvailableProducts/{num_of_items}")
def getAvailableProducts(num_of_items: int):

    try:
        dataList = scrape.getAllClothingData(num_of_items)

    except:
        return "there was an error scraping clothes"

    return dataList

@app.get("/")
def home():
    return "HOME ROUTE"
