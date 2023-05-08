# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:51:20 2023

@author: COLLINS
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
import time
import numpy as np
from tensorflow.keras.models import load_model


# Load the DNN model
model = load_model("dnn_model.h5")


# Load the dataset
data = pd.read_csv("synthetic_soc_data.csv")

# Split the dataset into features and labels
X = data.drop("SOC", axis=1)
y = data["SOC"]

# Fit the scaler on the training data
scaler = StandardScaler()
scaler.fit(X)

# Get the feature names from the training data
feature_names = X.columns

def generate_sensor_data():
    voltage_measured = np.random.uniform(2.5, 4.2)
    current_measured = np.random.uniform(-1, 1)
    temperature_measured = np.random.uniform(5, 40)
    current_load = np.random.uniform(-1, 1)
    voltage_load = np.random.uniform(2.5, 4.2)
    time_stamp = time.time()
    return [voltage_measured, current_measured, temperature_measured, current_load, voltage_load, time_stamp]

def predict_soc(sensor_data, scaler, feature_names):
    # Create a DataFrame from the sensor data and set the column names
    sensor_data = pd.DataFrame([sensor_data], columns=feature_names)

    # Scale the sensor data using the same StandardScaler used during training
    scaled_data = scaler.transform(sensor_data)

    # Make a prediction using the DNN model
    soc_prediction = model.predict(scaled_data)

    return soc_prediction[0][0]

# Run the simulation
while True:
    # Generate simulated sensor data
    sensor_data = generate_sensor_data()

    # Preprocess the sensor data and make a prediction
    soc_prediction = predict_soc(sensor_data, scaler, feature_names)

    # Print the SOC prediction
    print(f"Time: {sensor_data[-1]}, SOC prediction: {soc_prediction:.4f}")

    # Sleep for a short amount of time to simulate real-time data collection
    time.sleep(0.1)
