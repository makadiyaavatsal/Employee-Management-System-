employees = {}

def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")
    employees[emp_id] = {
        'name': name,
        'department': department,
        'salary': salary
    }
    print("Employee added successfully!")

def view_employees():
    if len(employees) == 0:
        print("No employees found!")
    else:
        print("\n--- Employee List ---")
        for emp_id, details in employees.items():
            print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Salary: {details['salary']}")

def search_employee():
    emp_id = input("Enter Employee ID to search: ")
    if emp_id in employees:
        details = employees[emp_id]
        print(f"ID: {emp_id}, Name: {details['name']}, Department: {details['department']}, Salary: {details['salary']}")
    else:
        print("Employee not found!")

def update_employee():
    emp_id = input("Enter Employee ID to update: ")
    if emp_id in employees:
        print("Current details:")
        print(f"ID: {emp_id}, Name: {employees[emp_id]['name']}, Department: {employees[emp_id]['department']}, Salary: {employees[emp_id]['salary']}")
        print("\nEnter new details (press Enter to keep current value):")
        name = input(f"Name ({employees[emp_id]['name']}): ") or employees[emp_id]['name']
        department = input(f"Department ({employees[emp_id]['department']}): ") or employees[emp_id]['department']
        salary = input(f"Salary ({employees[emp_id]['salary']}): ") or employees[emp_id]['salary']
        
        employees[emp_id] = {
            'name': name,
            'department': department,
            'salary': salary
        }
        print("Employee updated successfully!")
    else:
        print("Employee not found!")

def delete_employee():
    emp_id = input("Enter Employee ID to delete: ")
    if emp_id in employees:
        del employees[emp_id]
        print("Employee deleted successfully!")
    else:
        print("Employee not found!")

def main():  
    while True:
        print("\nSelect Appropriate option:")
        print("1. Add \n2. View \n3. Search \n4. Update \n5. Delete \n6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            view_employees()
        elif choice == '3':
            search_employee()
        elif choice == '4':
            update_employee()
        elif choice == '5':
            delete_employee()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()