Home Price Prediction App
Overview
The Home Price Prediction App is designed to help users predict home prices 12 months out based on various macroeconomic indicators. The app uses a LightGBM model and integrates real-time data from public open sources to assist in scenario planning for the Government of Canada. The app provides an interactive interface where users can input home price details, and the system will generate a prediction using the latest data and model.

Features
User Input for Home Prices: Users can input current home prices and related details.
Prediction Model: The app uses a LightGBM machine learning model to predict home prices 12 months out.
Macroeconomic Data Integration: The app integrates the most recent home price data from open public sources and macroeconomic indicators.
Scenario Planning for Government of Canada: The predictions help inform future home price trends for government policy and planning.
Application Workflow
index.html: This is the landing page of the app. It provides an overview and a link to the prediction page where users can enter data.
predict.html: This page allows users to input data, including the current home price and relevant macroeconomic indicators.
app.py: This backend script processes the input data, applies the LightGBM model, and generates a prediction based on the current data. The result is then sent to the prediction.html page.
prediction.html: Displays the prediction results, including the projected home price for the next 12 months, helping with scenario planning.
Installation Instructions
Prerequisites
Ensure that the following are installed on your system:

Python (3.x recommended)
Docker (for containerization)
Virtual Environment (for managing dependencies)
GitHub Account (for repository hosting and version control)
Cloud Account (for hosting the app)
Setting up the Virtual Environment
Clone the repository:

bash
Copy code
git clone https://github.com/joel-collard/INSY695-696-Data-Science.git
cd INSY695-696-Data-Science
Set up a Python virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install required libraries:

bash
Copy code
pip install -r requirements.txt
Running the Application Locally
Run the backend application:

The main backend logic is contained within app.py. To run it locally:

bash
Copy code
python app.py
This will start a local server (usually on http://127.0.0.1:5000/) where the app can be accessed.

Open your browser and go to the following URL:

arduino
Copy code
http://127.0.0.1:5000/
Docker Setup
To run the app within a container using Docker:

Build the Docker image:

bash
Copy code
docker build -t home-price-prediction-app .
Run the Docker container:

bash
Copy code
docker run -p 5000:5000 home-price-prediction-app
Open your browser and access the app at:

arduino
Copy code
http://127.0.0.1:5000/
App Workflow and Prediction Process
User Input
On predict.html, users can enter the current home price and additional macroeconomic indicators such as interest rates, inflation, and employment data.

The input data is processed and fed into the LightGBM model.

LightGBM Model
The LightGBM model is a machine learning model that has been trained on historical home price data and macroeconomic indicators.
The model predicts home prices based on the provided input and uses the latest data from open public sources for the most accurate predictions.
Macroeconomic Data Integration
The app fetches real-time home price data and macroeconomic indicators from public open sources to feed into the prediction model.
The model is designed to work with data inputs from macroeconomic indicators such as:
Interest rates
Inflation
Employment rates
Economic growth metrics
Predictions
The app outputs the predicted home price 12 months into the future, providing valuable insights for scenario planning.
The prediction is displayed on prediction.html, along with a visualization of the forecasted home price trends.
Known Issues
Compatibility Issues with Virtual Environment: Currently, there are compatibility issues with some libraries and programs in the conda virtual environment, preventing the completion of the final solution to deploy in the cloud using docker.
These issues are related to conflicting library versions or dependencies that need to be resolved for full functionality.