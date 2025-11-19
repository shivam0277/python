import json
from collections import Counter

FILE_PATH = "employees.json"

def read_employee_data():
    """Reads and returns employee data from JSON file safely."""
    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            if not isinstance(data, list):
                raise ValueError("JSON data is not a list!")
            return data
    except FileNotFoundError:
        print("Error: employees.json file not found!")
        return []
    except json.JSONDecodeError:
        print("Error: JSON file is malformed!")
        return []
    except Exception as e:
        print("Unexpected error:", e)
        return []

def print_stats(employees):
    """Print all required statistics."""
    if not employees:
        print("No employee data found.")
        return

    # Total employees
    print(f"\nTotal Employees: {len(employees)}")

    # Department-wise count
    try:
        dept_counts = Counter(emp["dept"] for emp in employees)
        print("\nDepartment-wise Count:")
        for dept, count in dept_counts.items():
            print(f"{dept}: {count}")
    except KeyError:
        print("Error: One or more employee records are missing the 'dept' key.")

    # Highest-paid employee
    try:
        highest_paid = max(employees, key=lambda e: e["salary"])
        print("\nHighest Paid Employee:")
        print(f"{highest_paid['name']} (${highest_paid['salary']})")
    except KeyError:
        print("Error: Missing 'salary' or 'name' key in records.")
    except ValueError:
        print("Error: No valid salary data found.")

def append_employee(new_emp):
    """Safely appends a new employee record to the JSON file."""
    employees = read_employee_data()
    
    # Validate keys
    required_keys = {"name", "dept", "salary"}
    if not required_keys.issubset(new_emp.keys()):
        print("Error: New employee record is missing required fields!")
        return

    employees.append(new_emp)

    try:
        with open(FILE_PATH, "w") as file:
            json.dump(employees, file, indent=2)
        print("\nNew employee added successfully!")
    except Exception as e:
        print("Failed to write to file:", e)


if __name__ == "__main__":
    # Step 1: Read existing employee data
    data = read_employee_data()

    # Step 2: Print required statistics
    print_stats(data)

    # Step 3: Append a new employee (example)
    new_employee = {
        "name": "Charlie",
        "dept": "Finance",
        "salary": 78000
    }

    append_employee(new_employee)

# Example content of employees.json after appending:
[ {"name": "Alice", "dept": "IT", "salary": 85000}, {"name": "Bob", "dept": "HR", "salary": 60000} ]