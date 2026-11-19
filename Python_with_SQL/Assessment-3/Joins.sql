CREATE DATABASE company_db;

USE company_db;

CREATE TABLE employee (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(50),
    dept_id INT,
    salary INT
    );

CREATE TABLE departments (
    dept_id INT PRIMARY KEY,
    dept_name VARCHAR(50) 
    ); 

INSERT INTO employees (emp_id, emp_name, dept_id, salary)
VALUES
(101, 'Dhvani', 1, 65000),
(102, 'Rahul', 1, 55000),
(103, 'Priya', 1, 72000),
(104, 'Amit', 2, 48000),
(105, 'Neha', 2, 52000),
(106, 'Karan', 3, 60000),
(107, 'Riya', 3, 45000),
(108, 'Vivek', 4, 75000),
(109, 'Anjali', 4, 58000),
(110, 'Mehul', NULL, 50000);

INSERT INTO departments (dept_id, dept_name)
VALUES
(1, 'IT'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing'),
(5, 'Sales');

-- 1. Display employee name with department name
SELECT 
    e.emp_name,
    d.dept_name
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id;


-- 2. Display employees earning more than 50,000
SELECT *
FROM employees
WHERE salary > 50000;


-- 3. Display department-wise total salary
SELECT 
    d.dept_name,
    SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name;


-- 4. Display departments with more than 2 employees
SELECT 
    d.dept_name,
    COUNT(e.emp_id) AS employee_count
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_name
HAVING COUNT(e.emp_id) > 2;


-- 5. Display employees without a department
SELECT *
FROM employees
WHERE dept_id IS NULL;