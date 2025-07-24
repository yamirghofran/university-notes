---
title: Basic Mongodb
---

To start the MongoDB Shell, open your terminal and type: `mongosh`.

You can connect to a specific database using the `use` command. If the database doesn't exist, MongoDB will create it when you insert data.

`use mydatabase`

# Basic Commands

`show dbs`: Displays a list of all databases on the MongoDB server.
`show collections`: Lists all collections in the currently selected database.
`db`: Returns the name of the current database.
`db.<collection>`: Switches to the specified collection in the current database.
`help`: Provides help and documentation for MongoDB Shell commands.

## Creating a simple document and inserting it into a collection
`use mydatabase`
`db.mycollection.insertOne({ name: "John Doe", age: 30, city: "New York"})`


## Querying documents

### Find all documents in a collection
`db.mycollection.find()`

### Find documents that match a specified condition
`db.mycollection.find({ age: {$gt: 25 }})`

The `$gt` operator is used here to find documents where the 'age' field is greater than 25. MongoDB supports a variety of query operators for different conditions.

## Updating Documents

```SQL
db.mycollection.updateOne(
	{name: "John Doe"},
	{$set: { age: 31, city: "San Francisco" }}
);
```
We update the document with the name "John Doe". The `$set` operator is used to set the 'age' to 31 and 'city' to "San Francisco". If the document doesn't exist, it won't be updated.

## Updating Many
```SQL
db.mycollection.updateMany(
	{ age: { $lt: 30 }},
	{ $set: { status: "Young Adult"}}
)
```
Update all documents where the 'age' is less than 30. The `$set` operator is used to add a new field 'status' with the value "Young Adult" to each matching document.

## Set Operator
Set a specific field in a document.
```SQL
db.mycollection.updateOne(
	{name: "Alice"},
	{$set: {age: 25, city: "London"}}
)
```

## Inc Operator
Increment the value of a field in a document.
```SQL
db.mycollection.updateOne(
	{name:"Bob"},
	{$inc: {age: 1}}
)
```

## Push Operator
Add an element to an array field in a document.
```SQL
db.mycollection.updateOne(
	{ name: "Charlie"},
	{ $push: { hobbies: "Reading" }}
)
```

## Removing a Document
Delete a document
`db.mycollection.deleteOne({ name: "John Doe" })`
