USE ecommerce_db;

-- 1. Add index
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

-- 2. Analyze query using EXPLAIN
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 1;

-- 3. Add index for JOIN/filter optimization
CREATE INDEX idx_customers_city
ON customers(city);

-- Analyze optimized JOIN
EXPLAIN
SELECT c.name, o.order_date, o.amount
FROM customers c
JOIN orders o
ON c.customer_id = o.customer_id
WHERE c.city = 'Surat';

-- Check indexes
SHOW INDEX FROM orders;
SHOW INDEX FROM customers;