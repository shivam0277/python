-- 1. SELECT — Fetching Data
-- The SELECT statement is used to choose which columns you want to retrieve from a table.

-- Syntax
-- SELECT column1, column2 FROM table_name;

-- Example
-- Table: employees

-- id	name	age	department
-- 1	John	28	HR
-- 2	Maya	32	IT
-- 3	Sam	25	Finance

-- Query
-- SELECT name, age FROM employees;

-- Output
-- John, 28
-- Maya, 32
-- Sam, 25

-- 2. WHERE — Filtering Rows
-- WHERE is used to extract only those rows that meet a condition.

-- Syntax
-- SELECT columns FROM table_name
-- WHERE condition;

-- Examples
-- ✔ Condition: equality
-- SELECT * FROM employees
-- WHERE department = 'IT';

-- ✔ Condition: comparison
-- SELECT name, age FROM employees
-- WHERE age > 30;

-- ✔ Condition: multiple filters (AND / OR)
-- SELECT * FROM employees
-- WHERE age < 30 AND department = 'Finance';

-- 1. AND / OR — Combine Conditions
-- AND → both conditions must be true

-- SELECT * FROM employees
-- WHERE department = 'IT' AND age > 25;
-- ✔ OR → at least one condition must be true

-- SELECT * FROM employees
-- WHERE department = 'HR' OR department = 'Finance';


-- 2. IN — Match Any Value in a List
-- IN is cleaner than multiple OR conditions.

-- SELECT * FROM employees
-- WHERE department IN ('HR', 'IT', 'Finance');


-- WHERE department = 'HR' OR department = 'IT' OR department = 'Finance';


-- 3. BETWEEN — Range Check
-- Inclusive → includes the start and end values.

-- SELECT * FROM products
-- WHERE price BETWEEN 100 AND 500;

-- SELECT * FROM orders
-- WHERE order_date BETWEEN '2025-01-01' AND '2025-01-31';


-- 4. LIKE — Pattern Matching
-- Used for searching text.

-- % → any number of characters

-- _ → 1 single character

-- Starts with 'A'

-- SELECT * FROM students
-- WHERE name LIKE 'A%';

-- ✔ Ends with 'n'
-- SELECT * FROM students
-- WHERE name LIKE '%n';


-- ✔ Contains “an”

-- SELECT * FROM students
-- WHERE name LIKE '%an%';


-- 3-letter names starting with S

-- SELECT * FROM students
-- WHERE name LIKE 'S__';


-- 1. Sort by One Column
-- Ascending (A → Z, 1 → 9)
-- SELECT * FROM employees
-- ORDER BY age ASC;

-- Descending (Z → A, 9 → 1)
-- SELECT * FROM employees
-- ORDER BY age DESC;

-- 2. Sort by Multiple Columns

-- Example:
-- Sort by department (A–Z), and within each department sort by salary (high to low):

-- SELECT * FROM employees
-- ORDER BY department ASC, salary DESC;

-- 3. Sorting Text Columns (Alphabetical)
-- A–Z
-- SELECT * FROM students
-- ORDER BY name;

-- Z–A
-- SELECT * FROM students
-- ORDER BY name DESC;

-- 4. Sorting with WHERE + ORDER BY
-- SELECT name, marks FROM students
-- WHERE marks > 70
-- ORDER BY marks DESC;


-- 1. Aggregate Functions (Basics)
-- These functions summarize data.

-- ✔ Count rows
-- SELECT COUNT(*) FROM employees;

-- ✔ Total (sum)
-- SELECT SUM(salary) FROM employees;

-- ✔ Average value
-- SELECT AVG(marks) FROM students;

-- ✔ Maximum value
-- SELECT MAX(price) FROM products;

-- ✔ Minimum value
-- SELECT MIN(price) FROM products;


-- 2. GROUP BY — Group the rows before applying aggregation

-- Example 1: Count employees in each department
-- SELECT department, COUNT(*) AS total_employees
-- FROM employees
-- GROUP BY department;

-- Example 2: Average salary by department
-- SELECT department, AVG(salary) AS avg_salary
-- FROM employees
-- GROUP BY department;

-- Example 3: Sum of sales by region
-- SELECT region, SUM(amount) AS total_sales
-- FROM sales
-- GROUP BY region;


-- 3. GROUP BY + ORDER BY
-- Example: highest total sales first.

-- SELECT region, SUM(amount) AS total_sales
-- FROM sales
-- GROUP BY region
-- ORDER BY total_sales DESC;


-- 1. Basic Example
-- Count employees in each department, but only show departments with more than 5 employees

-- SELECT department, COUNT(*) AS total_employees
-- FROM employees
-- GROUP BY department
-- HAVING COUNT(*) > 5;
-- You cannot use WHERE COUNT(*) > 5 (invalid) because COUNT() is created after grouping.

-- 2. GROUP BY with SUM + HAVING
-- Show products whose total sales exceed 10,000

-- SELECT product_id, SUM(amount) AS total_sales
-- FROM sales
-- GROUP BY product_id
-- HAVING SUM(amount) > 10000;


-- 3. GROUP BY with AVG + HAVING + ORDER BY
-- Show departments with average salary above 50,000 sorted high → low:

-- SELECT department, AVG(salary) AS avg_salary
-- FROM employees
-- GROUP BY department
-- HAVING AVG(salary) > 50000
-- ORDER BY avg_salary DESC;


-- 4. Using HAVING without GROUP BY (allowed!)
-- This works because HAVING can be used like WHERE for aggregates:

-- SELECT COUNT(*) AS total_orders
-- FROM orders
-- HAVING COUNT(*) > 1000;


-- 5. WHERE + GROUP BY + HAVING together
-- Example:
-- Find departments with total salary > 100,000 BUT only considering employees older than 30.

-- SELECT department, SUM(salary) AS total_salary
-- FROM employees
-- WHERE age > 30
-- GROUP BY department
-- HAVING SUM(salary) > 100000;


