
Fortunately, we have already seen a good solution earlier in this chapter: LSM-trees. All writes
first go to an in-memory store, where they are added to a sorted structure and prepared for writing
to disk. It doesn’t matter whether the in-memory store is row-oriented or column-oriented. When
enough writes have accumulated, they are merged with the column files on disk and written to new
files in bulk. This is essentially what Vertica does
[[62](ch03.html#Lamb2012ub)]. Queries need to examine both the column data on disk and the recent writes in memory, and combine
the two. However, the query optimizer hides this distinction from the user. From an analyst’s point
of view, data that has been modified with inserts, updates, or deletes is immediately reflected in
subsequent queries. ## Aggregation: Data Cubes and Materialized Views 
Not every data warehouse is necessarily a column store: traditional row-oriented databases and a few
other architectures are also used. However, columnar storage can be significantly faster for ad hoc
analytical queries, so it is rapidly gaining popularity
[[51](ch03.html#OneSizeFitsNone2013vw),
[63](ch03.html#LeDem2014tl)].