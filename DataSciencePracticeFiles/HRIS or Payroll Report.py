import pandas as pd

# Sample Payroll Data
data = {
    'Employee ID': [1001, 1002, 1003, 1004, 1005],
    'Employee Name': ['John Doe', 'Jane Smith', 'Jim Brown', 'Linda White', 'Tom Black'],
    'Department': ['Sales', 'Marketing', 'Engineering', 'HR', 'Finance'],
    'Salary': [50000, 55000, 70000, 48000, 60000],
    'Overtime Hours': [10, 5, 8, 0, 15],
    'Overtime Rate': [25, 30, 35, 20, 40]
}

# Create DataFrame
payroll_data = pd.DataFrame(data)

# Calculate Total Salary (Salary + Overtime Pay)
payroll_data['Overtime Pay'] = payroll_data['Overtime Hours'] * payroll_data['Overtime Rate']
payroll_data['Total Salary'] = payroll_data['Salary'] + payroll_data['Overtime Pay']

# Show the data
print(payroll_data)
