employees = []


def add_employee(emp_id, name, job_title, salary):
    employee = {
        "id": emp_id,
        "name": name,
        "job_title": job_title,
        "salary": salary
    }
    employees.append(employee)
    print('Employee Added Successfully')


def search_employee(emp_id):
    for i, employee in enumerate(employees):
        if employee["id"] == emp_id:
            return i
    return -1


def update_employee(emp_id, salary):
    index = search_employee(emp_id)
    if index != -1:
        employees[index]["salary"] = salary
        print('Employee Updated Successfully')
    else:
        print('Employee Not Found.')


def delete_employee(emp_id):
    index = search_employee(emp_id)
    if index != -1:
        employees.pop(index)
        print('Employee Deleted Successfully')
    else:
        print('Employee Not Found.')


while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee Salary")
    print("4. Delete Employee")
    print("5. Show All Employees")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))
        name = input("Enter Name: ")
        job_title = input("Enter Job Title: ")
        salary = float(input("Enter Salary: "))
        add_employee(emp_id, name, job_title, salary)

    elif choice == 2:
        emp_id = int(input("Enter Employee ID to search: "))
        index = search_employee(emp_id)
        if index != -1:
            print("Employee Found:", employees[index])
        else:
            print("Employee Not Found.")

    elif choice == 3:
        emp_id = int(input("Enter Employee ID to update: "))
        salary = float(input("Enter New Salary: "))
        update_employee(emp_id, salary)

    elif choice == 4:
        emp_id = int(input("Enter Employee ID to delete: "))
        delete_employee(emp_id)

    elif choice == 5:
        print("\n All Employees:")
        for emp in employees:
            print(emp)

    elif choice == 6:
        print("Exiting Program..Bye")
        break

    else:
        print("Invalid Choice. Please Try Again.")
