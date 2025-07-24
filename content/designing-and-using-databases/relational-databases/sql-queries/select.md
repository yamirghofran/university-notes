---
title: SELECT
---

To retrieve data from a database table.

```SQL
SELECT column1, column2, (*) FROM table_name;

SELECT product_name AS "Product Name", price AS "Price" FROM products;
```

Arithmetic Operations
```SQL
SELECT product_name, price, quantity, price*quantity AS total_price FROM products;
```

Functions:
Concatenate first_name and last_name with a space in between:
```SQL
SELECT CONCAT(first_name, ' ',last_name) AS full_name FROM employees;
```

**Using a CASE**:
```SQL
SELECT 
	first_name,
	last_name,
	salary,
	CASE 
		WHEN salary >= 60000 THEN 'High'
		WHEN salary >= 40000 THEN 'Medium'
		ELSE 'Low'
	END AS salary_group
FROM employees;
```

**Using JOINS**
Retrieve customer information and their associated orders
```SQL
SELECT customers.customer_name, orders.order_date 
FROM customers
INNER JOIN orders ON customers.customer_id = orders.customer_id;
```

**GROUP by Aggregate Functions**
Count the number of orders for each product category
```SQL
SELECT product_category, COUNT(*) AS order_count
FROM products
INNER JOIN order_details ON products.product_id = order_details.product_id
GROUP BY product_category
```

**USING Subqueries**
Find the employees who are managers
```SQL
SELECT first_name, last_name
FROM employees
WHERE employee_id IN (
SELECT manager_id
FROM employees
)
```

## The FROM Clause
```SQL
SELECT column1, column2
FROM table_name;
```

Multiple tables:
```SQL
SELECT orders.order_id, orders.order_date, customers.customer_name
FROM orders
INNER JOIN customers ON orders.customer_id = customers.customer_id;
```

Using table aliases:
```SQL
SELECT column1, column2
FROM table_name AS alias;
```

## The WHERE Clause
```SQL
SELECT column1, column2
FROM table_name
WHERE condition;
```
uses comparison operators to create condition. (=,>,<,>=,<=,<>)
**Operators**
- AND, OR, NOT can be used to combine multiple conditions.
- BETWEEN operator is used to specify a range of values.
- LIKE operator for pattern matching, including wildcard characters (% and `_`)
- The IS NULL operator checks for NULL values in a column.
- The IS NOT NULL operator checks for non-NULL values.
```SQL
SELECT * FROM customers
WHERE last_name = 'Smith';

SELECT * FROM products
WHERE price <> 50;

SELECT * FROM orders
WHERE order_date BETWEEN '2023-01-01' AND '2023-06-30';

SELECT * FROM products
WHERE product_name LIKE '%apple%';

SELECT * FROM employees
WHERE last_name LIKE 'Sm%'

SELECT * FROM products
WHERE price < 50 and stock_quantity > 10;
SELECT * FROM customers
WHERE state NOT IN ('New York', 'California');
```

**JOIN Operations**
```SQL
SELECT columns
FROM table1
JOIN table2 ON table1.column_name = table2.column_name;
```

**The GROUP BY Clause**
```SQL
SELECT column1, aggregate_function(column2)
FROM table_name
GROUP BY column1
```

**Aggregate Functions**
Aggregate functions (e.g. COUNT, SUM, AVG, MAX, MIN) are used within the SELECT statement to summarize data.

Each function serves a different purpose, such as counting rows or calculating the average of numeric values.

**The HAVING Clause**
The HAVING clause allows you to filter groups based on aggregate function results.
It's used to set conditions for the grouped data, similar to WHERE clause