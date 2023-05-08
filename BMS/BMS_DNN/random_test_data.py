# -*- coding: utf-8 -*-
"""
Created on Sun May  7 16:42:32 2023

@author: COLLINS
"""

import pandas as pd
from sklearn.model_selection import train_test_split

# Load the data from synthetic_soc_data.csv
data = pd.read_csv("synthetic_soc_data.csv")

# Split the data into training and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Save the training features and labels to train_features.csv and train_labels.csv
train_data.drop(columns=["SOC"]).to_csv("train_features.csv", index=False)
train_data["SOC"].to_csv("train_labels.csv", index=False)

# Save the test features and labels to test_features.csv and test_labels.csv
test_data.drop(columns=["SOC"]).to_csv("test_features.csv", index=False)
test_data["SOC"].to_csv("test_labels.csv", index=False)
