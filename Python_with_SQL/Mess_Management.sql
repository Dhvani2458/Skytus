CREATE DATABASE mess_management;

USE mess_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(100) NOT NULL,
    gender VARCHAR(10),
    room_no VARCHAR(20),
    phone VARCHAR(15)
);

CREATE TABLE meals (
    meal_id INT PRIMARY KEY,
    meal_date DATE NOT NULL,
    meal_type VARCHAR(20) NOT NULL,
    menu VARCHAR(255),
    price DECIMAL(10,2)
);

CREATE TABLE meal_attendance (
    attendance_id INT PRIMARY KEY,
    student_id INT,
    meal_id INT,
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (meal_id) REFERENCES meals(meal_id)
);

CREATE TABLE payments (
    payment_id INT PRIMARY KEY,
    student_id INT,
    payment_date DATE,
    amount DECIMAL(10,2),
    payment_status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE complaints (
    complaint_id INT PRIMARY KEY,
    student_id INT,
    complaint_date DATE,
    complaint_type VARCHAR(50),
    description VARCHAR(255),
    status VARCHAR(20),
    FOREIGN KEY (student_id) REFERENCES students(student_id)
);

INSERT INTO students VALUES
(1, 'Dhvani', 'Female', 'A101', '9876543210'),
(2, 'Rahul', 'Male', 'A102', '9876543211'),
(3, 'Priya', 'Female', 'A103', '9876543212'),
(4, 'Amit', 'Male', 'A104', '9876543213'),
(5, 'Neha', 'Female', 'A105', '9876543214'),
(6, 'Karan', 'Male', 'A106', '9876543215');

INSERT INTO meals VALUES
(1, '2026-10-01', 'Breakfast', 'Poha, Tea', 40),
(2, '2026-10-01', 'Lunch', 'Dal, Rice, Roti, Sabzi', 80),
(3, '2026-10-01', 'Dinner', 'Paneer, Roti, Rice', 90),
(4, '2026-10-02', 'Breakfast', 'Idli, Sambar, Tea', 45),
(5, '2026-10-02', 'Lunch', 'Rajma, Rice, Roti', 75),
(6, '2026-10-02', 'Dinner', 'Dal, Roti, Mix Veg', 80),
(7, '2026-10-03', 'Breakfast', 'Upma, Tea', 40),
(8, '2026-10-03', 'Lunch', 'Chole, Rice, Roti', 75),
(9, '2026-10-03', 'Dinner', 'Paneer, Dal, Roti', 90);

INSERT INTO meal_attendance VALUES
(1, 1, 1, 'Present'),
(2, 2, 1, 'Present'),
(3, 3, 1, 'Absent'),
(4, 1, 2, 'Present'),
(5, 2, 2, 'Present'),
(6, 3, 2, 'Present'),
(7, 4, 2, 'Absent'),
(8, 5, 2, 'Present'),
(9, 1, 3, 'Present'),
(10, 2, 3, 'Absent'),
(11, 3, 3, 'Present'),
(12, 4, 3, 'Present'),
(13, 5, 3, 'Present'),
(14, 6, 3, 'Present'),
(15, 1, 4, 'Present'),
(16, 2, 4, 'Present'),
(17, 3, 4, 'Present'),
(18, 4, 4, 'Present'),
(19, 5, 4, 'Absent'),
(20, 6, 4, 'Present');

INSERT INTO payments VALUES
(1, 1, '2026-10-01', 3000, 'Paid'),
(2, 2, '2026-10-01', 3000, 'Paid'),
(3, 3, '2026-10-01', 2800, 'Paid'),
(4, 4, '2026-10-01', 2500, 'Paid'),
(5, 5, '2026-10-01', 3000, 'Pending'),
(6, 6, '2026-10-01', 2700, 'Paid');

INSERT INTO complaints VALUES
(1, 1, '2026-10-01', 'Food Quality', 'Food was too spicy', 'Open'),
(2, 2, '2026-10-01', 'Cleanliness', 'Dining area needs cleaning', 'Resolved'),
(3, 3, '2026-10-02', 'Food Quality', 'Food was cold', 'Open'),
(4, 4, '2026-10-02', 'Service', 'Late dinner service', 'Resolved'),
(5, 5, '2026-10-03', 'Food Quality', 'Less quantity of food', 'Open');

SELECT * FROM students;
SELECT * FROM meals;

SELECT DISTINCT s.student_id, s.student_name
FROM students s
JOIN meal_attendance ma
ON s.student_id = ma.student_id
WHERE ma.status = 'Present';

SELECT s.student_name, COUNT(ma.attendance_id) AS meals_attended
FROM students s
JOIN meal_attendance ma
ON s.student_id = ma.student_id
WHERE ma.status = 'Present'
GROUP BY s.student_id, s.student_name;

SELECT s.student_name, m.meal_date, m.meal_type
FROM students s
JOIN meal_attendance ma
ON s.student_id = ma.student_id
JOIN meals m
ON ma.meal_id = m.meal_id
WHERE ma.status = 'Absent';

SELECT s.student_name, SUM(p.amount) AS total_paid
FROM students s
JOIN payments p
ON s.student_id = p.student_id
WHERE p.payment_status = 'Paid'
GROUP BY s.student_id, s.student_name;

SELECT s.student_name, p.amount, p.payment_status
FROM students s
JOIN payments p
ON s.student_id = p.student_id
WHERE p.payment_status = 'Pending';

SELECT SUM(amount) AS total_revenue
FROM payments
WHERE payment_status = 'Paid';

SELECT *
FROM meals
ORDER BY price DESC
LIMIT 1;

SELECT COUNT(*) AS total_complaints
FROM complaints;

SELECT s.student_name, c.complaint_type, c.description
FROM complaints c
JOIN students s
ON c.student_id = s.student_id
WHERE c.status = 'Open';

SELECT complaint_type, COUNT(*) AS total_complaints
FROM complaints
GROUP BY complaint_type;

SELECT s.student_name, COUNT(ma.attendance_id) AS total_meals
FROM students s
JOIN meal_attendance ma
ON s.student_id = ma.student_id
WHERE ma.status = 'Present'
GROUP BY s.student_id, s.student_name
HAVING COUNT(ma.attendance_id) > 1;


SELECT DISTINCT s.student_id, s.student_name
FROM students s
JOIN complaints c
ON s.student_id = c.student_id;

SELECT DISTINCT s.student_id, s.student_name
FROM students s
JOIN complaints c
ON s.student_id = c.student_id;

CREATE INDEX idx_attendance_student
ON meal_attendance(student_id);

CREATE INDEX idx_attendance_meal
ON meal_attendance(meal_id);

CREATE INDEX idx_payment_student
ON payments(student_id);

CREATE INDEX idx_complaint_student
ON complaints(student_id);

SELECT s.student_name, COUNT(ma.attendance_id) AS meals_attended
FROM students s
JOIN meal_attendance ma
ON s.student_id = ma.student_id
WHERE ma.status = 'Present'
GROUP BY s.student_id, s.student_name;

SELECT s.student_name, SUM(p.amount) AS total_paid
FROM students s
JOIN payments p
ON s.student_id = p.student_id
WHERE p.payment_status = 'Paid'
GROUP BY s.student_id, s.student_name;

SELECT s.student_name, c.complaint_type, c.description
FROM complaints c
JOIN students s
ON c.student_id = s.student_id
WHERE c.status = 'Open';