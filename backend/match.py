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
    return []

def getMatches(selected_images, available_products, preferences):

    list_of_matching_products = []

    for product in available_products:
        if meetsPreferences(product, preferences):
            list_of_matching_products.append(product)
            
    # Randomly shuffling items to make each page refresh unique
    random.shuffle(list_of_matching_products)
    return list_of_matching_products[:preferences['num_of_items']]


