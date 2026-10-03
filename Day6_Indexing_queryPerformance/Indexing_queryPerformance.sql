USE shopping_db;

-- INDEXING
-- 1. INDEX FUNDAMENTALS
-- customers: customer_id, customer_name, city
-- products: product_id, product_name, category, price
-- orders: order_id, customer_id, product_id, order_date, quantity

SHOW INDEX FROM customers;

SHOW INDEX FROM products;

SHOW INDEX FROM orders;

-- 2. PRIMARY INDEX
-- Column: customers.customer_id
EXPLAIN
SELECT *
FROM customers
WHERE customer_id = 5;

-- Column: products.product_id
EXPLAIN
SELECT *
FROM products
WHERE product_id = 3;

-- Column: orders.order_id
EXPLAIN
SELECT *
FROM orders
WHERE order_id = 7;

-- 3. UNIQUE INDEX
-- Column: customers.customer_name
CREATE UNIQUE INDEX idx_unique_customer_name
ON customers(customer_name);

SHOW INDEX FROM customers;

DROP INDEX idx_unique_customer_name
ON customers;

-- 4. COMPOSITE INDEX
-- Columns: customers.city, customers.customer_name
CREATE INDEX idx_customer_city_name
ON customers(city, customer_name);

SELECT *
FROM customers
WHERE city = 'Mumbai'
AND customer_name = 'Aakanksha';

EXPLAIN
SELECT *
FROM customers
WHERE city = 'Mumbai'
AND customer_name = 'Aakanksha';


-- 5. COVERING INDEX
-- Columns: customers.city, customers.customer_name
EXPLAIN
SELECT customer_name, city
FROM customers
WHERE city = 'Mumbai';

-- 6. FULL-TEXT INDEX
-- Column: products.product_name
CREATE FULLTEXT INDEX idx_product_fulltext
ON products(product_name);

SELECT *
FROM products
WHERE MATCH(product_name)
AGAINST('Laptop');

SELECT *
FROM products
WHERE MATCH(product_name)
AGAINST('Mobile');

SHOW INDEX FROM products;

-- 7. INDEX SELECTIVITY
-- Column: customers.city
SELECT COUNT(*) AS total_customers
FROM customers;

SELECT COUNT(DISTINCT city) AS unique_cities
FROM customers;

SELECT
    COUNT(DISTINCT city) / COUNT(*) AS city_selectivity
FROM customers;

-- Column: customers.customer_id
SELECT
    COUNT(DISTINCT customer_id) / COUNT(*) AS customer_id_selectivity
FROM customers;

-- 8. INDEXING FOREIGN KEY COLUMNS
-- Column: orders.customer_id
CREATE INDEX idx_orders_customer_id
ON orders(customer_id);

-- Column: orders.product_id
CREATE INDEX idx_orders_product_id
ON orders(product_id);

SHOW INDEX FROM orders;

-- 9. COMPOSITE INDEX ON ORDERS
-- Columns: orders.customer_id, orders.order_date
CREATE INDEX idx_orders_customer_date
ON orders(customer_id, order_date);

SELECT *
FROM orders
WHERE customer_id = 5
AND order_date = '2024-02-01';

EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 5
AND order_date = '2024-02-01';

--  QUERY OPTIMIZATION
-- 10.EXPLAIN
-- Column: customers.city
EXPLAIN
SELECT *
FROM customers
WHERE city = 'Mumbai';

-- 11. EXPLAIN USING PRIMARY KEY
-- Column: customers.customer_id
EXPLAIN
SELECT *
FROM customers
WHERE customer_id = 5;

-- 12. EXPLAIN ANALYZE
-- Column: customers.customer_id
EXPLAIN ANALYZE
SELECT *
FROM customers
WHERE customer_id = 5;

-- 13. QUERY EXECUTION PLAN
-- Columns:
-- customers.customer_id
-- customers.customer_name
-- orders.customer_id
-- orders.order_date
-- orders.quantity
EXPLAIN
SELECT
    c.customer_name,
    o.order_date,
    o.quantity
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;

-- 14. FULL TABLE SCAN
-- Column: customers.customer_name
EXPLAIN
SELECT *
FROM customers
WHERE customer_name LIKE '%a%';

-- 15. INDEX SCAN / INDEX LOOKUP
-- Column: customers.customer_id
EXPLAIN
SELECT *
FROM customers
WHERE customer_id = 5;

-- 16. JOIN OPTIMIZATION
-- Columns:
-- customers.customer_id
-- customers.customer_name
-- orders.customer_id
-- orders.product_id
-- orders.quantity
-- products.product_id
-- products.product_name
SELECT
    c.customer_name,
    p.product_name,
    o.quantity
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id;

EXPLAIN
SELECT
    c.customer_name,
    p.product_name,
    o.quantity
FROM orders o
JOIN customers c
    ON o.customer_id = c.customer_id
JOIN products p
    ON o.product_id = p.product_id;

-- 17. SUBQUERY OPTIMIZATION
-- Columns:
-- customers.customer_id
-- customers.customer_name
-- orders.customer_id
SELECT customer_name
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);

EXPLAIN
SELECT customer_name
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);

-- 18. EXISTS
-- Columns:
-- customers.customer_id
-- customers.customer_name
-- orders.customer_id
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
WHERE EXISTS
(
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);

EXPLAIN
SELECT
    c.customer_id,
    c.customer_name
FROM customers c
WHERE EXISTS
(
    SELECT 1
    FROM orders o
    WHERE o.customer_id = c.customer_id
);


-- 19. SUBQUERY VS JOIN
-- Columns:
-- customers.customer_id
-- customers.customer_name
-- orders.customer_id

EXPLAIN
SELECT customer_name
FROM customers
WHERE customer_id IN
(
    SELECT customer_id
    FROM orders
);

EXPLAIN
SELECT DISTINCT
    c.customer_name
FROM customers c
JOIN orders o
    ON c.customer_id = o.customer_id;

-- 20. QUERY COST
-- Column: customers.customer_id
EXPLAIN
SELECT *
FROM customers
WHERE customer_id = 5;

-- Column: customers.city
EXPLAIN
SELECT *
FROM customers
WHERE city = 'Mumbai';

-- 21. INDEX OPTIMIZATION
-- Columns: orders.customer_id, orders.order_date
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 5
AND order_date = '2024-02-01';

-- 22. LEFTMOST PREFIX
-- Column: orders.customer_id
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 5;

-- Columns: orders.customer_id, orders.order_date
EXPLAIN
SELECT *
FROM orders
WHERE customer_id = 5
AND order_date = '2024-02-01';


-- Column: orders.order_date
EXPLAIN
SELECT *
FROM orders
WHERE order_date = '2024-02-01';

-- 23. FINAL INDEX CHECK
SHOW INDEX FROM customers;
SHOW INDEX FROM products;
SHOW INDEX FROM orders;