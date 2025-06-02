import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.tsa.seasonal import seasonal_decompose

# Set seaborn style
sns.set(style='whitegrid')

# 1. Simulate Monthly Revenue Data (2018-2023)
np.random.seed(42)
months = pd.date_range(start='2018-01-01', end='2023-12-01', freq='MS')
revenue = 10000 + np.random.normal(0, 1500, len(months)) + np.linspace(0, 10000, len(months))
revenue += 2000 * np.sin(2 * np.pi * months.month / 12)  # Add seasonality

df = pd.DataFrame({'Month': months, 'Revenue': revenue})
df.set_index('Month', inplace=True)

# 2. Plot the Time Series
plt.figure(figsize=(12, 6))
plt.plot(df['Revenue'], label='Monthly Revenue', color='green')
plt.title('Monthly eCommerce Revenue (Simulated)')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.tight_layout()
plt.savefig('ecom_01_revenue_plot.png')
plt.show()

# 3. Decompose the Series
result = seasonal_decompose(df['Revenue'], model='additive', period=12)

result.plot()
plt.suptitle('Decomposition of eCommerce Revenue', fontsize=16)
plt.tight_layout()
plt.savefig('ecom_02_decomposition.png')
plt.show()

# 4. Add and Plot 3-Month Rolling Average
df['Rolling_3M'] = df['Revenue'].rolling(window=3).mean()

plt.figure(figsize=(12, 6))
plt.plot(df['Revenue'], label='Original Revenue')
plt.plot(df['Rolling_3M'], label='3-Month Rolling Average', color='red')
plt.title('3-Month Rolling Average of eCommerce Revenue')
plt.xlabel('Date')
plt.ylabel('Revenue ($)')
plt.legend()
plt.tight_layout()
plt.savefig('ecom_03_rolling_avg.png')
plt.show()
