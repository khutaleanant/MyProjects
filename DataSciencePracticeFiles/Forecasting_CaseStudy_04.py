import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")
# Ensure the index is datetime
series.index = pd.to_datetime(series.index)

# Load the dataset and parse dates
# Load the dataset and parse dates
DataFrame = pd.read_csv("C:\\Data Science Programs Practice\\DailyDelhiClimateTest.csv")
DataFrame['date'] = pd.to_datetime(DataFrame['date'], dayfirst=True)  # Fixed: Interpret date as DD-MM-YYYY
DataFrame.set_index("date", inplace=True)


# Select the column to forecast
series = DataFrame["meantemp"]

# Plot the original series
series.plot(title="Mean Temperature Over Time", figsize=(10, 4))
plt.xlabel("Date")
plt.ylabel("Mean Temperature")
plt.grid()
plt.show()

# Check stationarity using the Augmented Dickey-Fuller test
result = adfuller(series.dropna())
print("ADF Statistic:", result[0])
print("p-value:", result[1])

# Apply differencing if needed
if result[1] > 0.05:
    series_diff = series.diff().dropna()
    result_diff = adfuller(series_diff)
    print("ADF after differencing:", result_diff[0])
    print("p-value after differencing:", result_diff[1])
    d = 1
else:
    series_diff = series
    d = 0

# Fit the ARIMA model (manually setting p=1, d from above, q=1)
model = ARIMA(series, order=(1, d, 1))
model_fit = model.fit()

# Forecast the next 10 days
forecast_steps = 10
forecast = model_fit.forecast(steps=forecast_steps)

# Generate future date index
last_date = series.index[-1]
forecast_index = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=forecast_steps, freq='D')
forecast.index = forecast_index

# Print forecast
print("\nForecast for next 10 days:")
print(forecast)

# Plot recent actuals and forecast
plt.figure(figsize=(10, 5))
plt.plot(series[-50:], label="Observed")
plt.plot(forecast, label="Forecast", marker="x")
plt.title("Mean Temperature Forecast")
plt.xlabel("Date")
plt.ylabel("Mean Temperature")
plt.legend()
plt.grid()
plt.show()

# Residual diagnostics
residuals = model_fit.resid

plt.figure(figsize=(10, 4))
plt.plot(residuals)
plt.title("Residuals from ARIMA Model")
plt.grid()
plt.show()

# Plot residual density
residuals.plot(kind='kde', title='Density of Residuals')
plt.grid()
plt.show()