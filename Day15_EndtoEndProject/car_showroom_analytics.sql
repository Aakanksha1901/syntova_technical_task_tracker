USE car_showroom_db;

--  Total number of car records
SELECT COUNT(*) AS total_cars
FROM cars;

-- View sample records
SELECT *
FROM cars
LIMIT 10;

-- Find unique brands
SELECT DISTINCT brand FROM cars;

-- Total cars by brand
SELECT brand, COUNT(*) AS total_cars
FROM cars
GROUP BY brand
ORDER BY total_cars DESC;

-- Average price by brand
SELECT
    brand,
    COUNT(*) AS total_cars,
    ROUND(AVG(price), 2) AS average_price
FROM cars
GROUP BY brand
ORDER BY average_price DESC;

-- Most expensive cars
SELECT car_id, brand, model, `year`, price
FROM cars
ORDER BY price DESC
LIMIT 10;

-- Find cars priced above 15 lakh
SELECT * FROM cars WHERE price > 1500000;

-- Find cars manufactured after 2022
SELECT * FROM cars WHERE `year` > 2022;

-- Find petrol cars
SELECT * FROM cars WHERE fuel_type = 'Petrol';

-- Sort cars by price in descending order
SELECT * FROM cars ORDER BY price DESC;

-- Find cars priced between 10 lakh and 20 lakh
SELECT * FROM cars WHERE price BETWEEN 1000000 AND 2000000;

-- Find cars from selected brands
SELECT * FROM cars WHERE brand IN ('Toyota', 'Honda', 'Kia');

-- Find models starting with C
SELECT * FROM cars WHERE model LIKE 'C%';

-- Find average price by fuel type
SELECT fuel_type, AVG(price) AS average_price
FROM cars
GROUP BY fuel_type;

-- Find highest price by brand
SELECT brand, MAX(price) AS highest_price
FROM cars
GROUP BY brand;

-- Find brands with average mileage above 15
SELECT brand, AVG(mileage) AS average_mileage
FROM cars
GROUP BY brand
HAVING AVG(mileage) > 15;

-- Least expensive cars
SELECT car_id, brand, model, `year`, price
FROM cars
ORDER BY price ASC
LIMIT 10;


-- JOIN Queries

-- Create customers table for JOIN practice
CREATE TABLE IF NOT EXISTS customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(100),
    car_id INT
);

-- Insert sample customers
INSERT IGNORE INTO customers (customer_id, customer_name, car_id)
VALUES
(1, 'Amit', 1),
(2, 'Priya', 2),
(3, 'Rahul', 3),
(4, 'Sneha', 1),
(5, 'Neha', 8);

-- Display customers with their car details
SELECT cu.customer_name, c.brand, c.model
FROM customers cu
INNER JOIN cars c
ON cu.car_id = c.car_id;

-- Display all customers, including those without matching cars
SELECT cu.customer_name, c.brand, c.model
FROM customers cu
LEFT JOIN cars c
ON cu.car_id = c.car_id;

-- Display all cars, including cars without customers
SELECT c.brand, c.model, cu.customer_name
FROM cars c
LEFT JOIN customers cu
ON c.car_id = cu.car_id;

-- Find customers with cars priced above 15 lakh
SELECT cu.customer_name, c.brand, c.model, c.price
FROM customers cu
INNER JOIN cars c
ON cu.car_id = c.car_id
WHERE c.price > 1500000;


