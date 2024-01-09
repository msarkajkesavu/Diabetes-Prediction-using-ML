# Diabetes-Prediction-using-ML
# Diabetes Prediction Web Application

## Overview
This project implements a web application for predicting diabetes based on machine learning models. It uses a Random Forest classifier trained on a dataset containing features like age, hypertension, heart disease, gender, smoking history, BMI, HbA1c level, and blood glucose level.

## Usage
1. Clone the repository: `git clone https://github.com/arkajkesav/Diabetes-Prediction-using-ML.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the Flask application: `python app.py`
4. Open your web browser and go to http://127.0.0.1:5000/ to use the prediction form.

## Project Structure
- `app.py`: Flask application for serving the web pages and making predictions.
- `templates/`: Folder containing HTML templates for the web pages.
    - `index.html`: Form for user input.
    - `result.html`: Page displaying the prediction result.
- `diabetes_prediction_dataset.csv`: Dataset used for training the machine learning model.
- `requirements.txt`: List of Python dependencies.

## Notes
- Make sure to update the dataset file (`diabetes_prediction_dataset.csv`) if you have a different dataset.
- Customize the HTML templates to match your feature names and input requirements.
- Adjust the machine learning model and preprocessing as needed for your use case.

## Dependencies
- Flask
- pandas
- scikit-learn
- matplotlib
- seaborn
