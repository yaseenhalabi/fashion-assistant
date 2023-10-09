
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import threading
import time 
import re

driver = webdriver.Chrome()

def main():
    print("getting links...")
    
    # every scroll is 20 products!!
    scrollDepth = 5

    links = getProductLinks('https://www.grailed.com/categories/all', scrollDepth)
    print("scraping " +str(len(links))+ " products...") 

    for link in links:
        try:
            scrapeProduct(link)
        except:
            print("there was an error scraping this product: " + link)


# returns list of links to products
def getProductLinks(URL, NUM_OF_SCROLLS):

    driver.get(URL)
    time.sleep(1)
    # scroll to bottom to see more products
    scroll_to_me = driver.find_element(By.TAG_NAME, "footer")
    SCROLL_WAIT_TIME = 1
    for i in range(NUM_OF_SCROLLS):
        ActionChains(driver)\
            .scroll_by_amount(0, 3000)\
            .perform()
        time.sleep(SCROLL_WAIT_TIME)
    

    product_element_container = driver.find_element(By.CLASS_NAME, "feed")
    product_elements = product_element_container.find_elements(By.CLASS_NAME, "listing-item-link")
    
    product_links = list(map(lambda element: element.get_attribute("href"), product_elements))

    return product_links



# returns dictionary of product data 
def scrapeProduct(URL):
    
    data = {}
    
    data['url'] = URL 
    driver.get(URL)
    
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

    # now that we are done getting the basic stuff, on to the description...
    try:
        data['description'] = " ".join(list(map(lambda x: x.text, sidebar.find_elements(By.CLASS_NAME, "ListingPage-Description-Body-Paragraph"))))
    except:
        data['description'] = "none"
    print(data)
    print()
    
if __name__ == "__main__":
    start_time = time.time() 
    main()  
    
    print("end time: " + str(time.time()-start_time))
