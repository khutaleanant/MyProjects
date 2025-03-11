## By standardizing data formats like this, 
# the dataset becomes more consistent and easier to analyze.
## Here’s a small Python example to demonstrate 
# how to standardize different data formats such as 
# dates, currencies, times, and phone numbers:

import pandas as pd
from datetime import datetime
import re

# Sample Data

Data={'Date':['2002/02/01', '2004-07-10','2003-11-24','2004/07/15'],
        'Currency':['1,000.00', '$2,000.00', '$3,000.00', '$4,000.00'],
        'Time':['1:00 PM', '2:00', '3:00 PM', '4:00 am'],
        'Phone Number':['123-456-7890', '+1234-57-8901', '(345)-678-9012', '456-789-0123']}

# Create a DataFrame
df=pd.DataFrame(Data)

# Standardize Date Format (YYYY-MM-DD)

df['Date']=pd.to_datetime(df['Date'], dayfirst=False).dt.strftime('%Y-%m-%d')

# Standardize Currency Format ($X,XXX.XX)
df['Currency']=df['Currency'].replace('[\$,]', '', regex=True).astype(float)

# 3. Standardize Time Format to HH:MM AM/PM
df['time'] = pd.to_datetime(df['time'], errors='coerce').dt.strftime('%I:%M %p')

# 4. Standardize Phone Numbers to +1 (XXX) XXX-XXXX format
df['phone'] = df['phone'].apply(lambda x: re.sub(r'[^0-9]', '', x))  # Remove non-numeric characters
df['phone'] = df['phone'].apply(lambda x: f"+1 ({x[:3]}) {x[3:6]}-{x[6:]}")


# Show the standardized DataFrame
print(df)
