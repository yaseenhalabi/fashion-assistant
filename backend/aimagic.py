#get list of tagged product objects
#scrape a hundred to a thousand products
#use tagged products to determine which of the thousand new products match

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
import numpy as np
import json

def preprocess_data(tagged_data, untagged_data):
    """
    Convert JSON data into a format suitable for machine learning.
    """
    # Combine all data for consistent preprocessing
    all_data = tagged_data + untagged_data
    
    # Vectorize tags and description using TF-IDF
    tfidf_tags = TfidfVectorizer(max_features=100)
    tfidf_desc = TfidfVectorizer(max_features=100)
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
    y = np.array([d['rating'] for d in tagged_data])
    
    return X_tagged, y, X_untagged

# Sample data for testing the preprocessing function

untagged_sample = [
    {
        "rating": 5,
        "color": "green",
        "condition": "used",
        "size": "US M",
        "image": "url2",
        "price": "$30",
        "url": "url2",
        "tags": "green shirt vintage",
        "description": "A vintage green shirt."
    }
]
 
  
tagged_sample = [
    {
        "rating": 5,
        "color": "green",
        "condition": "used",
        "size": "US M",
        "image": "url2",
        "price": "$30",
        "url": "url2",
        "tags": "green shirt vintage",
        "description": "A vintage green shirt."
    }
]
preprocess_data(tagged_sample, untagged_sample)


from sklearn.ensemble import RandomForestRegressor

def select_top_clothes(tagged_data, untagged_data):
    # Preprocess the data
    X_tagged, y, X_untagged = preprocess_data(tagged_data, untagged_data)
    
    # Train a regression model
    model = RandomForestRegressor(n_estimators=100)
    model.fit(X_tagged, y)
    
    # Predict ratings for the untagged data
    predicted_ratings = model.predict(X_untagged)
    
    # Get indices of top 10 predicted ratings
    top_indices = np.argsort(predicted_ratings)[-10:][::-1]
    
    # Return top 10 items
    return [untagged_data[i] for i in top_indices]

# Testing with the sample data (This won't be very meaningful with just one sample, but it's for testing purposes)
print(select_top_clothes(tagged_sample, untagged_sample))


