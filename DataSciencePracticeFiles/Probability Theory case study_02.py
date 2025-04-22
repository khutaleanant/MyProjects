from turtle import width
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

DataFrame=pd.read_csv("C:\Data Science Programs Practice\student_marks.csv")

#Define test columns
test_cols=[f"Test_{i}" for i in range(1,13)]

#Check for the missing columns
missing=[col for col in test_cols if col not in DataFrame.columns]
if missing:
    print("Missing Columns:",missing)
else:
    #calculate the average marks
    DataFrame["Average"]=DataFrame[test_cols].mean(axis=1)

    #Compute mean and standard deviation
    mean=DataFrame["Average"].mean()
    stddev=DataFrame["Average"].std()

    print(f"Mean of Average Marks: {mean:.2f}")
    print(f"Standard Deviation: {stddev:.2f}")

    #Generate X values and corresponding Y value for normal distribution curve
    x=np.linspace(mean-4*stddev,mean+4*stddev,1000)
    ## This line of code is using numpy to create an array of 1000 values that are
    ## evenly spaced over specific interval center around a mean and spanning
    ## 4 standard deviations in both directions.

    ## mean-4*stddev: start of the interval(4 std dev below the mean)
    ## mean+4*stddev: end of the interval(4 std dev above the mean)
    ## 1000: number of evenly spaced values between start and end.

    y=norm.pdf(x,mean,stddev)
    ## Above line is calculating the probability density funtion of a normal distribution
    ## for each value in the x array we created earlier.
    ## norm.pdf(): is from scipy.stats and it gives the height of the normal distribution curve
    ## at each x.
    ## x is your array of values.
    ## mean and stddev are parameters of the normal distribution.     

    #Plot only the normal distribution curve
    plt.figure(figsize=(10,10))
    plt.plot(x,y,color="blue",linewidth=2,label="Normal Distribution Curve")
    
    #Styling
    plt.title("Bell Curve (Normal Distribution) of student average marks.")
    plt.xlabel("Average Marks")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

    #Overlay Histogram (to compare actual vs normal curve):
    plt.figure(figsize=(10, 10))
    plt.hist(DataFrame["Average"], bins=20, density=True, alpha=0.6, color='orange', label='Actual Distribution')
    plt.plot(x, y, color="blue", linewidth=2, label="Normal Distribution Curve")
    plt.title("Bell Curve (Normal Distribution) vs Actual Average Marks")
    plt.xlabel("Average Marks")
    plt.ylabel("Probability Density")
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()

                                                