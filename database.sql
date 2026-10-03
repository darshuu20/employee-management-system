CREATE DATABASE IF NOT EXISTS employee_management;

USE employee_management;

CREATE TABLE IF NOT EXISTS employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    department VARCHAR(50),
    salary DECIMAL(10,2),
    location VARCHAR(100)
);