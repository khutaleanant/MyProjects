# A time series is stationary if its properties (mean,variance) do not change over time.

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller

DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\DailyDelhiClimateTest.csv")

# Select the column to check for stationarity
series= DataFrame["meantemp"]

# plotting the original time series
plt.figure(figsize=(10,4))
plt.plot(series,label="Mean Temperature")
plt.xlabel("Dates")
plt.ylabel("Temperature")
plt.legend()
plt.grid()
plt.show()

# Calculating rolling statistics (Moving Average and Moving Standard Deviation)
rolling_mean= series.rolling(window=12).mean()
rolling_std= series.rolling(window=12).std()

# plot rolling statistics
plt.figure(figsize=(10,5))
plt.plot(series,label="Original")
plt.plot(rolling_mean,color="Red",label="Rolling Mean")
plt.plot(rolling_std,color="Blue",label="Rolling STD DEV")
plt.legend(loc="best")
plt.title("Rolling Mean and Std Dev")
plt.grid()
plt.show()

# Perform Augmented Dickey-Fuller test
print("Results of Augmented Dickey-Fuller test")
adf_test = adfuller(series.dropna())
adf_output = pd.Series(adf_test[0:4], index=["adf statistics", "p-value", "#Lags Used", "Number of Observation Used"])
# Add critical values if available
if len(adf_test) > 4 and isinstance(adf_test[4], dict):
    for key, value in adf_test[4].items():
        adf_output[f"Critical Value ({key})"] = value
print(adf_output)