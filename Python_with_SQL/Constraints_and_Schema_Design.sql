USE company_db;

CREATE TABLE users (
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO users (name, email, password)
VALUES
('Dhvani', 'dhvani@gmail.com', '12345'),
('Rahul', 'rahul@gmail.com', 'abc123'),
('Priya', 'priya@gmail.com', 'pass123');

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO orders (user_id, order_date, amount)
VALUES
(1, '2026-10-01', 500.00),
(1, '2026-10-02', 750.00),
(2, '2026-10-03', 300.00);

CREATE INDEX idx_email ON users(email);

CREATE VIEW user_order_summary AS
SELECT 
    u.user_id,
    u.name,
    u.email,
    COUNT(o.order_id) AS total_orders,
    COALESCE(SUM(o.amount), 0) AS total_amount
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.name, u.email;

SELECT * FROM user_order_summary;