CREATE DATABASE bank;

USE bank;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY,
    name VARCHAR(100),
    balance DECIMAL(10,2)
);

INSERT INTO accounts (account_id, name, balance)
VALUES
(1, 'Dhvani', 10000.00),
(2, 'Rahul', 5000.00);

START TRANSACTION;

INSERT INTO accounts (account_id, name, balance)
VALUES (3, 'Priya', 7000.00);

ROLLBACK;

START TRANSACTION;

INSERT INTO accounts (account_id, name, balance)
VALUES (3, 'Priya', 7000.00);

COMMIT;

START TRANSACTION;

UPDATE accounts
SET balance = balance - 2000
WHERE account_id = 1;

UPDATE accounts
SET balance = balance + 2000
WHERE account_id = 2;

COMMIT;

SELECT * FROM accounts;