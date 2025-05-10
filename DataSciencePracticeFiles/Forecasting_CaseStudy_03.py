# Forecasting Model : Statistical Model: ARIMA
# ARIMA stands for: AutoRegressive (AR) Integrated (I) Moving Average (MA)
# It’s written as ARIMA(p, d, q) where:
# p = number of autoregressive terms (AR)
# d = number of differences needed to make the series stationary (Integration)
# q = number of moving average terms (MA)
###### 🔍 Components of ARIMA ######
# 1. AR (Autoregression): The model uses the past values of the series to predict the future.
# Example: If p=1, it uses 1 lagged value (Y(t-1)) to predict Y(t).
# 2. I (Integration):This part involves differencing the data to make it stationary.
# If d=1, it means the model is using the first difference:
#  Y'(t) = Y(t) - Y(t-1)
# 3. MA (Moving Average): The model uses past forecast errors in a regression-like model.
# If q=1, the error at time t is influenced by the error at t-1.

import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

DataFrame=pd.read_csv("C:\\Data Science Programs Practice\\DailyDelhiClimateTest.csv")
DataFrame.set_index("date",inplace=True)

# Select the column to forecast
series=DataFrame["meantemp"]

# plot the original series
series.plot(title="mean temperature over time")
plt.show()

# Check stationarity with ADF test
result=adfuller(series.dropna())
print("ADF statistic:",result[0])
print("p-value:",result[1])

# if p-value is >0.05 then the series is non-stationary and hence we difference it.
if result[1]>0.05:
    series_diff=series.diff().dropna()
    result_diff=adfuller(series_diff)
    print("ADF after differencing:",result_diff[0])
    print("p-value after differencing:",result_diff[1])
else:
    series_diff=series

# Fit ARIMA model (ARIMA(p,d,q)- Here assuming ARIMA(1,1,1) as example)
model=ARIMA(series,order=(1,1,1))
model_fit=model.fit()

# Forecast
forecast_steps=10
forecast=model_fit.forecast(steps=forecast_steps)
print("next 10 days forecast")
print(forecast)

# plot forecast
plt.figure(figsize=(16,16))
plt.plot(series[-50:],label="Observed")
plt.plot(forecast.index,forecast.values,label="Forecast",marker="x")
plt.legend()
plt.title("Mean temperature forecast")
plt.xlabel("Date")
plt.ylabel("Mean Temperature")
plt.grid()
plt.show()
