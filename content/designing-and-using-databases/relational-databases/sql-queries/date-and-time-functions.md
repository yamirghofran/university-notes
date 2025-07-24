---
title: Date and Time Functions
---

- `NOW()`: Retrieves the current date and time.
- `DATE_ADD()`: Adds a specific amount of time to a date.
- `DATEDIFF()`: Calculates the difference between two dates or times.
- `DATEPART()`: Extracts a specific part (e.g year, month, day) from a date.

**NOW()**

```SQL
SELECT NOW() AS current_datetime;
```

## DATE_ADD()
```SQL
SELECT rental_id, rental_date, DATE_ADD(rental_date, INTERVAL 7 DAY) AS extended_return_date
FROM rental
LIMIT 5;
```

## DATEDIFF()
```SQL
SELECT customer_id, MAX(rental_date) AS last_rental, DATEDIFF(NOW(), MAX(rental_date)) AS days_since_last_rental
FROM rental
GROUP BY customer_id
ORDER BY days_since_last_rental ASC
LIMIT 5;
```

## EXTRACT()
```SQL
SELECT rental_id, rental_date, EXTRACT(MONTH FROM rental_date) AS rental_month, EXTRACT(YEAR FROM rental_date) AS rental_year
FROM rental
ORDER BY rental_date DESC
LIMIT 5;
```

# Formatting dates and timezones
`FORMAT()`: This function allows you to format a date or time into a specific string representation, making it more human-readable.
`SWITHOFFSET()`: Adjusts the time zone offset for a given datetime value.