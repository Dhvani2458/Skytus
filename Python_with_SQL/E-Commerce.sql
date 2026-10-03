CREATE DATABASE ecommerce_db;
USE ecommerce_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100),
    city VARCHAR(50)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE,
    amount DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE products (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE order_items (
    order_id INT,
    product_id INT,
    quantity INT,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);

INSERT INTO customers (customer_id, name, city) VALUES
(1, 'Dhvani', 'Surat'),
(2, 'Rahul', 'Mumbai'),
(3, 'Priya', 'Ahmedabad'),
(4, 'Amit', 'Surat'),
(5, 'Neha', 'Vadodara'),
(6, 'Karan', 'Mumbai'),
(7, 'Riya', 'Rajkot');

INSERT INTO products (product_id, product_name, price) VALUES
(1, 'Laptop', 60000.00),
(2, 'Smartphone', 30000.00),
(3, 'Headphones', 3000.00),
(4, 'Keyboard', 2000.00),
(5, 'Mouse', 1000.00);

INSERT INTO orders (order_id, customer_id, order_date, amount) VALUES
(101, 1, '2026-01-10', 60000.00),
(102, 2, '2026-01-15', 30000.00),
(103, 1, '2026-02-05', 30000.00),
(104, 3, '2026-02-12', 55000.00),
(105, 4, '2026-03-01', 70000.00),
(106, 5, '2026-03-15', 25000.00),
(107, 2, '2026-04-05', 40000.00),
(108, 4, '2026-04-20', 35000.00),
(109, 6, '2026-05-10', 65000.00),
(110, 1, '2026-05-25', 20000.00);

INSERT INTO order_items (order_id, product_id, quantity) VALUES
(101, 1, 1),
(102, 2, 1),
(103, 2, 1),
(104, 1, 1),
(105, 1, 1),
(105, 3, 2),
(106, 3, 2),
(107, 2, 1),
(107, 4, 5),
(108, 3, 5),
(109, 1, 1),
(110, 2, 1);

-- 1. Total orders per customer
SELECT 
    c.customer_id,
    c.name,
    COUNT(o.order_id) AS total_orders
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name;


-- 2. Customers who never placed an order
SELECT 
    c.customer_id,
    c.name,
    c.city
FROM customers c
LEFT JOIN orders o ON c.customer_id = o.customer_id
WHERE o.order_id IS NULL;


-- 3. Highest selling product
SELECT 
    p.product_id,
    p.product_name,
    SUM(oi.quantity) AS total_quantity_sold
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
GROUP BY p.product_id, p.product_name
ORDER BY total_quantity_sold DESC
LIMIT 1;


-- 4. Monthly sales report
SELECT 
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(amount) AS total_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;


-- 5. Customers with total purchase > ₹50,000
SELECT 
    c.customer_id,
    c.name,
    SUM(o.amount) AS total_purchase
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id, c.name
HAVING SUM(o.amount) > 50000;


-- 6. Top 3 cities by revenue
SELECT 
    c.city,
    SUM(o.amount) AS total_revenue
FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.city
ORDER BY total_revenue DESC
LIMIT 3;