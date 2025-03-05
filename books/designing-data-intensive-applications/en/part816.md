## Reduce-Side Joins and Grouping 
We discussed joins in [Chapter 2](ch02.html#ch_datamodels) in the context of data models and query languages, but we
have not delved into how joins are actually implemented. It is time that we pick up that thread
again. 
In many datasets it is common for one record to have an association with another record: a foreign
key in a relational model, a document reference in a document model, or an edge in a graph
model. A join is necessary whenever you have some code that needs to access records on both sides of
that association (both the record that holds the reference and the record being referenced). As
discussed in [Chapter 2](ch02.html#ch_datamodels), denormalization can reduce the need for joins but generally not
remove it entirely.[v](ch10.html#idm140605758092544) 
In a database, if you execute a query that involves only a small number of records, the database
will typically use an index to quickly locate the records of interest (see [Chapter 3](ch03.html#ch_storage)). If
the query involves joins, it may require multiple index lookups. However, MapReduce has no concept
of indexes—at least not in the usual sense.