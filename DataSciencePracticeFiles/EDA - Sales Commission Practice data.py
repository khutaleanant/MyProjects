import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Create a DataFrame from the dataset
data = {
    'Employee ID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Name': ['John Doe', 'Jane Smith', 'Michael Lee', 'Emma Brown', 'Kevin White', 
             'Laura Green', 'James Black', 'Sophia Clark', 'David Wilson', 'Olivia White'],
    'Department': ['Sales', 'Marketing', 'Engineering', 'Marketing', 'Sales', 
                   'HR', 'Engineering', 'HR', 'Sales', 'Engineering'],
    'Salary': [55000, 62000, 75000, 58000, 53000, 60000, 72000, 65000, 58000, 70000],
    'Performance Score': [85, 90, 80, 88, 82, 95, 78, 91, 87, 92],
    'Years at Company': [3, 5, 7, 2, 4, 6, 8, 3, 5, 4],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
}

df = pd.DataFrame(data)

# 1. **Average Salary and Performance by Department**
avg_salary_per_dept = df.groupby('Department')[['Salary', 'Performance Score']].mean()
print("Average Salary and Performance by Department:")
print(avg_salary_per_dept)

# 2. **Salary vs. Performance Score Correlation**
salary_vs_performance = df[['Salary', 'Performance Score']].corr()
print("\nCorrelation between Salary and Performance Score:")
print(salary_vs_performance)

# 3. **Average Salary by Gender**
avg_salary_by_gender = df.groupby('Gender')['Salary'].mean()
print("\nAverage Salary by Gender:")
print(avg_salary_by_gender)

# 4. **Salary Distribution by Gender**
sns.boxplot(x='Gender', y='Salary', data=df)
plt.title('Salary Distribution by Gender')
plt.show()

# 5. **Performance Categories**: Categorizing employees by performance score
def categorize_performance(score):
    if score <= 60:
        return 'Low'
    elif 61 <= score <= 80:
        return 'Medium'
    else:
        return 'High'

df['Performance Category'] = df['Performance Score'].apply(categorize_performance)

# 6. **Performance Categories Distribution**
performance_dist = df['Performance Category'].value_counts()
print("\nPerformance Categories Distribution:")
print(performance_dist)

# 7. **Visualizing Salary vs. Years at Company**
plt.figure(figsize=(8,6))
sns.scatterplot(x='Years at Company', y='Salary', data=df, hue='Gender', style='Gender')
plt.title('Salary vs. Years at Company')
plt.xlabel('Years at Company')
plt.ylabel('Salary')
plt.show()

# 8. **Visualizing Performance Scores by Department**
plt.figure(figsize=(8,6))
sns.boxplot(x='Department', y='Performance Score', data=df)
plt.title('Performance Scores by Department')
plt.show()