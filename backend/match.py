import random

def meetsPreferences(product, preferences):
    if preferences['bot_size'] != None or preferences['top_size'] != None:
        if product['size'] != str(preferences['bot_size']) and product['size'] != preferences['top_size']:
            return False

    if preferences['color'] != None:
        if (product['color'] != preferences['color']):
            return False
    
    if preferences['min_condition'] != None:
        if preferences['min_condition'] == 'new' and product['condition'] == 'used':
            return False
    
    if preferences['min_price'] != None:
        if int(preferences['min_price']) > int(product['price']):
            return False
     
    if preferences['max_price'] != None:
        if int(preferences['max_price']) < int(product['price']):
            return False
    return True


def sortByRelevance(available_products, selected_images):
    # insert code here
    return []

def getMatches(selected_images, available_products, preferences):

    list_of_matching_products = []

    for product in available_products:
        if meetsPreferences(product, preferences):
            list_of_matching_products.append(product)
            
    # list_of_matching_products = sortByRelavance(available_products=available_products, selected_images=selected_images)

    # Randomly shuffling items to make each page refresh unique
    random.shuffle(list_of_matching_products)
    return list_of_matching_products[:preferences['num_of_items']]


import sample_data

sample_products = sample_data.getData()
sample_images = ["https://media-assets.grailed.com/prd/listing/44972277/944c4e0bc87743088c6b3f68b3150b77?w=1050&h=1400&fit=clip&q=20&auto=format"]

if __name__ == "main":
    sortByRelevance(sample_products, sample_images)
