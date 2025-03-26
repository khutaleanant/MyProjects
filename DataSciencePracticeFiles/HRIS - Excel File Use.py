import openpyxl
from openpyxl.styles import Font

# Create a new workbook and a sheet
wb = openpyxl.Workbook()
ws = wb.active
ws.title = "Payroll Report"

# Sample Data (could be from the payroll_data DataFrame in pandas)
data = [
    ['Employee ID', 'Employee Name', 'Department', 'Salary', 'Overtime Hours', 'Overtime Rate', 'Overtime Pay', 'Total Salary'],
    [1001, 'John Doe', 'Sales', 50000, 10, 25, 250, 50250],
    [1002, 'Jane Smith', 'Marketing', 55000, 5, 30, 150, 55150],
    [1003, 'Jim Brown', 'Engineering', 70000, 8, 35, 280, 70280],
    [1004, 'Linda White', 'HR', 48000, 0, 20, 0, 48000],
    [1005, 'Tom Black', 'Finance', 60000, 15, 40, 600, 60600]
]

# Add data to the sheet
for row in data:
    ws.append(row)

# Apply formatting to the headers
for cell in ws[1]:
    cell.font = Font(bold=True)

# Save the workbook to a file
wb.save('payroll_report_openpyxl.xlsx')

print("Payroll report saved using openpyxl.")