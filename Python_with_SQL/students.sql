CREATE DATABASE college;

USE college;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(30),
    year INT,
    marks INT
);

INSERT INTO students (student_id, name, department, year, marks)
VALUES
(1, 'Dhvani', 'CSE', 4, 85),
(2, 'Rahul', 'IT', 3, 72),
(3, 'Priya', 'CSE', 2, 91),
(4, 'Amit', 'ECE', 4, 68),
(5, 'Neha', 'IT', 3, 88),
(6, 'Karan', 'CSE', 4, 95),
(7, 'Riya', 'ME', 2, 76);

-- Display all student records
SELECT * FROM students;

-- Display name and department
SELECT name, department
FROM students;

-- Display students from CSE department
SELECT *
FROM students
WHERE department = 'CSE';

-- Display students with marks less than 75
SELECT *
FROM students
WHERE marks < 75;

-- Display students with marks greater than 75
SELECT *
FROM students
WHERE marks > 75;

-- Sort students by marks in descending order
SELECT *
FROM students
ORDER BY marks DESC;

-- Display top 3 scorers
SELECT *
FROM students
ORDER BY marks DESC
LIMIT 3;