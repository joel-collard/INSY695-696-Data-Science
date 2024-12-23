from flask import Flask, render_template, request
import joblib
import webbrowser
import threading
import numpy as np
import pandas as pd
import lightgbm as lgb

app = Flask(__name__)

# Load the model
model = joblib.load('lightgbm_model_HP_t+12.pkl')

# Define categorical features
categorical_features = ['Province', 'Home_Type']

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get dropdown selections
            home_type = request.form.get('home_type')  # Match name in HTML
            province = request.form.get('province')  # Match name in HTML

            # print("Debug values:")
            # print("home_type:", request.form.get('home_type'))
            # print("province:", request.form.get('province'))
            # print("overnight_rate:", request.form.get('overnight_rate'))
            # print("cpi_shelter:", request.form.get('cpi_shelter'))
            # print("cpi_all_change_lag_12:", request.form.get('cpi_all_change_lag_12'))
            # print("cpi_shelter_change_lag_12:", request.form.get('cpi_shelter_change_lag_12'))
            # print("population_growth_lag_12:", request.form.get('population_growth_lag_12'))

            # Get numeric inputs and convert to float
            overnight_rate = float(request.form.get('overnight_rate', 0))
            cpi_shelter_change_lag_12 = float(request.form.get('cpi_shelter_change_lag_12', 0))
            population_growth_lag_12 = float(request.form.get('population_growth_lag_12', 0))
            cpi_shelter = float(request.form.get('cpi_shelter', 0))
            home_starts = float(request.form.get('home_starts', 0))

            # Load data from CSV
            data = pd.read_csv('data.csv')

            subset_data = data[(data['Home_Type'] == home_type) & (data['Province'] == province)]
            most_recent_date = subset_data['Year_Month_Day'].max()
            recent_data = subset_data[subset_data['Year_Month_Day'] == most_recent_date]

            # print("recent_data dtypes:")
            # print(recent_data.dtypes)
            # print("recent_data sample:")
            # pd.set_option('display.max_columns', None)
            # print(recent_data.head())

            # # Check if required columns are present
            # print("Feature names from the model:")
            # print(model.booster_.feature_name())

            if recent_data.empty or 'HP_Lag_12' not in recent_data.columns or 'Home_Price' not in recent_data.columns:
                return "Required data is missing for the selected home type and province."
            
            # Convert categorical columns to category dtype
            for feature in categorical_features:
                recent_data[feature] = recent_data[feature].astype('category')

            # Construct input DataFrame
            input_data = pd.DataFrame({
                'Overnight_Rate': [overnight_rate],
                'CPI_Shelter_Change_Lag_12': [cpi_shelter_change_lag_12],
                'Population_Growth_Lag_12': [population_growth_lag_12],
                'Province': [province],
                'CPI_Shelter': [cpi_shelter],
                'Home_Type': [home_type],
                'Home_Starts': [home_starts],
                'HP_Lag_12': recent_data['HP_Lag_12'].values,
                'Home_Price': recent_data['Home_Price'].values               
            })

            # Set categorical dtype
            for feature in categorical_features:
                if feature in input_data.columns:
                    input_data[feature] = input_data[feature].astype('category')

            # print("Input data:")
            pd.set_option('display.max_columns', None)  
            print(input_data)
            print("recent_data dtypes:")
            print(input_data.info())

            # Check if required columns are present
            print("Feature names from the model:")
            print(model.booster_.feature_name())

            # print current date
            print(most_recent_date)

            # Make prediction
            model_prediction = model.predict(input_data)[0]  # Assuming a single prediction
            model_prediction = f"${round(float(model_prediction), 0):,}"

            # Render the prediction result on prediction.html
            return render_template('prediction.html', prediction=model_prediction)

        except ValueError as e:
            print("ValueError:", e)
            return f"Invalid input: {e}"

        except Exception as e:
            print("An unexpected error occurred:", e)
            return f"An error occurred: {str(e)}"

    return render_template('predict.html')

@app.route('/favicon.ico')
def favicon():
    return '', 204  # Disables the favicon.ico request handling

# def open_browser():
#     # Open the browser once the Flask app is running
#     webbrowser.open("http://127.0.0.1:3000/")

if __name__ == "__main__":
    # Start the browser-opening thread
    # threading.Timer(1, open_browser).start()
    app.run(debug=True, port=5000)