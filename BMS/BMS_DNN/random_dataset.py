# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:14:07 2023

@author: COLLINS
"""

import numpy as np
import pandas as pd

# Set the random seed for reproducibility
np.random.seed(42)

# Number of data points
n_samples = 1000

# Generate random feature values
voltage_measured = np.random.uniform(2.5, 4.2, n_samples)
current_measured = np.random.uniform(-1, 1, n_samples)
temperature_measured = np.random.uniform(5, 40, n_samples)
current_load = np.random.uniform(-1, 1, n_samples)
voltage_load = np.random.uniform(2.5, 4.2, n_samples)
time = np.random.uniform(0, 1000, n_samples)

# Generate random SOC values (between 0 and 1)
soc = np.random.uniform(0, 1, n_samples)

# Create a DataFrame with the generated data
data = pd.DataFrame({
    "Voltage_measured": voltage_measured,
    "Current_measured": current_measured,
    "Temperature_measured": temperature_measured,
    "Current_load": current_load,
    "Voltage_load": voltage_load,
    "Time": time,
    "SOC": soc
})

# Save the generated data to a CSV file
data.to_csv("synthetic_soc_data.csv", index=False)

# Print the first few rows of the dataset
print(data.head())
