
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

import time 
import re

chrome_options = Options()
chrome_options.add_argument("--headless")

chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")
driver = webdriver.Chrome(options=chrome_options)

def getAllClothingData(depth):
    print("getting links...")
    
    # every scroll is 20 products!!

    links = list(set(getProductLinks('https://www.grailed.com/categories/all', depth)))

    listOfData = []

    for link in links:
        try:
            listOfData.append(scrapeProduct(link))
        except:
            print("could not scrape " + link)

    print("scraped " +str(len(links))+ " products...") 

    return listOfData

# returns list of links to products
def getProductLinks(url, num_of_scrolls):

    driver.get(url)
    time.sleep(1)
    # scroll to bottom to see more products
    SCROLL_WAIT_TIME = .5
    for i in range(num_of_scrolls):
        ActionChains(driver)\
            .scroll_by_amount(0, 3000)\
            .perform()
        time.sleep(SCROLL_WAIT_TIME)
    
    try:

        # driver.save_screenshot('screenshot.png')
        product_element_container = driver.find_element(By.CLASS_NAME, "feed")
        product_elements = product_element_container.find_elements(By.CLASS_NAME, "listing-item-link")
        
        product_links = list(map(lambda element: element.get_attribute("href"), product_elements))

        return product_links
    except:
        print("could not find elements :(")
        return []


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
    
    data['price'] = sidebar.find_element(By.CLASS_NAME, "Money_root__8lDCT").text
    data['tags']= basic_data.find_element(By.CLASS_NAME, "Details_title__PpX5v").text
    
    # uses regex to isolate the size in US terms - S, M, L, or XXL

    size_info = basic_data.find_element(By.CLASS_NAME, "Details_value__S1aVR").text

    match = re.search(r'US (\w+)', size_info)
   
    if match:
        data['size'] = match.group()
    else:
        data['size'] = "none" 

    data['color'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[1].text.split()[-1]

    data['condition'] = basic_data.find_elements(By.CLASS_NAME, "Details_nonMobile__AObqX")[2].text.split()[-1]
   
    # get measurements 
    # try:
    #
    # except:

    # now that we are done getting the basic stuff, on to the description...
    try:
        data['description'] = " ".join(list(map(lambda x: x.text, sidebar.find_elements(By.CLASS_NAME, "ListingPage-Description-Body-Paragraph"))))
    except:
        data['description'] = "none"
    print("scraped " + data['tags'])

    return data
# getAllClothingData(2
