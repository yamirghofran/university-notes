---
title: Common Table Expressions
---

CTE is a named temporary result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement.

Provides readability and reusability.

Starts with WITH keyword and is defined within a query.

```SQL
WITH TopFilms AS (
	SELECT
		title, rental_rate,
		RANK() OVER (ORDER BY rental_rate DESC) AS film_rank
	FROM film
)
SELECT
	title, rental_date, film_rank
FROM TopFilms
WHERE film_rank <= 5;
```

## Benefits of CTE
- Improve query readability and maintainability.
- Encapsulate complex logic in a single location.
- Avoid duplicating subqueries within a query.
