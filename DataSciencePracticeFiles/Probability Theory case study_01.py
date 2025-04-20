import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

DataFrame= pd.read_csv("C:\Data Science Programs Practice\student_marks.csv")

# Define test_columns
test_cols=[f"Test_{i}"for i in range(1,13)]

# Check for the missing test columns
missing=[col for col in test_cols if col not in DataFrame.columns]
if missing:
    print("Missing Columns:",missing)
else:
    #Calculate Average
    DataFrame["Average"]=DataFrame[test_cols].mean(axis=1)
    
    #Define "Failed" & "Low_Score"
    DataFrame["Failed"]=DataFrame["Average"]<40
    DataFrame["Low_Score"]=DataFrame["Average"]<=30

    #Calculate the probabilities
    P_failed=DataFrame["Failed"].mean()
    P_low_score=DatFrame["Low_Score"].mean()
    P_low_given_failed=DataFrame[DataFrame[DataFrame["Failed"]==1]["Low_Score"]].mean()

    # Avoid divide by 0
    if P_low_score>0:
        P_failed_given_low_score=(P_low_given_failed*P_failed)/P_low_score
    else:
        P_failed_given_low_score=float("NaN")
        print("No Student Have Low Score <=30")
        
    #Output
    print(f"P(Failed)={P_failed:.2f}")
    print(f"P(Low_Score)={P_low_score:.2f}")
    print(f"P(Low_Score|Failed):{P_low_given_failed:.2f}")
    print(f"P(Failed|Low_Score):{P_failed_given_low_score:.2f}")

    #Visulalized HistoGram
    plt.figure(figsize=(10,10))
    sns.histplot(DataFrame["Average"],bins=15,color="red",edgecolor="black")

    #Mark Low Score and Failed thresholds
    plt.axvline(30,color="blue",linestyle="--",label="Low Score Threshold(30)")
    plt.axvline(40,color="yellow",linestyle="--",label="Failed Threshold(40)")

    #Plot Labels
    plt.title("HistoGram of Student's Average Marks",fontsize=14)
    plt.xlabel("Average Score",fontsize=12,color="pink")
    plt.ylabel("Number Of Students",fontsize=12,color="pink")
    plt.legend()
    plt.tight_layout()
    plt.show()
