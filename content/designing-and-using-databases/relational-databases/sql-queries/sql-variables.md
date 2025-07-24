---
title: SQL Variables
---

SQL variables are placeholders or containers in which you can store values temporarily to use later in your SQL queries. They help in writing more dynamic and reusable SQL code, especially in procedures and scripts.

Types of SQL variables:
- **User-defined variables**: These are variables that you define and use within a session.
- **System variables**: Predefined variables that control the operation of the MySQL server.
- **Session variables**: Specific to each session and only exist while the session is active.

# User-Defined Variables

```SQL
SET @actor_name = 'PENELOPE';
SELECT * FROM sakila.actor
WHERE first_name = @actor_name
```

## Using variables in calculations

```SQL
SET @rental_rate = (SELECT rental_rate FROM sakila.film WHERE title = 'ACADEMY DINOSAUR');

SELECT title, rental_rate
FROM sakila.film
WHERE rental_rate > @rental_rate;
```

# Session variables and statements
```SQL
SET @film_limit = 5;
PREPARE STMT FROM 'SELECT title, rental_rate
FROM sakila.film
LIMIT ?;';

EXECUTE STMT USING @film_limit;
```

# Dynamic SQL with Variables
```SQL
SET @dynamic_query = 'SELECT title FROM sakila.film WHERE rental_rate > ?;';

PREPARE stmt FROM @dynamic_query;
SET @rental_rate_limit = 3.99;
EXECUTE stmt USING @rental_rate_limit;
DEALLOCATE PREPARE stmt;
```