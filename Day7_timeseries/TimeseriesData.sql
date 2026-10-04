-- TIME SERIES 
CREATE DATABASE time_series_practice;
USE time_series_practice;

CREATE TABLE orders (
    order_id INT,
    customer_id INT,
    product VARCHAR(50),
    category VARCHAR(50),
    order_date DATE,
    delivery_date DATE,
    quantity INT,
    amount DECIMAL(10,2)
);


INSERT INTO orders VALUES
(1,  101, 'Laptop',   'Electronics', '2024-01-05', '2024-01-08', 1, 50000),
(2,  102, 'Mouse',    'Electronics', '2024-02-10', '2024-02-12', 3, 3000),
(3,  103, 'Keyboard', 'Electronics', '2024-03-15', '2024-03-18', 2, 4000),
(4,  101, 'Monitor',  'Electronics', '2024-04-20', '2024-04-25', 1, 30000),
(5,  104, 'Laptop',   'Electronics', '2024-05-08', '2024-05-12', 1, 55000),
(6,  105, 'Mouse',    'Electronics', '2025-01-07', '2025-01-09', 5, 5000),
(7,  102, 'Laptop',   'Electronics', '2025-02-14', '2025-02-18', 2, 110000),
(8,  106, 'Keyboard', 'Electronics', '2025-03-11', '2025-03-14', 3, 6000),
(9,  103, 'Monitor',  'Electronics', '2025-04-22', '2025-04-27', 2, 60000),
(10, 107, 'Laptop',   'Electronics', '2025-05-17', '2025-05-20', 1, 60000),
(11, 107, 'Keyboard', 'Electronics', '2026-04-12', '2026-04-15', 5, 10000),
(12, 103, 'Laptop',   'Electronics', '2026-05-20', '2026-05-24', 1, 65000),
(13, 101, 'Monitor',  'Electronics', '2026-06-06', '2026-06-10', 2, 70000),
(14, 104, 'Mouse',    'Electronics', '2026-07-18', '2026-07-20', 6, 6000),
(15, 105, 'Laptop',   'Electronics', '2026-08-25', '2026-08-29', 2, 140000);

-- Display year from date
SELECT
    order_date,
    YEAR(order_date) AS order_year
FROM orders;

-- Display month from date
SELECT
    order_date,
    MONTH(order_date) AS order_month
FROM orders;

--  Display quarter from date
SELECT
    order_date,
    QUARTER(order_date) AS quarter
FROM orders;

--  Find number of orders per day
SELECT
    order_date,
    COUNT(*) AS total_orders
FROM orders
GROUP BY order_date
ORDER BY order_date;

-- Find sales per month
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(amount) AS monthly_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- Find sales per year
SELECT
    YEAR(order_date) AS year,
    SUM(amount) AS yearly_sales
FROM orders
GROUP BY YEAR(order_date)
ORDER BY year;

-- Find sales per quarter
SELECT
    YEAR(order_date) AS year,
    QUARTER(order_date) AS quarter,
    SUM(amount) AS quarterly_sales
FROM orders
GROUP BY YEAR(order_date), QUARTER(order_date)
ORDER BY year, quarter;

-- DATE FILTERING
-- Sales between two dates
SELECT *
FROM orders
WHERE order_date BETWEEN '2025-01-01' AND '2025-06-30';

-- Orders from a particular month
SELECT *
FROM orders
WHERE YEAR(order_date) = 2025
AND MONTH(order_date) = 3;

--  Orders from a particular year
SELECT *
FROM orders
WHERE YEAR(order_date) = 2025;

-- Last 7 days
SELECT *
FROM orders
WHERE order_date >= '2026-08-31' - INTERVAL 7 DAY;

--  Last 30 days
SELECT *
FROM orders
WHERE order_date >= '2026-08-31' - INTERVAL 30 DAY;

