#  Urban Traffic Congestion Prediction

A machine learning project that predicts urban traffic congestion levels as **Low, Medium, or High** using traffic, environmental, and contextual information.

##  Project Overview

Urban traffic congestion is affected by several factors such as the number of vehicles, traffic speed, road occupancy, accidents, weather conditions, and traffic signals.

This project uses machine learning classification models to predict the traffic condition from these features.

The project includes:

- Exploratory Data Analysis (EDA)
- Feature engineering
- Data preprocessing
- Multiple classification models
- Model evaluation
- Time-based model evaluation
- Feature importance analysis
- A Streamlit web application for predictions

## 📊 Dataset

The dataset contains **5,000 traffic records** with information about:

- Timestamp
- Latitude and Longitude
- Vehicle Count
- Traffic Speed
- Road Occupancy
- Traffic Light State
- Weather Condition
- Accident Report
- Sentiment Score
- Ride Sharing Demand
- Parking Availability
- Emission Levels
- Energy Consumption
- Traffic Condition

The target variable is:

- **Low**
- **Medium**
- **High**

##  Exploratory Data Analysis

The dataset was analyzed to understand:

- Traffic condition distribution
- Average vehicle count for different traffic conditions
- Average traffic speed
- Road occupancy
- Effect of weather conditions
- Traffic light conditions
- Accident reports
- Vehicle count variation by hour
- Vehicle count variation by day
- Correlations between numerical features

##  Machine Learning Models

The following models were evaluated:

1. Baseline Classifier
2. Logistic Regression
3. Decision Tree
4. Limited Depth Decision Tree
5. Random Forest
6. Balanced Random Forest
7. Time-Based Balanced Random Forest

##  Model Performance

| Model | Accuracy |
| Baseline | 63.3% |
| Logistic Regression | 76.2% |
| Decision Tree | 99.9% |
| Limited Depth Decision Tree | 94.0% |
| Random Forest | 99.8% |
| Balanced Random Forest | 100.0% |
| Time-Based Balanced Random Forest | 99.79% |

The **Time-Based Balanced Random Forest** was selected as the final model because the dataset contains timestamped observations and a time-based evaluation provides a more realistic test of performance on later observations.

##  Important Features

The Random Forest model identified the following as the most important features:

- Vehicle Count
- Road Occupancy
- Traffic Speed
- Accident Report

These features had substantially more influence on the model than the remaining features.

##  Time-Based Evaluation

Since the dataset contains timestamps, the data was also evaluated using a chronological split.

Earlier observations were used for training, while later observations were used for testing.

The final time-based model achieved approximately **99.79% accuracy** on the test data.

##  Streamlit Application

A Streamlit application was created to allow users to enter traffic information and receive:

- Predicted traffic condition
- Prediction probabilities for Low, Medium, and High congestion

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit
- Jupyter Notebook

##  Project Structure

urban-traffic-congestion/

- app.py
- traffic_congestion.ipynb
- traffic.csv
- traffic_congestion_model.pkl
- model_features.pkl
- requirements.txt
- README.md
- .gitignore
