from db import create_connection


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid salary.")


def add_employee():
    name = input("Enter employee name: ")
    age = get_integer("Enter age: ")
    department = input("Enter department: ")
    salary = get_float("Enter salary: ")
    location = input("Enter location: ")

    connection = create_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO employees (name, age, department, salary, location)
        VALUES (%s, %s, %s, %s, %s)
    """

    values = (name, age, department, salary, location)

    cursor.execute(query, values)
    connection.commit()

    print("\nEmployee added successfully!")

    cursor.close()
    connection.close()


def view_employees():
    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM employees"
    cursor.execute(query)

    employees = cursor.fetchall()

    if not employees:
        print("\nNo employees found.")
    else:
        print("\n========== EMPLOYEE DETAILS ==========")

        for employee in employees:
            print("Employee ID:", employee[0])
            print("Name:", employee[1])
            print("Age:", employee[2])
            print("Department:", employee[3])
            print("Salary:", employee[4])
            print("Location:", employee[5])
            print("--------------------------------------")

    cursor.close()
    connection.close()


def search_employee():
    employee_id = get_integer("Enter employee ID: ")

    connection = create_connection()
    cursor = connection.cursor()

    query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(query, (employee_id,))

    employee = cursor.fetchone()

    if employee:
        print("\n========== EMPLOYEE FOUND ==========")
        print("Employee ID:", employee[0])
        print("Name:", employee[1])
        print("Age:", employee[2])
        print("Department:", employee[3])
        print("Salary:", employee[4])
        print("Location:", employee[5])
    else:
        print("\nEmployee not found.")

    cursor.close()
    connection.close()


def update_employee():
    employee_id = get_integer("Enter employee ID to update: ")

    connection = create_connection()
    cursor = connection.cursor()

    check_query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(check_query, (employee_id,))

    employee = cursor.fetchone()

    if employee is None:
        print("\nEmployee not found.")
        cursor.close()
        connection.close()
        return

    print("\nEnter new employee details:")

    name = input("Enter new name: ")
    age = get_integer("Enter new age: ")
    department = input("Enter new department: ")
    salary = get_float("Enter new salary: ")
    location = input("Enter new location: ")

    query = """
        UPDATE employees
        SET name = %s,
            age = %s,
            department = %s,
            salary = %s,
            location = %s
        WHERE employee_id = %s
    """

    values = (name, age, department, salary, location, employee_id)

    cursor.execute(query, values)
    connection.commit()

    print("\nEmployee updated successfully!")

    cursor.close()
    connection.close()


def delete_employee():
    employee_id = get_integer("Enter employee ID to delete: ")

    connection = create_connection()
    cursor = connection.cursor()

    check_query = "SELECT * FROM employees WHERE employee_id = %s"
    cursor.execute(check_query, (employee_id,))

    employee = cursor.fetchone()

    if employee is None:
        print("\nEmployee not found.")
        cursor.close()
        connection.close()
        return

    confirm = input("Are you sure you want to delete this employee? (yes/no): ")

    if confirm.lower() == "yes":
        query = "DELETE FROM employees WHERE employee_id = %s"

        cursor.execute(query, (employee_id,))
        connection.commit()

        print("\nEmployee deleted successfully!")
    else:
        print("\nDelete cancelled.")

    cursor.close()
    connection.close()


def main():
    while True:
        print("\n====================================")
        print("      EMPLOYEE MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        print("====================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            print("\nThank you for using Employee Management System!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 6.")


if __name__ == "__main__":
    main()