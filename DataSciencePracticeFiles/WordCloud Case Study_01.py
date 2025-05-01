#Cleanning for the 'reviewDescription' column and consolidation script

import pandas as pd

DataFrame=pd.read_csv("C:/Data Science Programs Practice/iphone.csv")

#Drop rows with missing or empty reviews 
DataFrame.dropna(subset=['reviewDescription'], inplace=True)

#Convert the 'reviewDescription' column to string type
DataFrame['reviewDescription'] = DataFrame['reviewDescription'].astype(str)

#Combine all reviews into a single string
all_reviews = ' '.join(DataFrame['reviewDescription'])

#Save the cleaned reviews (individual rows) to a new CSV file.
DataFrame.to_csv("Cleaned_iphone_Reviews.csv", index=False)

#Save the full combined text to a new CSV file.
combined_DataFrame = pd.DataFrame({'CombinedReviews': [all_reviews]})
combined_DataFrame.to_csv("All_Combined_iphone_Reviews.csv", index=False)

#Print the first few rows of the cleaned DataFrame
print(DataFrame.head())
#Print the first few rows of the combined DataFrame
print(combined_DataFrame.head())

print("\nCleaned Reviews saved to 'Cleaned_iphone_Reviews.csv'.")
print("\nFull Combined Review saved to 'All_Combined_iphone_Reviews.csv'.")

#The code above reads a CSV file containing iPhone reviews, 
#cleans the 'reviewDescription' column by removing rows with missing or empty values,
#and converts the reviews to string type.
#It then combines all reviews into a single string and saves both the cleaned reviews
#and the combined reviews to separate CSV files.
#The cleaned reviews are saved in 'Cleaned_iphone_Reviews.csv',
#and the combined reviews are saved in 'All_Combined_iphone_Reviews.csv'.
#The first few rows of both DataFrames are printed to the console for verification.
#The code also includes print statements to confirm that the cleaned and combined reviews have been saved successfully.
#The cleaned reviews are saved in 'Cleaned_iphone_Reviews.csv',
#and the combined reviews are saved in 'All_Combined_iphone_Reviews.csv'.