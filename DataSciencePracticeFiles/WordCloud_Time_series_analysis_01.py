import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Set seaborn style
sns.set(style='whitegrid')

# Load the dataset
url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/airline-passengers.csv'
data = pd.read_csv(url, parse_dates=['Month'], index_col='Month')

# Display first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Plot original time series
plt.figure(figsize=(12, 6))
plt.plot(data, label='Monthly Passengers', color='blue')
plt.title('Monthly Number of Airline Passengers')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.legend()
plt.tight_layout()
plt.savefig('01_time_series_plot.png')  # Save plot
plt.show()

# Decompose the time series
result = seasonal_decompose(data, model='multiplicative')

# Plot decomposition
result.plot()
plt.suptitle('Time Series Decomposition', fontsize=16)
plt.tight_layout()
plt.savefig('02_decomposition.png')  # Save decomposition plot
plt.show()

# Compute and plot rolling mean
data['Rolling_Mean'] = data['Passengers'].rolling(window=12).mean()

plt.figure(figsize=(12, 6))
plt.plot(data['Passengers'], label='Original')
plt.plot(data['Rolling_Mean'], label='12-Month Rolling Mean', color='red')
plt.title('Rolling Mean of Airline Passengers')
plt.xlabel('Date')
plt.ylabel('Passengers')
plt.legend()
plt.tight_layout()
plt.savefig('03_rolling_mean.png')  # Save rolling mean plot
plt.show()
