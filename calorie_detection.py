from flask import Flask, request, render_template
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Dummy data for model training (in a real scenario, use a larger dataset)
activities = ['walking', 'running', 'cycling']
durations = [30, 60, 45, 120, 15, 90, 10, 20, 35, 75]  
weights = [60, 70, 80, 90, 100, 70, 65, 55, 75, 85]   
calories_burned = [200, 600, 450, 800, 100, 250, 50, 150, 300, 500]  

# Prepare the data for model training
X = np.array([[1, 30, 60], [2, 60, 70], [3, 45, 80], [2, 120, 90], 
              [1, 15, 100], [3, 90, 70], [1, 10, 65], [2, 20, 55], 
              [1, 35, 75], [2, 75, 85]])  # activity as numerical encoding
y = np.array(calories_burned)

# Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train the model 
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_scaled, y)

@app.route('/')
def home():
    return render_template('index.html', prediction=None)

@app.route('/predict', methods=['POST'])
def predict():
    activity = request.form.get('activity')
    duration = request.form.get('duration', type=int)
    weight = request.form.get('weight', type=int)

    # Encode activity
    activity_mapping = {'walking': 1, 'running': 2, 'cycling': 3}
    activity_encoded = activity_mapping.get(activity, 0)

    # Scale input features
    input_features = np.array([[activity_encoded, duration, weight]])
    input_scaled = scaler.transform(input_features)

    # Make a prediction on given input
    prediction = model.predict(input_scaled)[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
