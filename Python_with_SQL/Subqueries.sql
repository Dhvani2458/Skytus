USE company_db;

-- 1. Find employees earning more than average salary
SELECT *
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
);


-- 2. Find department with highest total salary
SELECT d.dept_name, SUM(e.salary) AS total_salary
FROM employees e
JOIN departments d
    ON e.dept_id = d.dept_id
GROUP BY d.dept_id, d.dept_name
HAVING SUM(e.salary) = (
    SELECT MAX(total_salary)
    FROM (
        SELECT SUM(salary) AS total_salary
        FROM employees
        WHERE dept_id IS NOT NULL
        GROUP BY dept_id
    ) AS dept_totals
);


-- 3. Display employee with second highest salary
SELECT *
FROM employees
WHERE salary = (
    SELECT MAX(salary)
    FROM employees
    WHERE salary < (
        SELECT MAX(salary)
        FROM employees
    )
);


-- 4. Display employees working in same department as "Amit"
SELECT *
FROM employees
WHERE dept_id = (
    SELECT dept_id
    FROM employees
    WHERE emp_name = 'Amit'
);