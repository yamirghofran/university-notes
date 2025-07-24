---
title: Normalization
---

Normalization is the process to eliminate data redundancy and enhance data integrity in the table. Normalization also helps to organize the data in the database. It is a multi-step process that sets the data into tabular form and removes the duplicated data from the relational tables.


# First Normal Form (1NF): Ensuring Atomicity and Uniqueness
A table is in 1NF if:
- Each column contains atomic (indivisible) values – meaning each field must contain only one value, not multiple values or lists.
- Each row must be unique – so there are no duplicate rows.
eg

| student_id | name     | courses             |
| ---------- | -------- | ------------------- |
| 1          | John Doe | Math, Science       |
| 2          | Jane Doe | History, Literature |
this table is not in 1NF because the `courses` column holds multiple values (Math, Science). To bring this table into 1NF, we need to split the multiple values into separate rows.


| student_id | name     | course     |
| ---------- | -------- | ---------- |
| 1          | John Doe | Math       |
| 1          | John Doe | Science    |
| 2          | Jane Doe | History    |
| 2          | Jane Doe | Literature |
now each field has atomic values and each row is unique – so the table is in 1NF.


# Second Normal Form (2NF): Removing Partial Dependencies
A table is in 2NF if:
- It is already in 1NF.
- Every non-key column is fully dependent on the entire [[Primary Keys |primary key]], meaning there are no partial dependencies.
- Partial dependency occurs when a non-key column depends only on part of a composite primary key (when the primary key consists of more than one column).
Suppose you have a `student_courses` table like this:

| student_id | course_id | student_name | course_name |
| ---------- | --------- | ------------ | ----------- |
| 1          | 101       | John Doe     | Math        |
| 1          | 102       | John Doe     | Science     |
Here, the `student_name` and `course_name` columns depend only on part of the composite key (either `student_id` or `course_id`), but not both. This violates 2NF.

### Students Table:
| student_id | student_name |
|------------|--------------|
| 1          | John Doe     |
| 2          | Jane Doe     |

### Courses Table:
| course_id | course_name |
|-----------|-------------|
| 101       | Math        |
| 102       | Science     |

### StudentCourses Table (Associating students with their courses):
| student_id | course_id |
|------------|-----------|
| 1          | 101       |
| 1          | 102       |
now, every non-key column is fully dependent on the entire primary key, and the table is in 2NF.


# Third Normal Form (3NF): Removing Transitive Dependencies
A table is in 3NF if:
- It is already in 2NF.
- There are no transitive dependencies, meaning no non-key column depends on another non-key column.

| student_id | student_name | department | department_location |
|------------|--------------|------------|---------------------|
| 1          | John Doe     | Math       | Building A          |
| 2          | Jane Doe     | History    | Building B          |
in this table, `department_location` depends on `department`, not directly on `student_id`. This is a transitive dependency and violates 3NF.

To remove the transitive dependency, split the table:

### Students Table:
| student_id | student_name | department |
|------------|--------------|------------|
| 1          | John Doe     | Math       |
| 2          | Jane Doe     | History    |

### Departments Table:
| department | department_location |
|------------|---------------------|
| Math       | Building A          |
| History    | Building B          |