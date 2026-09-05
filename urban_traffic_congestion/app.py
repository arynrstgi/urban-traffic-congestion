import streamlit as st
import pandas as pd
import joblib

import os
import joblib
BASE_DIR =os.path.dirname(os.path.abspath(__file__))
model = joblib.load("traffic_congestion_model.pkl")
features = joblib.load(os.path.join(BASE_DIR,"model_features.pkl"))

st.set_page_config(
    page_title="Traffic Congestion Prediction",
    page_icon="👮‍♂️"
)
st.title("⚠️Urban Traffic Congestion Prediction⚠️")

st.write(
    "Enter the traffic conditions below to predict the level of congestion."
)
st.subheader("Traffic Information")

latitude = st.number_input(
    "Latitude",
    value=40.75
)
longitude = st.number_input(
    "Longitude",
    value=-73.85
)
vehicle_count = st.number_input(
    "Vehicle Count",
    min_value=0,
    value=150
)
speed = st.number_input(
    "Traffic Speed (km/h)",
    min_value=0.0,
    value=35.0
)
occupancy = st.number_input(
    "Road Occupancy (%)",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)
accident = st.selectbox(
    "Accident Report",
    ["No", "Yes"]
)
sentiment = st.number_input(
    "Sentiment Score",
    value=0.2
)
ride_demand = st.number_input(
    "Ride Sharing Demand",
    min_value=0,
    value=50
)
parking = st.number_input(
    "Parking Availability (%)",
    min_value=0.0,
    max_value=100.0,
    value=40.0
)
emissions = st.number_input(
    "Emission Levels (g/km)",
    min_value=0.0,
    value=150.0
)
energy = st.number_input(
    "Energy Consumption (L/h)",
    min_value=0.0,
    value=5.0
)
hour = st.number_input(
    "Hour",
    min_value=0,
    max_value=23,
    value=12
)
traffic_light = st.selectbox(
    "Traffic Light State",
    ["Green", "Yellow", "Red"]
)
weather = st.selectbox(
    "Weather Condition",
    ["Clear", "Rain", "Fog", "Snow"]
)
day = st.selectbox(
    "Day",
    [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday"
    ]
)

if st.button("Predict Traffic Condition"):

   
    accident_value = 1 if accident == "Yes" else 0

   
    data = pd.DataFrame([{

        "Latitude": latitude,
        "Longitude": longitude,
        "Vehicle_Count": vehicle_count,
        "Traffic_Speed_kmh": speed,
        "Road_Occupancy_%": occupancy,
        "Accident_Report": accident_value,
        "Sentiment_Score": sentiment,
        "Ride_Sharing_Demand": ride_demand,
        "Parking_Availability": parking,
        "Emission_Levels_g_km": emissions,
        "Energy_Consumption_L_h": energy,
        "Hour": hour,

        
        "Traffic_Light_State_Red": traffic_light == "Red",
        "Traffic_Light_State_Yellow": traffic_light == "Yellow",

     
        "Weather_Condition_Fog": weather == "Fog",
        "Weather_Condition_Rain": weather == "Rain",
        "Weather_Condition_Snow": weather == "Snow",

        
        "Day_Monday": day == "Monday",
        "Day_Saturday": day == "Saturday",
        "Day_Sunday": day == "Sunday",
        "Day_Thursday": day == "Thursday",
        "Day_Tuesday": day == "Tuesday",
        "Day_Wednesday": day == "Wednesday"
    }])

    data = data[features]

    prediction = model.predict(data)[0]

    st.success(
        f"Predicted Traffic Condition: {prediction}"
    )

    probabilities = model.predict_proba(data)[0]

    st.write("### Prediction Probabilities")


    for class_name, probability in zip(
        model.classes_,
        probabilities
    ):

        st.write(
            f"{class_name}: {probability:.0%}"
        )

        st.progress(
            float(probability)
        )