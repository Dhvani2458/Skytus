USE company_db;

-- 1. Nth highest salary (3rd highest)
SELECT DISTINCT salary
FROM employee
ORDER BY salary DESC
LIMIT 1 OFFSET 2;


-- 2. Find duplicate records
SELECT emp_name, dept_id, salary, COUNT(*) AS total
FROM employee
GROUP BY emp_name, dept_id, salary
HAVING COUNT(*) > 1;


-- 3. Find records common in two tables
SELECT e.emp_id, e.emp_name, e.dept_id, d.dept_name
FROM employee e
INNER JOIN departments d
ON e.dept_id = d.dept_id;


-- 4. Employees hired in last 6 months
ALTER TABLE employee
ADD hire_date DATE;

SELECT *
FROM employee
WHERE hire_date >= DATE_SUB(CURDATE(), INTERVAL 6 MONTH);


-- 5. Continuous duplicate values
SELECT *
FROM (
    SELECT
        emp_id,
        emp_name,
        salary,
        LAG(salary) OVER (ORDER BY emp_id) AS previous_salary
    FROM employee
) AS x
WHERE salary = previous_salary;

