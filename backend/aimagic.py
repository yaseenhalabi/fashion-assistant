#get list of tagged product objects
#scrape a hundred to a thousand products
#use tagged products to determine which of the thousand new products match
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np

def preprocess_data(tagged_data, untagged_data):
    """
    Convert JSON data into a format suitable for machine learning.
    """
    # Combine all data for consistent preprocessing
    all_data = tagged_data + untagged_data
    
    # Vectorize tags and description using TF-IDF
    tfidf_tags = TfidfVectorizer(max_features=3)
    tfidf_desc = TfidfVectorizer(max_features=20)
    tags_matrix = tfidf_tags.fit_transform([d['tags'] for d in all_data])
    desc_matrix = tfidf_desc.fit_transform([d['description'] for d in all_data])
    
    # Convert categorical features into numerical labels
    le_color = LabelEncoder()
    le_condition = LabelEncoder()
    le_size = LabelEncoder()
    colors = le_color.fit_transform([d['color'] for d in all_data])
    conditions = le_condition.fit_transform([d['condition'] for d in all_data])
    sizes = le_size.fit_transform([d['size'] for d in all_data])
    
    # Normalize price
    scaler = MinMaxScaler()
    prices = scaler.fit_transform(np.array([float(d['price'][1:]) for d in all_data]).reshape(-1, 1))
    
    # Construct feature matrix
    X = np.hstack((
        tags_matrix.toarray(), 
        desc_matrix.toarray(), 
        colors.reshape(-1, 1), 
        conditions.reshape(-1, 1), 
        sizes.reshape(-1, 1), 
        prices
    ))
    
    # Split back into tagged and untagged data
    X_tagged = X[:len(tagged_data)]
    X_untagged = X[len(tagged_data):]
    
    # Extract ratings for tagged data
    y = np.array([int(d['rating']) for d in tagged_data])
    
    return X_tagged, y, X_untagged


from sklearn.ensemble import RandomForestRegressor

def select_top_clothes(tagged_data, untagged_data, num_of_items):
    # Preprocess the data
    X_tagged, y, X_untagged = preprocess_data(tagged_data, untagged_data)
    
    # Train a regression model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_tagged, y)
    
    # Predict ratings for the untagged data
    predicted_ratings = model.predict(X_untagged)
    
    # Get indices of top 10 predicted ratings
    top_indices = np.argsort(predicted_ratings)[-(num_of_items):][::-1]
    
    # Return top 10 items
    return [untagged_data[i] for i in top_indices]

# Testing with the sample data (This won't be very meaningful with just one sample, but it's for testing purposes)



# Sample data for testing the preprocessing function
untagged_sample = [
    {
        "url": "https://www.grailed.com/listings/51148652-nike-x-nike-acg-x-outdoor-life-nike-acg-outdoor-hiking-mountain-jacket-recco-system?g_aidx=Listing_production&g_aqid=e0d7161859767ce3bbe57f3fca6babca",
        "image": "https://media-assets.grailed.com/prd/listing/48098874/96314e64085d4b3c8bf3167601acb350?h=700&fit=clip&auto=format",
        "price": "$109",
        "tags": "Nike ACG outdoor hiking mountain jacket RECCO system",
        "size": "US M",
        "color": "Pink",
        "condition": "Used",
        "description": "Nike ACG women’s jacket\nSize M\nGood condition"
    }, 
] 
tagged_sample =[
    {
        "url": "https://www.grailed.com/listings/48199030-bomber-jacket-x-japanese-brand-x-vintage-vintage-lisburn-wool-bomber-jacket?g_aidx=Listing_production&g_aqid=8c750efc17dc04738bb71e9f05840a30",
        "image": "https://media-assets.grailed.com/prd/listing/48199030/7ee4f3b5913d4652a993e9ef8cd9e764?w=525&h=700&fit=clip&auto=format",
        "price": "$175",
        "tags": "Vintage Lisburn Wool Bomber Jacket",
        "size": "US M",
        "color": "Red",
        "condition": "Used",
        "description": "Ref. Item : PH6 SIZE ON TAG : Medium MANUAL MEASUREMENT ( INCHES ) Armpit : 25 Inches Length : 24 Inches CONDITION 7/10 See Picture For More Detail PAYMENT We accept Paypal only. The item will be sent within 2-5 days after payment is completed. SHIPPING Transit time can take 5-7(DHL Express) days to reach destination. REFUNDS Refunds are given only if items are not as described. No refunds for wrong sizes so please check and compare measurements to something you own before bidding. Most of my items are Vintage/Used Items, so please check pictures and ask questions. Thank You.",
        "rating": "5"
    }
    
]
# print(select_top_clothes(tagged_sample, untagged_sample))





