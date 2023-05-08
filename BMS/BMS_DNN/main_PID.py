# -*- coding: utf-8 -*-
"""
Created on Sun May  7 18:31:31 2023

@author: COLLINS
"""

import time
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler


# Load the pre-trained deep learning model
model = load_model("dnn_model.h5")

# Load and preprocess the input data
input_data = np.array([[3.8, 0.5, 25, 0.5, 3.7, 1000]])
scaler = StandardScaler()
scaled_input = scaler.fit_transform(input_data)

# PID controller gains
Kp = 1.0
Ki = 0.5
Kd = 0.1

# Initialize error values and integral term
previous_error = 0
integral = 0

# Desired SOC
desired_SOC = 0.8

# Initial charging rate
charging_rate = 0.5

# Time step for the control loop (in seconds)
dt = 1

while True:
    # Get the current SOC prediction from the deep learning model
    current_SOC = model.predict(scaled_input)[0][0]

    # Calculate the error between the desired SOC and the current SOC
    error = desired_SOC - current_SOC

    # Calculate the proportional, integral, and derivative terms
    proportional = Kp * error
    integral += error * dt
    derivative = Kd * (error - previous_error) / dt

    # Calculate the output of the PID controller
    output = proportional + integral + derivative

    # Update the charging/discharging rate based on the PID controller output
    charging_rate += output

    # Update the previous error value
    previous_error = error

    # Print the current time, SOC prediction, and charging rate
    print(f"Time: {time.time()}, SOC prediction: {current_SOC:.4f}, Charging rate: {charging_rate:.4f}")

    # Wait for the next iteration (dt seconds)
    time.sleep(dt)
