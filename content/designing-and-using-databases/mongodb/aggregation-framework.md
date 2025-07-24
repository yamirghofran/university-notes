---
title: Aggregation Framework
---

The Aggregation Framework in MongoDB is a set of data processing stages that allows you to filter, reshape, and analyze data in a more sophisticated manner than simple queries. It is inspired by the concept of data pipelines, where documents flow through a sequence of processing stages.

**Pipeline**: A sequence of stages where each stage performs a specific operation on the data.

**Operators**: These are expressions used in various stages of the pipeline to perform specific operations like filtering, grouping, sorting, and more.

# Basic Aggregation Pipeline Operations

Find documents where the `age` is greater than 25.
```SQL
db.mycollection.aggregate([
	{$match: { age: { $gt: 25 }}}
]);
```

## Group
Group documents by 'city' and calculate the average age in each city.
```SQL
db.mycollection.aggregate([
	{$group: {_id: "$city", averageAge: {$avg: "$age"}}}
])
```

The `$group` stage separates documents into groups according to a "group key". The output is one document for each unique group key.

## Reshaping Documents
Project only the 'name' and 'age' fields, and add a new field `isAdult`.
```SQL
db.mycollection.aggregate([
	{$project: {name: 1, age: 1, isAdult: {$gte: ["$age", 18]}}}
]);
```

## Lookup
Performs a left outer join to a collection in the same database.

- `from`: The collection to use for lookup in the same database.
- `localField`: The field in the primary collection that can be used as a unique identifier in the `from` collection.
- `foreignField`: The field in the `from` collection that can be used as a unique identifier in the primary collection.
- `as`: The name of the new field that will contain the matching documents from the `from` collection.

```SQL
db.comments.aggregate([
  {
    $lookup: {
      from: "movies",
      localField: "movie_id",
      foreignField: "_id",
      as: "movie_details",
    },
  },
  {
    $limit: 1
  }
])
```

## Sorting
Sort documents by 'age' in descending order.
```SQL
db.mycollection.aggregate([
	{$sort: {age: -1}}
]);
```

## Limiting the Results
Limit the results set to the first 5 documents.
```SQL
db.mycollection.aggregate([
	{$limit: 5}
])
```
