-- SHOPPING DATABASE
-- Create Database
CREATE DATABASE shopping_db;

-- Use Database
USE shopping_db;

--   CUSTOMERS TABLE
CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(50) NOT NULL,
    city VARCHAR(50)
);

-- Insert Customers
INSERT INTO customers (customer_name, city)
VALUES
('Aakanksha', 'Mumbai'),
('Rahul', 'Pune'),
('Sneha', 'Delhi'),
('Amit', 'Mumbai'),
('Priya', 'Pune'),
('Rohan', 'Nashik'),
('Neha', 'Mumbai'),
('Raj', 'Kolhapur'),
('Pooja', 'Delhi'),
('Karan', 'Pune');

-- PRODUCTS TABLE
CREATE TABLE products (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(50) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- Insert Products
INSERT INTO products (product_name, category, price)
VALUES
('Laptop', 'Electronics', 60000),
('Mobile', 'Electronics', 30000),
('Headphones', 'Electronics', 5000),
('T-Shirt', 'Clothing', 1200),
('Jeans', 'Clothing', 2500),
('Shoes', 'Footwear', 4000),
('Watch', 'Accessories', 7000),
('Bag', 'Accessories', 3000),
('Keyboard', 'Electronics', 2000),
('Mouse', 'Electronics', 1000);


--  ORDERS TABLE
CREATE TABLE orders (
    order_id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    product_id INT,
    order_date DATE,
    quantity INT,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

-- Insert Orders
INSERT INTO orders
(customer_id, product_id, order_date, quantity)
VALUES
(1, 1, '2024-01-10', 1),
(2, 2, '2024-01-12', 2),
(3, 4, '2024-01-15', 3),
(4, 3, '2024-01-20', 1),
(5, 5, '2024-02-01', 2),
(6, 6, '2024-02-05', 1),
(7, 7, '2024-02-10', 1),
(8, 8, '2024-02-15', 2),
(9, 9, '2024-03-01', 1),
(10, 10, '2024-03-05', 3);

-- Check data
SELECT * FROM customers;
SELECT * FROM products;
SELECT * FROM orders;

--  ALTER TABLE
--  Add a brand column to products.
ALTER TABLE products
ADD brand VARCHAR(50);

-- Remove the brand column.
ALTER TABLE products
DROP COLUMN brand;

-- SELECT
--  Display all customers.
SELECT *FROM customers;

--  Display all products.
SELECT *FROM products;

--  Display all orders.
SELECT * FROM orders;

-- Display customer name and city.
SELECT 
	customer_name AS NAME, 
    city
FROM customers;

-- DISTINCT
--  Display unique cities.
SELECT DISTINCT city FROM customers;

-- Display unique product categories.
SELECT DISTINCT category FROM products;

--  WHERE
-- Find customers from Mumbai.
SELECT * FROM customers
WHERE city = 'Mumbai';

--  Find products below 5,000.
SELECT * FROM products
WHERE price < 5000;

--  AND / OR / NOT
--  Find Electronics products above 10,000.
SELECT * FROM products
WHERE category = 'Electronics'
AND price > 10000;

-- Find customers from Mumbai or Pune.
SELECT * FROM customers
WHERE city = 'Mumbai'
OR city = 'Pune';

--  Find customers who are not from Mumbai.
SELECT * FROM customers
WHERE NOT city = 'Mumbai';

-- IN
--  Find customers from Mumbai, Pune or Delhi.
SELECT * FROM customers
WHERE city IN ('Mumbai', 'Pune', 'Delhi');

-- Find Electronics or Clothing products.
SELECT * FROM products
WHERE category IN ('Electronics', 'Clothing');

-- BETWEEN
--  Find products priced between 2,000 and 10,000.
SELECT * FROM products
WHERE price BETWEEN 2000 AND 10000;

--  Find orders between two dates.
SELECT * FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-02-28';

-- LIKE
-- Find customers whose name starts with A.
SELECT * FROM customers
WHERE customer_name LIKE 'A%';

--  Find customers whose name ends with a.
SELECT * FROM customers
WHERE customer_name LIKE '%a';

-- Find products whose name contains 'o'.
SELECT * FROM products
WHERE product_name LIKE '%o%';

-- Find products whose name starts with M.
SELECT * FROM products
WHERE product_name LIKE 'M%';

--  IS NULL / IS NOT NULL
--  Find customers whose email is NULL.
SELECT * FROM orders
WHERE order_date IS NULL;

--  Find customers whose email is NOT NULL.
SELECT * FROM products
WHERE product_id IS NOT NULL;

--  ORDER BY
-- Display products from lowest to highest price.
SELECT * FROM products
ORDER BY price ASC;

--  Display products from highest to lowest price.
SELECT * FROM products
ORDER BY price DESC;

--  Display customers alphabetically.
SELECT * FROM customers
ORDER BY customer_name ASC;

--  LIMIT
-- Display 3 most expensive products.
SELECT * FROM products
ORDER BY price DESC
LIMIT 3;

--  Display 3 cheapest products.
SELECT * FROM products
ORDER BY price ASC
LIMIT 3;

--  ALIAS
--  Display customer_name as Name.
SELECT customer_name AS Name
FROM customers;

--  UPDATE
-- Change Aakanksha's city to Pune.
UPDATE customers
SET city = 'Pune'
WHERE customer_name = 'Aakanksha';

--  Change Laptop price to 65,000.
UPDATE products
SET price = 65000
WHERE product_name = 'Laptop';

-- DELETE
-- Delete order number 5.
DELETE FROM orders
WHERE order_id = 5;


-- AGGREGATE FUNCTIONS
--  Count total customers.
SELECT COUNT(*) AS total_customers
FROM customers;

--  Count total products.
SELECT COUNT(*) AS total_products
FROM products;

-- Count total orders.
SELECT COUNT(*) AS total_orders
FROM orders;

--  Find total quantity ordered.
SELECT SUM(quantity) AS total_quantity
FROM orders;

--  Find average product price.
SELECT AVG(price) AS average_price
FROM products;

--  Find cheapest product price.
SELECT MIN(price) AS minimum_price
FROM products;

-- Find highest product price.
SELECT MAX(price) AS maximum_price
FROM products;

--  GROUP BY
--  Count customers according to city.
SELECT city,
       COUNT(*) AS total_customers
FROM customers
GROUP BY city;

--  Count products according to category.
SELECT category,
       COUNT(*) AS total_products
FROM products
GROUP BY category;

--  Find average price of each category.
SELECT category,
       AVG(price) AS average_price
FROM products
GROUP BY category;

--  Find highest price in each category.
SELECT category,
       MAX(price) AS highest_price
FROM products
GROUP BY category;

--  Find lowest price in each category.
SELECT category,
       MIN(price) AS lowest_price
FROM products
GROUP BY category;


--  Find total quantity ordered for each product.
SELECT product_id,
       SUM(quantity) AS total_quantity
FROM orders
GROUP BY product_id;

--  Find number of orders placed by each customer.
SELECT customer_id,
       COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id;

--  HAVING
--  Find cities having more than 2 customers.
SELECT city,
       COUNT(*) AS total_customers
FROM customers
GROUP BY city
HAVING COUNT(*) > 2;

-- Find categories having more than 2 products.
SELECT category,
       COUNT(*) AS total_products
FROM products
GROUP BY category
HAVING COUNT(*) > 2;


