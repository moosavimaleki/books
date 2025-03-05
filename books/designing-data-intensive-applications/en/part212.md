
Another aspect of data warehouses that is worth mentioning briefly is materialized aggregates. As
discussed earlier, data warehouse queries often involve an aggregate function, such as COUNT, SUM,
AVG, MIN, or MAX in SQL. If the same aggregates are used by many different queries, it can be
wasteful to crunch through the raw data every time. Why not cache some of the counts or sums that
queries use most often? 
One way of creating such a cache is a materialized view. In a relational data model, it is often
defined like a standard (virtual) view: a table-like object whose contents are the results of some
query. The difference is that a materialized view is an actual copy of the query results, written to
disk, whereas a virtual view is just a shortcut for writing queries. When you read from a virtual
view, the SQL engine expands it into the view’s underlying query on the fly and then processes the
expanded query.