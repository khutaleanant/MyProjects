# Calculating the sales commission on the given data

import pandas as pd

# Sample sales data for 5 salespeople
DataSet = {
    'Salesperson': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Sales_Made': [10000.00, 15000.00, 20000.00, 12000.00, 8000.00]  # sales in dollars
}

# Create a DataFrame
DataFrame = pd.DataFrame(DataSet)

# Commission rate
commission_rate = 0.10  # 10%

# Calculate the commission for each salesperson
DataFrame['Commission'] = DataFrame['Sales_Made'] * commission_rate
# Calculate Total Earnings by adding Sales Made and Commission
DataFrame['Total_Earning']=DataFrame['Sales_Made'] + DataFrame['Commission']

# Round Total Earnings to 2 decimal places
DataFrame['Commission'] = DataFrame['Commission'].round()
DataFrame['Total_Earning'] = DataFrame['Total_Earning'].round()
# Display the results
print(DataFrame)