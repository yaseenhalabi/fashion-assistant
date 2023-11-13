

def meetsPreferences(product, preferences):
    if preferences['bot_size'] != None and preferences['top_size'] != None:
        if product['size'] != preferences['bot_size'] and product['size'] != preferences['top_size']:
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

def getMatches(selectedProducts, availableProducts, preferences):

    list_of_matching_products = []

    for product in availableProducts:
        if meetsPreferences(product, preferences):
            list_of_matching_products.append(product)

    return list_of_matching_products[:preferences['num_of_items']]
