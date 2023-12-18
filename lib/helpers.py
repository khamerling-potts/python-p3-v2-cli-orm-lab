from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()


# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f"Department {name} not found")


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Success: {department}")
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f"Success: {department}")
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f"Department {id_} not found")


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f"Department {id_} deleted")
    else:
        print(f"Department {id_} not found")


# You'll implement the employee functions in the lab


def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter employee's name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print(f"Employee {name} not found")


def find_employee_by_id():
    id = input("Enter employee's id: ")
    employee = Employee.find_by_id(id)
    print(employee) if employee else print(f"Employee {id} not found")


def create_employee():
    name = input("Enter employee's name: ")
    job = input("Enter employee's job title: ")
    department_id = int(input("Enter employee's department id: "))
    try:
        employee = Employee.create(name, job, department_id)
        print(f"Success: {employee}")
    except Exception as exc:
        print(f"Error creating employee: {exc}")


def update_employee():
    id = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id):
        try:
            name = input("Enter new name: ")
            employee.name = name
            job = input("Enter new job title: ")
            employee.job_title = job
            department_id = int(input("Enter new department id: "))
            employee.department_id = department_id
            employee.update()
            print("Success updating employee: ", employee)
        except Exception as exc:
            print("Error creating employee: ", exc)
    else:
        print(f"Employee {id} does not exist in the database")


def delete_employee():
    id = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id):
        employee.delete()
        print("Success deleting employee ", id)
    else:
        print(f"Employee {id} is not in the database")


def list_department_employees():
    department_id = input("Enter department's id: ")
    if department := Department.find_by_id(department_id):
        print([employee for employee in department.employees()])
    else:
        print(f"Department {department_id} does not exist in the database")
