USE college;

-- 1. Count total number of students
SELECT COUNT(*) AS total_students
FROM students;

-- 2. Find average marks of students
SELECT AVG(marks) AS average_marks
FROM students;

-- 3. Find highest and lowest marks
SELECT 
    MAX(marks) AS highest_marks,
    MIN(marks) AS lowest_marks
FROM students;

-- 4. Find department-wise average marks
SELECT 
    department,
    AVG(marks) AS average_marks
FROM students
GROUP BY department;

-- 5. Display departments where average marks > 70
SELECT 
    department,
    AVG(marks) AS average_marks
FROM students
GROUP BY department
HAVING AVG(marks) > 70;