--  Current month
SELECT *
FROM orders
WHERE YEAR(order_date) = YEAR(CURRENT_DATE)
AND MONTH(order_date) = MONTH(CURRENT_DATE);

--  Previous month
SELECT *
FROM orders
WHERE YEAR(order_date) = YEAR(CURRENT_DATE - INTERVAL 1 MONTH)
AND MONTH(order_date) = MONTH(CURRENT_DATE - INTERVAL 1 MONTH);

-- DATE AGGREGATION
-- Daily total sales
SELECT
    order_date,
    SUM(amount) AS daily_sales
FROM orders
GROUP BY order_date
ORDER BY order_date;

--  Monthly total sales
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(amount) AS monthly_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

--  Average monthly sales
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    AVG(monthly_sales) AS average_monthly_sales
FROM monthly_sales;

--  Number of orders per month
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    COUNT(*) AS total_orders
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

--  Highest sales month
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT *
FROM monthly_sales
ORDER BY monthly_sales DESC
LIMIT 1;

--  Lowest sales month
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT *
FROM monthly_sales
ORDER BY monthly_sales ASC
LIMIT 1;

--  DATE DIFFERENCE
-- Days between order and delivery
SELECT
    order_id,
    order_date,
    delivery_date,
    DATEDIFF(delivery_date, order_date) AS delivery_days
FROM orders;


--  Days between two transactions
WITH transaction_dates AS (
    SELECT
        order_id,
        order_date,
        LAG(order_date) OVER (
            ORDER BY order_date
        ) AS previous_order_date
    FROM orders
)
SELECT
    order_id,
    order_date,
    previous_order_date,
    DATEDIFF(order_date, previous_order_date) AS days_between_orders
FROM transaction_dates;

--  Find orders taking more than 3 days
SELECT
    order_id,
    order_date,
    delivery_date,
    DATEDIFF(delivery_date, order_date) AS delivery_days
FROM orders
WHERE DATEDIFF(delivery_date, order_date) > 3;

--  Add days to a date
SELECT
    order_date,
    DATE_ADD(order_date, INTERVAL 10 DAY) AS date_after_10_days
FROM orders;

-- Subtract days from a date
SELECT
    order_date,
    DATE_SUB(order_date, INTERVAL 10 DAY) AS date_before_10_days
FROM orders;

-- TIME-SERIES COMPARISON
-- Previous day's sales
WITH daily_sales AS (
    SELECT
        order_date,
        SUM(amount) AS daily_sales
    FROM orders
    GROUP BY order_date
)
SELECT
    order_date,
    daily_sales,
    LAG(daily_sales) OVER (
        ORDER BY order_date
    ) AS previous_day_sales
FROM daily_sales;

-- Previous month's sales
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    monthly_sales,
    LAG(monthly_sales) OVER (
        ORDER BY year, month
    ) AS previous_month_sales
FROM monthly_sales;

--  MOM ANALYSIS
--  Monthly sales
SELECT
    YEAR(order_date) AS year,
    MONTH(order_date) AS month,
    SUM(amount) AS monthly_sales
FROM orders
GROUP BY YEAR(order_date), MONTH(order_date)
ORDER BY year, month;

-- Previous month's sales
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    monthly_sales,
    LAG(monthly_sales) OVER (
        ORDER BY year, month
    ) AS previous_month_sales
FROM monthly_sales;

--  Monthly sales difference
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
),
comparison AS (
    SELECT
        *,
        LAG(monthly_sales) OVER (
            ORDER BY year, month
        ) AS previous_sales
    FROM monthly_sales
)
SELECT
    year,
    month,
    monthly_sales,
    previous_sales,
    monthly_sales - previous_sales AS sales_difference
FROM comparison;

--  Find months where sales increased
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
),
comparison AS (
    SELECT
        *,
        LAG(monthly_sales) OVER (
            ORDER BY year, month
        ) AS previous_sales
    FROM monthly_sales
)
SELECT *
FROM comparison
WHERE monthly_sales > previous_sales;

