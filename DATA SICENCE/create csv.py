import pandas as pd
import numpy as np
from datetime import timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate a random sample of 2000 records
num_records = 2000

# Generate random data for each column
order_ids = np.arange(1001, 1001 + num_records)
customer_ids = [f'C{str(i).zfill(3)}' for i in np.random.randint(1, 101, num_records)]
customer_names = np.random.choice(['John Doe', 'Jane Smith', 'Sam Brown', 'Sarah White', 'Mike Black', 'Lisa Green',
                                   'Tom Harris', 'Emma Davis', 'Mark Lee', 'Olivia White', 'James Taylor', 
                                   'Sophia Scott', 'Daniel King', 'Hannah Allen', 'Andrew Moore', 'Laura Clark'], num_records)

# Adjust the order dates to span from 2018-01-01 to 2025-12-31
order_dates = pd.to_datetime(np.random.choice(pd.date_range('2018-01-01', '2025-12-31', freq='H'), num_records))
delivery_dates = order_dates + pd.to_timedelta(np.random.randint(1, 7, num_records), unit='D')  # Delivery within 1-6 days
shipping_methods = np.random.choice(['Standard', 'Expedited'], num_records)
delivery_status = np.random.choice(['Delivered', 'Pending'], num_records)
delivery_times = (delivery_dates - order_dates).days  # Delivery time in days
product_categories = np.random.choice(['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Groceries'], num_records)
delivery_regions = np.random.choice(['North America', 'Europe', 'Asia'], num_records)

# Add time column (random time between 00:00:00 and 23:59:59)
order_times = [str(np.random.randint(0, 24)).zfill(2) + ':' + str(np.random.randint(0, 60)).zfill(2) + ':' + str(np.random.randint(0, 60)).zfill(2) for _ in range(num_records)]
delivery_times = [str(np.random.randint(0, 24)).zfill(2) + ':' + str(np.random.randint(0, 60)).zfill(2) + ':' + str(np.random.randint(0, 60)).zfill(2) for _ in range(num_records)]

# Create DataFrame
df = pd.DataFrame({
    'Order ID': order_ids,
    'Customer ID': customer_ids,
    'Customer Name': customer_names,
    'Order Date': order_dates,
    'Order Time': order_times,
    'Delivery Date': delivery_dates,
    'Delivery Time': delivery_times,
    'Shipping Method': shipping_methods,
    'Delivery Status': delivery_status,
    'Delivery Time (days)': delivery_times,
    'Product Category': product_categories,
    'Delivery Region': delivery_regions
})

# Show the first few rows of the DataFrame
print(df.head())

# Save to a CSV file
df.to_csv("ecommerce_delivery_data_2018_2025.csv", index=False)
