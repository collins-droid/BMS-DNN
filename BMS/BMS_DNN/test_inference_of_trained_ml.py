# Load the saved model
from tensorflow.keras.models import load_model
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn.preprocessing import StandardScaler
import numpy as np
# Load the test data
X_test = pd.read_csv("test_features.csv")
y_test = pd.read_csv("test_labels.csv")

# Scale the features using the previously fitted StandardScaler
scaler = StandardScaler()
scaler.fit(X_test)
X_test_scaled = scaler.transform(X_test)

# Load the saved model
model = load_model("dnn_model.h5")

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Calculate the Mean Absolute Error on the test set
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
print(f"Mean Absolute Error on test set: {mae:.4f}")

# Make predictions on the test set
y_pred = model.predict(X_test_scaled)

# Create a scatter plot of true SOC values vs predicted SOC values
plt.scatter(y_test, y_pred)
plt.xlabel("True SOC Values")
plt.ylabel("Predicted SOC Values")
plt.title("True SOC vs Predicted SOC")

# Add a diagonal line to the plot to indicate perfect predictions
diagonal_line = np.linspace(0, 1, 100)
plt.plot(diagonal_line, diagonal_line, 'r', linestyle='--')

# Display the plot
plt.show()