-- Find months where sales decreased
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
),
comparison AS (
    SELECT
        *,
        LAG(monthly_sales) OVER (
            ORDER BY year, month
        ) AS previous_sales
    FROM monthly_sales
)
SELECT *
FROM comparison
WHERE monthly_sales < previous_sales;

--  RUNNING TOTAL
--  Running sales total
WITH daily_sales AS (
    SELECT
        order_date,
        SUM(amount) AS daily_sales
    FROM orders
    GROUP BY order_date
)
SELECT
    order_date,
    daily_sales,
    SUM(daily_sales) OVER (
        ORDER BY order_date
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS running_sales
FROM daily_sales;

--  Cumulative revenue
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS revenue
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    revenue,
    SUM(revenue) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_revenue
FROM monthly_sales;

--  Cumulative number of orders
WITH monthly_orders AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        COUNT(*) AS total_orders
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    total_orders,
    SUM(total_orders) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_orders
FROM monthly_orders;


--  Cumulative quantity sold
WITH monthly_quantity AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(quantity) AS total_quantity
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
)
SELECT
    year,
    month,
    total_quantity,
    SUM(total_quantity) OVER (
        ORDER BY year, month
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_quantity
FROM monthly_quantity;


--  MOVING AVERAGE
-- 7-day moving average
WITH daily_sales AS (
    SELECT
        order_date,
        SUM(amount) AS daily_sales
    FROM orders
    GROUP BY order_date
)
SELECT
    order_date,
    daily_sales,
    AVG(daily_sales) OVER (
        ORDER BY order_date
        ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
    ) AS seven_day_average
FROM daily_sales;

-- 30-day moving average
WITH daily_sales AS (
    SELECT
        order_date,
        SUM(amount) AS daily_sales
    FROM orders
    GROUP BY order_date
)
SELECT
    order_date,
    daily_sales,
    AVG(daily_sales) OVER (
        ORDER BY order_date
        ROWS BETWEEN 29 PRECEDING AND CURRENT ROW
    ) AS thirty_day_average
FROM daily_sales;

-- YoY difference
WITH monthly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        SUM(amount) AS monthly_sales
    FROM orders
    GROUP BY YEAR(order_date), MONTH(order_date)
),
comparison AS (
    SELECT
        *,
        LAG(monthly_sales, 12) OVER (
            ORDER BY year, month
        ) AS previous_year_sales
    FROM monthly_sales
)
SELECT
    year,
    month,
    monthly_sales,
    previous_year_sales,
    monthly_sales - previous_year_sales AS yoy_difference
FROM comparison;

--  Find years with increased sales
WITH yearly_sales AS (
    SELECT
        YEAR(order_date) AS year,
        SUM(amount) AS yearly_sales
    FROM orders
    GROUP BY YEAR(order_date)
),
comparison AS (
    SELECT
        *,
        LAG(yearly_sales) OVER (
            ORDER BY year
        ) AS previous_year_sales
    FROM yearly_sales
)
SELECT
    year,
    yearly_sales,
    previous_year_sales,
    CASE
        WHEN yearly_sales > previous_year_sales THEN 'Increased'
        WHEN yearly_sales < previous_year_sales THEN 'Decreased'
        ELSE 'No Change'
    END AS trend
FROM comparison;

-- Rank products by monthly sales
WITH monthly_product_sales AS (
    SELECT
        YEAR(order_date) AS year,
        MONTH(order_date) AS month,
        product,
        SUM(amount) AS total_sales
    FROM orders
    GROUP BY
        YEAR(order_date),
        MONTH(order_date),
        product
)
SELECT
    year,
    month,
    product,
    total_sales,
    RANK() OVER (
        PARTITION BY year, month
        ORDER BY total_sales DESC
    ) AS product_rank
FROM monthly_product_sales;
