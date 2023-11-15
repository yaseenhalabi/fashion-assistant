
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
import math
import time 
import re

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

driver = webdriver.Chrome(options=chrome_options)

def getAllClothingData(num_of_items):
    
    links = getProductLinks('https://www.grailed.com/categories/all', num_of_items)

    listOfData = []
    count = 1
    for link in links:
    
        try:
            listOfData.append(scrapeProduct(link))
            print("[" + str(count) + "]" + " scraped " + link[42:55] + "...")
            count += 1
        except:
            print("Error! Could not scrape " + link[42:55] + "...")
    
    # removes any duplicates
    listOfData = [dict(t) for t in {tuple(d.items()) for d in listOfData}]
    print("finished scraping " + str(len(listOfData)) + " products")
    return listOfData

# returns list of links to products
def getProductLinks(url: str, num_of_items: int):
    
    driver.get(url) 

    wait = WebDriverWait(driver, 2).until(     
      EC.presence_of_element_located((By.CLASS_NAME, "feed")) 
    )

    # scroll to bottom to see more products
    num_of_scrolls = math.ceil((num_of_items-40)/40)  
    for i in range(num_of_scrolls):  
        ActionChains(driver)\
            .scroll_by_amount(0, 8000)\
            .perform()
        print("scrolled down page for more items")
        time.sleep(3)
     
    try: # driver.save_screenshot('screenshot.png')
        feed = driver.find_element(By.CLASS_NAME, "feed")
        feed_items = feed.find_elements(By.CLASS_NAME, "listing-item-link")
        links = list(map(lambda item: item.get_attribute("href"), feed_items[:num_of_items]))
        return links
    except OSError:
        return error


# returns dictionary of product data 
def scrapeProduct(url):
    
    data = {}
    
    data['url'] = url 
    driver.get(url)
   
    data['image'] = driver.find_element(By.CLASS_NAME, "Photo_photo__9PBT1").find_element(By.TAG_NAME, "img").get_attribute("src")
    # the sidebar contains all the good stuff
    sidebar = driver.find_element(By.CLASS_NAME, "MainContent_sidebar__29G6s")
    # get the basic data - tags, size, color, condition 
    basic_data = driver.find_element(By.CLASS_NAME, "MainContent_itemLeftColumn__gGKV9")
    
    data['price'] = sidebar.find_element(By.CLASS_NAME, "Money_root__8lDCT").text[1:]
    data['tags']= basic_data.find_element(By.CLASS_NAME, "Details_title__PpX5v").text
    
    # uses regex to isolate the size in US terms - S, M, L, or XXL

    size_info = basic_data.find_element(By.CLASS_NAME, "Details_value__S1aVR").text

    match = re.search(r'US\s+([A-Z0-9]+)', size_info)

    if match:
        data['size'] = match.group(1).lower()

    else:
        data['size'] = 'none'

    data['color'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[1].text.split()[-1].lower()

    data['condition'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[2].text.split()[-1].lower()
    try:
        data['description'] = " ".join(list(map(lambda x: x.text, sidebar.find_elements(By.CLASS_NAME, "ListingPage-Description-Body-Paragraph"))))
    except:
        data['description'] = "none"
    
    return data
