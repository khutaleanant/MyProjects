import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
import seaborn as sns

DataFrame=pd.read_csv("C:\Data Science Programs Practice\student_marks.csv")

#identfy test score columns
test_cols = [col for col in DataFrame.columns if col.startswith("Test_")]

#Compute z-scores and add outlier flag
z_scores = DataFrame[test_cols].apply(zscore)

for col in test_cols:
    DataFrame[f"{col}_zscore"] = z_scores[col]
    DataFrame[f"{col}_outlier"] = z_scores[col].apply(lambda z: "yes" if abs(z) > 2 else "no")

#Save the final DataFrame to a new CSV file
DataFrame.to_csv("Student_marks_with_zscores.csv",index=False)

#plot histograms for each test column
plt.figure(figsize=(14, 8))
for i, col in enumerate(test_cols):
    plt.subplot(4, 3, i+1)
    #Adjust based on the number of tests (3 columns per row)
    sns.histplot(DataFrame[col], bins=10, kde=True,color="blue")
    plt.title(f"Histogram of {col}")
    plt.xlabel("Score")
    plt.ylabel("Frequency")

plt.tight_layout()
plt.suptitle("Histograms of student Test Scores", y=1.02, fontsize=16)
plt.show()