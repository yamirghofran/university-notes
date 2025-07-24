---
title: Choosing the Right Data Structrue
---

**Data Volume and Size**
- Consider the expected volume and size of your data.
- Some data structures are better suited for large datasets, while others excel in smaller ones.
**Access Patterns**
 - Analyze how data will be accessed.
 - Different data structures are optimized for different access patterns (e.g., random vs. sequential).
**Query Complexity**
- Determine the types of queries your database will frequently execute.
- Some data structures are better for range queries, point queries, or complex joins.
**Write Operations**
- Assess the frequency and nature of write operations.
- Certain data structures are well-suited for write-heavy workloads, while others favor read-heavy workloads.
**Scalability Requirements**
- Consider the scalability needs of your application.
- Choose data structures that can scale gracefully as data volumes grow.
**Memory vs. Disk Storage**
- Decide whether your data should primarily reside in memory or on disk.
- Some data structures are optimized for in-memory databases, while others work well for on-disk storage.
**Complexity and Maintenance**
- Evaluate the complexity of managing and maintaining your chosen data structure.
- Simpler data structures may be preferred for ease of maintenance.

```sql
WITH rental_revenue AS (
	SELECT f.film_id, f.rental_rate*COUNT(*) AS total_rental_revenue
	FROM film f
	JOIN inventory i ON i.film_id = f.film_id
	JOIN rental r ON r.inventory_id = i.inventory_id
	GROUP BY f.film_id
	),
	actor_revenue AS (
		SELECT a.actor_id, CONCAT(a.first_name, ' ', a.last_name) AS full_name, SUM(total_rental_revenue) as actor_rev, RANK () OVER (ORDER BY total_rental_revenue DESC) as actor_rank
		FROM actor a
		JOIN film_actor fa ON a.actor_id = fa.actor_id
		JOIN rental_revenue ON rental_revenue.film_id = fa.film_id
		GROUP BY a.actor_id
	)
	SELECT * FROM actor_revenue;
```



```sql
WITH VIP AS (
	SELECT c.customer_id, SUM(amount) AS total_spend
	FROM customer c
	JOIN payment p ON p.customer_id = c.customer_id
	GROUP BY c.customer_id
	HAVING SUM(amount) <= 100
)
WITH rented_times AS (
	SELECT f.film_id, COUNT(*) as rented_count
	FROM film f
	JOIN inventory i ON f.film_id = i.film_id
	JOIN rental r ON i.inventory_id = r.inventory_id
	GROUP BY f.film_id
) SELECT * from rented_times

```

```sql
our_movies AS (
	SELECT f.film_id, f.title, rt.rented_count, AVG(rt.rented_count) as total_average
	FROM film f
	JOIN rented_times rt ON rt.film_id = f.film_id
	GROUP BY AVG(rt.rented_count)
) SELECT * FROM our_movies;
```
SELECT AVG(rented_count) FROM rented_times;