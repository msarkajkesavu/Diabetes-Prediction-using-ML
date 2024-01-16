from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder, LabelEncoder
import numpy as np

app = Flask(__name__)

# Load the data
file_path = r"C:\Users\msark\Downloads\Diabetes-Prediction-using-ML-main\Diabetes-Prediction-using-ML-main\diabetes_prediction_dataset.csv"

df = pd.read_csv(file_path)

# Separate features and target variable
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Separate categorical and numerical features
categorical_features = ['gender', 'smoking_history']
numerical_features = [col for col in X.columns if col not in categorical_features]

# Preprocess categorical features using OneHotEncoder and handle_unknown
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ])

# Train a Random Forest
random_forest_model = RandomForestClassifier(n_estimators=100, random_state=42)

# Use the full preprocessing pipeline including OneHotEncoder
full_pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                                 ('classifier', random_forest_model)])

full_pipeline.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input from the form
        user_data = pd.DataFrame({
            'age': [float(request.form['age'])],
            'hypertension': [int(request.form['hypertension'])],
            'heart_disease': [int(request.form['heart_disease'])],
            'gender': [request.form['gender']],  # Include all columns
            'smoking_history': [request.form['smoking_history']],
            'bmi': [float(request.form['bmi'])],
            'HbA1c_level': [float(request.form['HbA1c_level'])],  # Use 'HbA1c_level'
            'blood_glucose_level': [int(request.form['blood_glucose_level'])]
        })

        # Make predictions using the trained model
        prediction = full_pipeline.predict(user_data)[0]

        return render_template('result.html', prediction=prediction)

    return render_template('index.html')

    return render_template('beauty.css')

if __name__ == '__main__':
    app.run(debug=True)
