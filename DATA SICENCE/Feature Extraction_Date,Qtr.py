## You can also extract other date-related features like:
# Day of the week (e.g., Monday, Tuesday, etc.)
# Week of the year (e.g., 1st week, 2nd week, etc.)
# Is the day a weekend or not?
# Quarter of the year (e.g., Q1, Q2, Q3, Q4):

#Example: 
#Let's say you have the following 
#DataFrame with a column date_column that contains dates in string format

import pandas as pd

# Sample data with dates

DateData={'Date_Column':['2024-01-04',
                         '2023-10-05',
                         '2022-12-15',
                         '2021-08-25',
                         '2020-06-30',
                         '2019-04-20',
                         '2018-02-10',
                         '2017-10-01']}

df=pd.DataFrame(DateData)


# Convert the Date_Column to datetime and year, month, and day

df['Date_Column']=pd.to_datetime(df['Date_Column'])
df['Year']=df['Date_Column'].dt.year
df['Month']=df['Date_Column'].dt.month
df['Day']= df['Date_Column'].dt.day

df['Weekday'] = df['Date_Column'].dt.day_name()
df['Week_Of_Year'] = df['Date_Column'].dt.isocalendar().week
df['Quarter'] = df['Date_Column'].dt.quarter

print(df)


