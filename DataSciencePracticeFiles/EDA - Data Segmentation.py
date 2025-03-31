##Conclusion##
# Data segmentation in EDA helps you understand the differences between 
# subgroups and can lead to more refined insights. By visualizing and analyzing each 
# segment, you can make more informed decisions about 
# how to approach data modeling or business strategy. 
# Whether using simple categorization or more complex clustering techniques, 
# segmentation adds value by providing a deeper dive into the dataset’s underlying structure.

import pandas as pd

# #Example 1 : Segmenting a Customer Dataset by Age
# # Sample customer dataset
# data = {
#     'CustomerID': [1, 2, 3, 4, 5],
#     'Age': [23, 45, 31, 65, 18],
#     'SpendingScore': [77, 56, 45, 23, 89]
# }

# # Create a DataFrame
# df = pd.DataFrame(data)

# # Define age segments
# def age_segment(age):
#     if age < 25:
#         return 'Youth'
#     elif 25 <= age < 40:
#         return 'Young Adult'
#     elif 40 <= age < 60:
#         return 'Middle Aged'
#     else:
#         return 'Senior'

# # Apply segmentation
# df['AgeSegment'] = df['Age'].apply(age_segment)

# # Display the segmented DataFrame
# print(df)

##########################################################
# #Example 2: Segmenting a Customer Dataset by Age
import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
data = pd.DataFrame({'Customer_ID': [1, 2, 3, 4, 5, 6, 7],
                     'Age': [15, 22, 35, 41, 57, 60, 72],
                     'Annual_Spend': [500, 1500, 2500, 3500, 5000, 7000, 8000]})

# Age Segmentation
bins = [0, 18, 35, 50, 100]
labels = ['0-18', '19-35', '36-50', '51+']
data['Age_Group'] = pd.cut(data['Age'], bins=bins, labels=labels, right=False)

# Segment Analysis
age_groups = data.groupby('Age_Group').agg({
    'Customer_ID': 'count',
    'Annual_Spend': 'mean'
}).reset_index()

# Visualizing the Segmentation
plt.figure(figsize=(8, 5))
plt.bar(age_groups['Age_Group'], age_groups['Annual_Spend'], color='skyblue')
plt.title('Average Annual Spend by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Annual Spend ($)')
plt.show()