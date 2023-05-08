# BMS-DNN
This project implements a battery management system (BMS) that uses a deep neural network (DNN) to predict the state of charge (SOC) of a battery based on measured sensor data. The BMS is implemented in Python using the TensorFlow and Keras libraries.


## Requirements
To run this project, you will need the following software:

pip install -r requirements.txt

## Data
The BMS uses a synthetic dataset of sensor data and corresponding SOC values. The dataset includes the following features:
- Voltage_measured
- Current_measured
- Temperature_measured
- Current_load
- Voltage_load
- Time
- SOC

## Training the DNN
The DNN model is trained on the synthetic dataset using the following steps:
- Load the dataset using Pandas.
- Split the dataset into features and labels.
- Split the data into training and testing sets.
- Scale the features using a StandardScaler.
- Define the DNN model using Keras.
- Compile the model using an optimizer and loss function.
- Train the model using the training data.
- Evaluate the model using the testing data.
- Save the model to a file.

## Simulating the BMS
The BMS simulates real-time data collection and SOC prediction using the trained DNN model. The simulation is implemented in the following steps:
- Load the trained DNN model from a file.
- Define a function to generate simulated sensor data.
- Define a function to preprocess the sensor data and make a SOC prediction using the DNN model.
- Run a loop that generates simulated sensor data, preprocesses the data, makes a SOC prediction, and prints the prediction to the console.
- Sleep for a short amount of time between iterations to simulate real-time data collection.

## Adding PID Control
To add PID control to the BMS, the following steps are implemented:
- The PID algorithm is implemented in a separate module.
- The BMS simulation script is modified to import the PID control module and use its functionality to adjust the charging and discharging rates of the battery based on the predicted SOC.

## Conclusion
This project demonstrates the implementation of a battery management system using a deep neural network to predict the state of charge of a battery. The system can be extended by adding PID control to adjust the charging and discharging rates of the battery to maintain a desired SOC.


 here's a table of the example dataset used in this project:

| Voltage_measured | Current_measured | Temperature_measured | Current_load | Voltage_load | Time           | SOC           |
|------------------|-------------------|----------------------|--------------|--------------|----------------|--------------|
| 3.136718202      | -0.629734142     | 14.15969893          | 0.345405988  | 3.472392993  | 393.6355203   | 0.648256954  |
| 4.116214321      | 0.083801895      | 13.64425797          | 0.593362794  | 3.86923496   | 473.4356594   | 0.172386362  |
| 3.744389701      | 0.745891672      | 36.71891032          | -0.499064202 | 3.792273581  | 854.5473932   | 0.872394563  |
| 3.517719423      | 0.464449773      | 13.73411699          | 0.249748199  | 2.761629838  | 340.0043861   | 0.613116239  |
| 2.765231689      | 0.613122296      | 14.51824041          | 0.143491966  | 2.753724099  | 869.6496848   | 0.157203884  |
| 2.765190685      | 0.317566733      | 31.57893918          | 0.665660754  | 2.955896425  | 88.13443098   | 0.962338057  |
| 2.598742141      | 0.384553129      | 20.74089449          | 0.812174121  | 3.113827035  | 776.7984372   | 0.518365463  |

The dataset includes 7 columns:

- Voltage_measured: voltage measured by a sensor
- Current_measured: current measured by a sensor
- Temperature_measured: temperature measured by a sensor
- Current_load: current load on the battery
- Voltage_load: voltage load on the battery
- Time: time at which the measurement was taken
- SOC: state of charge of the battery, which is the target variable for the prediction model.
The synthetic dataset used in this project is a simulated battery dataset that was generated using a battery model. It consists of 7 columns, including Voltage_measured, Current_measured, Temperature_measured, Current_load, Voltage_load, Time, and SOC.

The Voltage_measured column represents the voltage of the battery at a specific point in time, while the Current_measured column represents the current flowing through the battery at that same point in time. The Temperature_measured column represents the temperature of the battery, and the Current_load column represents the amount of current that is being drawn from the battery. The Voltage_load column represents the voltage of the load, and the Time column represents the time at which the data was collected. Finally, the SOC column represents the state of charge of the battery at each point in time.

Overall, this synthetic dataset was used to train a deep neural network model to predict the state of charge of a battery based on its electrical measurements. The trained model can be used in battery management systems to optimize the charging and discharging of the battery, which can improve the battery's performance and extend its lifetime.
