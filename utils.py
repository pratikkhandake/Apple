import pickle

# Load the trained decision tree model
with open('apple.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

def predict_quality(data):
    # Extract features
    features = [float(data['Size']), float(data['Weight']), float(data['Sweetness']), 
                float(data['Crunchiness']), float(data['Juiciness']), float(data['Ripeness']), 
                float(data['Acidity'])]

    # Make prediction
    prediction = model.predict([features])[0]

    # Map prediction to 'good' or 'bad'
    quality = 'good' if prediction == 1 else 'bad'

    return quality
