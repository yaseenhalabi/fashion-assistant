import random

def meetsPreferences(product, preferences):
    if preferences['bot_size'] is not None or preferences['top_size'] is not None: 
        if product['size'] is not str(preferences['bot_size']) and product['size'] is not preferences['top_size']:
            return False

    if preferences['color'] is not None:
        if (product['color'] is not preferences['color']):
            return False
    
    if preferences['min_condition'] is not None:
        if preferences['min_condition'] == 'new' and product['condition'] == 'used':
            return False
    
    if preferences['min_price'] is not None:
        if int(preferences['min_price']) > int(product['price']):
            return False
     
    if preferences['max_price'] is not None:
        if int(preferences['max_price']) < int(product['price']):
            return False
    return True

def getMatches(available_products, preferences):

    list_of_matching_products = []
    list_of_matching_products = [product for product in available_products if meetsPreferences(product, preferences)]
    random.shuffle(list_of_matching_products)
    return list_of_matching_products[:preferences['num_of_items']]


