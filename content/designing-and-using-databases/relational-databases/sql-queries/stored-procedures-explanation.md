---
title: Stored Procedures Explanation
---

A stored procedure is a precompiled collection of SQL statements and optional control-flow logic that is stored in the database. It can be executed with a single call and allows you to encapsulate complex logic and reuse it across different applications or queries.

In other words, a stored procedure is a block of SQL code that can include variable declarations, loops, conditionals, and even interactions with the data (like SELECT, INSERT, UPDATE, and DELETE statements). The procedure is stored on the database server and can be executed repeatedly without having to rewrite the SQL code each time.

# Structure

A stored procedure typically has the following structure:
- **Parameters**: You can pass parameters (inputs) to the procedure and get outputs back.
- **Logic**: The procedure can contain conditional statements (like IF), loops (like WHILE), and SQL queries.
- **Return Values**: Procedures can return values or a dataset (result set) after execution.

```SQL
DELIMETER //
CREATE PROCEDURE GetFilmsByRentalRate(IN rate_threshold DECIMAL(4,2))
BEGIN
	SELECT title, rental_rate
	FROM sakila.film
	WHERE rental_rate > rate_threshold;
END //
DELIMETER;
```

```SQL
DELIMETER //
CREATE PROCEDURE get_frequent_rentals(IN num_rentals INT)
BEGIN
	DECLARE rental_count INT;
	SELECT COUNT(*)
	INTO rental_count
	FROM sakila.rental
	WHERE film_id = num_rentals;
	SELECT film.title, rental_count
	FROM sakila.film
	WHERE film.film_id = num_rentals;
END //
DELIMETER;
```

