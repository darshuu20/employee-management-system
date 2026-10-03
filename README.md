# Employee Management System

A simple Employee Management System built using **Python and MySQL**.

## Features

* Add Employee
* View All Employees
* Search Employee by ID
* Update Employee
* Delete Employee
* Input validation
* MySQL database integration

## Technologies Used

* Python
* MySQL
* mysql-connector-python

## Project Structure

```text
Employee management system/
│
├── database.sql
├── db.py
├── main.py
├── requirements.txt
├── .gitignore
└── myenv/
```

## Database

The project uses a MySQL database named:

```text
employee_management
```

The `employees` table contains:

* employee_id
* name
* age
* department
* salary
* location

## Installation

Create and activate a virtual environment:

```cmd
python -m venv myenv
myenv\Scripts\activate
```

Install the required package:

```cmd
pip install -r requirements.txt
```

Set the MySQL password in the current Windows CMD session:

```cmd
set MYSQL_PASSWORD=YOUR_MYSQL_PASSWORD
```

Run the application:

```cmd
py main.py
```

## Main Menu

```text
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
```

## Purpose

This project was created to practice Python programming, MySQL, CRUD operations, database connectivity, SQL queries, and basic exception handling.
