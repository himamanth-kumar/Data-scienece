import csv

# Sample employee data for 3 different companies
employee_data = [
    {"EmployeeID": 1, "Name": "John Doe", "Age": 28, "Department": "HR", "Company": "Company A"},
    {"EmployeeID": 2, "Name": "Jane Smith", "Age": 34, "Department": "Finance", "Company": "Company A"},
    {"EmployeeID": 3, "Name": "Jim Brown", "Age": 26, "Department": "IT", "Company": "Company A"},
    {"EmployeeID": 4, "Name": "Emily Davis", "Age": 30, "Department": "Sales", "Company": "Company A"},
    {"EmployeeID": 5, "Name": "Michael Wilson", "Age": 41, "Department": "Marketing", "Company": "Company A"},
    {"EmployeeID": 6, "Name": "Sarah Miller", "Age": 39, "Department": "HR", "Company": "Company A"},
    {"EmployeeID": 7, "Name": "David Martinez", "Age": 32, "Department": "Finance", "Company": "Company A"},
    {"EmployeeID": 8, "Name": "Linda Garcia", "Age": 25, "Department": "IT", "Company": "Company A"},
    {"EmployeeID": 9, "Name": "James Harris", "Age": 37, "Department": "Sales", "Company": "Company A"},
    {"EmployeeID": 10, "Name": "Rachel Clark", "Age": 29, "Department": "Marketing", "Company": "Company A"},
    
    {"EmployeeID": 11, "Name": "William Walker", "Age": 29, "Department": "HR", "Company": "Company B"},
    {"EmployeeID": 12, "Name": "Olivia Hall", "Age": 34, "Department": "Finance", "Company": "Company B"},
    {"EmployeeID": 13, "Name": "Liam Allen", "Age": 27, "Department": "IT", "Company": "Company B"},
    {"EmployeeID": 14, "Name": "Sophia Young", "Age": 35, "Department": "Sales", "Company": "Company B"},
    {"EmployeeID": 15, "Name": "Benjamin King", "Age": 42, "Department": "Marketing", "Company": "Company B"},
    {"EmployeeID": 16, "Name": "Charlotte Wright", "Age": 38, "Department": "HR", "Company": "Company B"},
    {"EmployeeID": 17, "Name": "Alexander Scott", "Age": 31, "Department": "Finance", "Company": "Company B"},
    {"EmployeeID": 18, "Name": "Amelia Adams", "Age": 33, "Department": "IT", "Company": "Company B"},
    {"EmployeeID": 19, "Name": "Henry Nelson", "Age": 29, "Department": "Sales", "Company": "Company B"},
    {"EmployeeID": 20, "Name": "Eva Carter", "Age": 40, "Department": "Marketing", "Company": "Company B"},
    
    {"EmployeeID": 21, "Name": "Daniel Lewis", "Age": 28, "Department": "HR", "Company": "Company C"},
    {"EmployeeID": 22, "Name": "Mia Robinson", "Age": 36, "Department": "Finance", "Company": "Company C"},
    {"EmployeeID": 23, "Name": "Jack Lee", "Age": 27, "Department": "IT", "Company": "Company C"},
    {"EmployeeID": 24, "Name": "Grace Hall", "Age": 31, "Department": "Sales", "Company": "Company C"},
    {"EmployeeID": 25, "Name": "Ethan White", "Age": 43, "Department": "Marketing", "Company": "Company C"},
    {"EmployeeID": 26, "Name": "Chloe Perez", "Age": 39, "Department": "HR", "Company": "Company C"},
    {"EmployeeID": 27, "Name": "Matthew Gonzalez", "Age": 32, "Department": "Finance", "Company": "Company C"},
    {"EmployeeID": 28, "Name": "Isabella Miller", "Age": 30, "Department": "IT", "Company": "Company C"},
    {"EmployeeID": 29, "Name": "Sebastian Lee", "Age": 33, "Department": "Sales", "Company": "Company C"},
    {"EmployeeID": 30, "Name": "Zoe Hernandez", "Age": 38, "Department": "Marketing", "Company": "Company C"}
]

# Define CSV file path
file_path = "employees.csv"

# Writing to CSV
with open(file_path, mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["EmployeeID", "Name", "Age", "Department", "Company"])
    writer.writeheader()
    writer.writerows(employee_data)

print(f"CSV file 'employees.csv' has been created successfully!")
