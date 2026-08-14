class Employee:
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.salary = salary
    def display(self):
        # YOUR TURN: Finish this f-string using self.department and self.salary
        print(f"ID: {self.emp_id}, Name: {self.name}, Department: {self.department}, Salary: {self.salary}")
class EmployeeManager:
    def __init__(self):
        self.employees = {}
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        name = input("Enter Name: ")
        department = input("Enter Department: ")
        salary = input("Enter Salary: ")
        new_employee = Employee(emp_id, name, department, salary)
        self.employees[emp_id] = new_employee
        print("Employee added successfully!")

    def view_employees(self):
        if len(self.employees) == 0:
            print("No employees found!")
        else:
            print("\n--- Employee List ---")
            for emp_id, employee in self.employees.items():
                employee.display()
    def search_employee(self):
        emp_id = input("Enter Employee ID to search: ")
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            employee.display()
        else:
            print("Employee not found!")
    def update_employee(self):
        emp_id = input("Enter Employee ID to update: ")
        
        if emp_id in self.employees:
            employee = self.employees[emp_id]
            print("Current details:")
            # We can use our handy display method!
            employee.display() 
            
            print("\nEnter new details (press Enter to keep current value):")
            # 2. Use the object's attributes (employee.name) in the f-string
            name = input(f"Name ({employee.name}): ") or employee.name
            department = input(f"Department ({employee.department}): ") or employee.department
            salary = input(f"Salary ({employee.salary}):") or employee.salary    
            employee.name = name
            employee.department = department
            employee.salary = salary
            print("Employee updated successfully!")
        else:
            print("Employee not found!")
    def delete_employee(self):
        emp_id = input("Enter Employee ID to delete: ")
        if emp_id in self.employees:
            del self.employees[emp_id]
            print("Employee deleted successfully!")
        else:
            print("Employee not found!")
def main():
    # 1. Hire the manager! This creates the actual object.
    manager = EmployeeManager()
    while True:
        print("\nSelect Appropriate option:")
        print("1. Add \n2. View \n3. Search \n4. Update \n5. Delete \n6. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            manager.add_employee()
        elif choice == '2':
            manager.view_employees()
        elif choice == '3':
            manager.search_employee()
        elif choice == '4':
            manager.update_employee()
        elif choice == '5':
            manager.delete_employee()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()