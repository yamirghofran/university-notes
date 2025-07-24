---
title: SQL Commands
---

# Create a table
Syntax: `CREATE TABLE table_name (column1 datatype, column2 datatype,...);`
[Primary Keys](/designing-and-using-databases/relational-databases/primary-keys)
eg
```SQL
CREATE TABLE Users (
	UserID INT PRIMARY KEY,
	FirstName VARCHAR(50),
	LastName VARCHAR(50),
	Email VARCHAR(100) UNIQUE,
	Birthdate DATE
);
```

# Select from a table
`SELECT column1, column2 FROM table_name WHERE condition;`
eg
```SQL
SELECT FirstName, LastName, Email
FROM Users
WHERE Birthdate >= '1990-01-01';
```

# Insert into
`INSERT INTO table_name (column1, column2, ...) VALUES (value1, value2,...);`
eg
```SQL
INSERT INTO Users (FirstName, LastName, Email)
VALUES ('John', 'Doe', 'john.doe@email.com');
```

# Update table
`UPDATE table_name SET column1 = value1, column2 = value2 WHERE condition;`
eg
```SQL
UPDATE Users
SET LastName = 'Smith', Email = 'new.email@email.com'
WHERE UserID = 1;
```

# Delete table
`DELETE FROM table_name WHERE condition;`
eg
```SQL
DELETE FROM Users WHERE UserId = 1;
```

# Table with Reference
[Foreign Keys](/designing-and-using-databases/relational-databases/foreign-keys)
```SQL
	CREATE TABLE Orders (
	OrderID INT PRIMARY KEY,
	ProductID INT,
	-- Other order-related columns
	FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);
```

# Creating an [[Indexes | Index]]
```SQL
CREATE INDEX idx_LastName ON Employees(LastName);
```

# Creating a [[Transactions | Transaction]]
```SQL
BEGIN TRANSACTION;
-- SQL statements here (INSERT, UPDATE, DELETE, etc.)
COMMIT;
```

