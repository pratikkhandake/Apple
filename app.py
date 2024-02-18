from flask import Flask, render_template, request, jsonify
import joblib
from config import port_number 

app = Flask(__name__)
model = joblib.load('apple.pkl')  # Load your trained model

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def prediction():
    try:
        # Extract input data from the form
        size = float(request.form['Size'])
        weight = float(request.form['Weight'])
        sweetness = float(request.form['Sweetness'])
        crunchiness = float(request.form['Crunchiness'])
        juiciness = float(request.form['Juiciness'])
        ripeness = float(request.form['Ripeness'])
        acidity = float(request.form['Acidity'])

        # Make prediction
        prediction = model.predict([[size, weight, sweetness, crunchiness, juiciness, ripeness, acidity]])
        
        # Map prediction to label
        predicted_label = 'Good' if prediction[0] == 1 else 'Bad'

        return jsonify({'Quality': predicted_label})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=port_number, debug=False)
