USE shopping_db;
-- JOIN + WINDOW FUNCTIONS PRACTICE
-- Display customer name, product name, quantity, and total amount.
SELECT
    c.customer_name,
    p.product_name,
    o.quantity,
    p.price * o.quantity AS total_amount
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
INNER JOIN products p
    ON o.product_id = p.product_id;

-- Display all customers and their orders.
SELECT
    c.customer_name,
    o.order_id,
    o.order_date
FROM customers c
LEFT JOIN orders o
    ON c.customer_id = o.customer_id;

-- EMPLOYEES TABLE
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    manager_id INT
);

INSERT INTO employees (employee_id, employee_name, manager_id)
VALUES
(1, 'Aakanksha', NULL),
(2, 'Rahul', 1),
(3, 'Sneha', 1),
(4, 'Amit', 2),
(5, 'Priya', 2);

-- Display employees and their managers.
SELECT
    e.employee_name AS employee,
    m.employee_name AS manager
FROM employees e
LEFT JOIN employees m
    ON e.manager_id = m.employee_id;

-- Display total orders placed by each customer.
SELECT
    c.customer_name,
    COUNT(o.order_id) AS total_orders
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
GROUP BY c.customer_name;

-- Display customer name and total spending.
SELECT
    c.customer_name,
    SUM(p.price * o.quantity) AS total_spending
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id
INNER JOIN products p
    ON o.product_id = p.product_id
GROUP BY c.customer_name;

-- Display every order with the total number of orders.
SELECT
    o.order_id,
    c.customer_name,
    o.quantity,
    COUNT(*) OVER () AS total_orders
FROM orders o
INNER JOIN customers c
    ON o.customer_id = c.customer_id;

-- Display each customer's total quantity using a window function.
SELECT
    c.customer_name,
    o.order_id,
    o.quantity,
    SUM(o.quantity) OVER (
        PARTITION BY c.customer_id
    ) AS customer_total_quantity
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

-- Number all orders according to order date.
SELECT
    c.customer_name,
    o.order_id,
    o.order_date,
    ROW_NUMBER() OVER (
        ORDER BY o.order_date
    ) AS order_number
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

-- Number each customer's orders separately.
SELECT
    c.customer_name,
    o.order_id,
    o.order_date,
    ROW_NUMBER() OVER (
        PARTITION BY c.customer_id
        ORDER BY o.order_date
    ) AS customer_order_number
FROM customers c
INNER JOIN orders o
    ON c.customer_id = o.customer_id;

-- Rank products according to price.
SELECT
    p.product_name,
    p.category,
    p.price,
    RANK() OVER (
        ORDER BY p.price DESC
    ) AS price_rank
FROM products p;

-- Display product rank within each category.
SELECT
    p.product_name,
    p.category,
    p.price,
    RANK() OVER (
        PARTITION BY p.category
        ORDER BY p.price DESC
    ) AS category_rank
FROM products p;

-- Display the previous order quantity.
SELECT
    order_id,
    order_date,
    quantity,
    LAG(quantity) OVER (
        ORDER BY order_date
    ) AS previous_quantity
FROM orders;

-- Display the next order quantity.
SELECT
    order_id,
    order_date,
    quantity,
    LEAD(quantity) OVER (
        ORDER BY order_date
    ) AS next_quantity
FROM orders;

-- Display the first order quantity on every row.
SELECT
    order_id,
    order_date,
    quantity,
    FIRST_VALUE(quantity) OVER (
        ORDER BY order_date
    ) AS first_quantity
FROM orders;

-- Calculate the running total of quantity.
SELECT
    order_id,
    order_date,
    quantity,
    SUM(quantity) OVER (
        ORDER BY order_date
    ) AS running_total
FROM orders;

-- Calculate the average quantity across all orders.
SELECT
    order_id,
    quantity,
    AVG(quantity) OVER () AS average_quantity
FROM orders;

-- Calculate a 3-order moving average.
SELECT
    order_id,
    order_date,
    quantity,
    AVG(quantity) OVER (
        ORDER BY order_date
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS moving_average
FROM orders;

-- Divide products into 3 price groups.
SELECT
    product_name,
    price,
    NTILE(3) OVER (
        ORDER BY price DESC
    ) AS price_group
FROM products;