---
title: Window Functions
---

Window functions perform calculations across a set of table rows related to the current row.
They allow you to compare values in the current row with others in the result set.
Useful for running totals, rankings, and moving averages.

**Common Window Functions**
`ROW_NUMBER()`: Assigns a unique number to each row within a result set.
`RANK()`: Assigns a rank to each row based on a specified column.
`SUM()`: Calculates a running sum.
`LAG()` and `LEAD()`: Access data from preceding and following row.

## ROW_NUMBER()
```SQL
SELECT 
	ROW_NUMBER() OVER (ORDER BY rental_rate DESC) AS row_num,
	title,
	rental_rate
FROM film;
```

## RANK()
```SQL
SELECT 
	RANK() OVER (ORDER BY rental_rate DESC) AS row_num,
	title,
	rental_rate
FROM film;
```

## Running Sum
```SQL
SELECT 
	customer_id,
	payment_date,
	amount,
	SUM(amount) OVER (ORDER BY payment_date) AS running_total
FROM payment
WHERE customer_id = 1;
```

## Lead
```SQL
SELECT
	title,
	rental_duration,
	LEAD(rental_duration) OVER (ORDER BY rental_duration) AS next_rental_duration
FROM film;
```

## Lag
```SQL
SELECT
	title,
	rental_duration,
	LAG(rental_duration) OVER (ORDER BY rental_duration) AS previous_rental_duration
FROM film;
```