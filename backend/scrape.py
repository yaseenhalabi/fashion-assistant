from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import math
import time 
import re
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

def getAllClothingData(num_of_items):
    """
    runs the scraping functions to get all the clothing data
    returns: a list of dictionaries containing the data
    """
    listOfData = []
    links = getProductLinks('https://www.grailed.com/categories/all', num_of_items)
    count = 1
    for link in links:
        try:
            listOfData.append(scrapeProduct(link))
            print("[" + str(count) + "]" + " scraped " + link[42:55] + "...")
            count += 1
        except:
            # If 'link' is None, the slicing will not be attempted.
            print("Error! Could not scrape the product.")

    print("finished scraping " + str(len(listOfData)) + " products")
    return listOfData

def getProductLinks(url: str, num_of_items: int):
    """
    Scrapes the product links from given url.
    returns: string list of urls
    """
    links = []
    driver.get(url) 
    num_of_scrolls = math.ceil((num_of_items-40)/40)  
    for i in range(num_of_scrolls):  
        ActionChains(driver)\
            .scroll_by_amount(0, 8000)\
            .perform()
        print("scrolled down page for more items")
        time.sleep(3)
    feed = driver.find_element(By.CLASS_NAME, "feed")
    feed_items = feed.find_elements(By.CLASS_NAME, "listing-item-link")
    links = [item.get_attribute("href") for item in feed_items[:num_of_items]] 
    return links


def scrapeProduct(url):
    """
    Scrapes the product page for the following data:
    image-url, price, tags, size, color, condition
    returns: a dictionary of the data
    """
    data = {}
    data['url'] = url 
    driver.get(url)
    data['image'] = driver.find_element(By.CLASS_NAME, "Photo_photo__9PBT1").find_element(By.TAG_NAME, "img").get_attribute("src")
    sidebar = driver.find_element(By.CLASS_NAME, "MainContent_sidebar__29G6s")
    basic_data = driver.find_element(By.CLASS_NAME, "MainContent_itemLeftColumn__gGKV9")
    data['price'] = sidebar.find_element(By.CLASS_NAME, "Money_root__8lDCT").text[1:]
    data['tags']= basic_data.find_element(By.CLASS_NAME, "Details_title__PpX5v").text
    size_info = basic_data.find_element(By.CLASS_NAME, "Details_value__S1aVR").text
    match = re.search(r'US\s+([A-Z0-9]+)', size_info)
    data['size'] = match.group(1).lower() if match else 'none'
    data['color'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[1].text.split()[-1].lower()
    data['condition'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[2].text.split()[-1].lower()
    return data


data = getAllClothingData(45)

keys = data[0].keys()

with open('clothing_data.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully.")