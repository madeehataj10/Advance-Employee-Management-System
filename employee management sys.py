import sqlite3
from prettytable import PrettyTable

sqlite3: #This is Python’s built-in module for handling databases.

conn = sqlite3.connect("employee_payroll.db")
cursor = conn.cursor()

sqlite3.connect("employee_payroll.db"):

cursor = conn.cursor()

##This creates a cursor object to execute SQL commands.
#Step 3: Dropping the Table if It Already Exists
cursor.execute("DROP TABLE IF EXISTS employees")
conn.commit()

cursor.execute('''CREATE TABLE employees (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
date_of_joining TEXT,
basic_salary REAL,
overtime_hours INTEGER,
overtime_rate REAL,
medical_expenses REAL,
deductions REAL,
start_date TEXT,
end_date TEXT,
leaves_taken INTEGER,
allowances REAL
)''')
conn.commit()
Understanding Each Column
Column Name
Data Type
Description
id
INTEGER PRIMARY KEY AUTOINCREMENT
Unique ID for each employee, automatically increasing
name
TEXT NOT NULL
Employee's name (Cannot be empty)
date_of_joining
TEXT
The date when the employee joined
basic_salary
REAL
The fixed salary of the employee
overtime_hours
INTEGER
Number of extra hours worked
overtime_rate
REAL
Payment per extra hour worked
medical_expenses
REAL
Amount reimbursed for medical expenses
deductions
REAL
Any salary deductions (like tax, absence, etc.)
start_date
TEXT
Start date of the payroll period
end_date
TEXT
End date of the payroll period
leaves_taken
INTEGER
Number of leaves taken in the period
allowances
REAL
#Additional earnings (like bonuses, house rent, etc.)

INTEGER: Stores whole numbers (like number of leaves taken).
#Step 5: Function to Add Employee Data
def add_employee(name, doj, salary, ot_hours, ot_rate, med_exp, deductions, start, end, leaves, allowances):
cursor.execute('''INSERT INTO employees (name, date_of_joining, basic_salary, overtime_hours, overtime_rate,
medical_expenses, deductions, start_date, end_date, leaves_taken, allowances)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
(name, doj, salary, ot_hours, ot_rate, med_exp, deductions, start, end, leaves, allowances))
conn.commit()


"INSERT INTO employees (...)":

"VALUES (?, ?, ?, ..., ?)":



add_employee("John Doe", "2022-01-15", 50000, 10, 200, 3000, 5000, "2024-02-01", "2024-02-28", 2, 7000)

#Step 6: Function to Generate Payslip
def generate_payslip(emp_id):
cursor.execute("SELECT * FROM employees WHERE id = ?", (emp_id,))
employee = cursor.fetchone()

if not employee:
print("Employee not found!")
return

emp_name, doj, salary, ot_hours, ot_rate, med_exp, deductions, start, end, leaves, allowances = employee[1:]

employee[1:] #extracts the data fields, excluding the id.

#Creates a PrettyTable object with columns "Field" and "Details".
table.add_row(["Employee Name", emp_name])
table.add_row(["Date of Joining", doj])
table.add_row(["Basic Salary", f"₹{salary:.2f}"])
table.add_row(["Overtime Hours", ot_hours])
table.add_row(["Overtime Pay", f"₹{overtime_pay:.2f}"])
table.add_row(["Medical Expenses", f"₹{med_exp:.2f}"])
table.add_row(["Allowances", f"₹{allowances:.2f}"])
table.add_row(["Leaves Taken", leaves])
table.add_row(["Deductions", f"₹{deductions:.2f}"])
table.add_row(["Gross Salary", f"₹{gross_salary:.2f}"])
table.add_row(["Net Salary", f"₹{net_salary:.2f}"])

print(f"\nPAYSLIP for {emp_name}")
print(table)
generate_payslip(1)
conn.close()