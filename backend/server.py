from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# import scrape
#fix scrape it has error with chromedriver!!!!
import aimagic
import sample_data1
import sample_data2
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
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

@app.post("/api/getProductMatches/{num_of_items}")
def getProductMatches(num_of_items: int, prefererred_clothes: list[PrefererredClothes]):
    
    #gets untagged data from data.py
    untagged = sample_data1.getData()

    tagged = [convertToUsableJson(i.model_dump_json()) for i in prefererred_clothes]

    matches = aimagic.select_top_clothes(tagged_data=tagged, untagged_data=untagged, num_of_items=num_of_items)
    
    return matches


@app.get("/api/getProducts/{num_of_items}")
def getAvailableProducts(num_of_items: int):

    try:
        # dataList = scrape.getAllClothingData(num_of_items) 
        dataList = sample_data2.getData()[:num_of_items]

    except:
        return "there was an error scraping clothes"

    return dataList

@app.get("/")
def home():
    return {"message": "hello world"}


