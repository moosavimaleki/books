
As the same or related data appears in several different places, they need to be kept in sync with
one another: if an item is updated in the database, it also needs to be updated in the cache, search
indexes, and data warehouse. With data warehouses this synchronization is usually performed by ETL
processes (see [“Data Warehousing”](ch03.html#sec_storage_dwh)), often by taking a full copy of a database, transforming it, and
bulk-loading it into the data warehouse—in other words, a batch process. Similarly, we saw in
[“The Output of Batch Workflows”](ch10.html#sec_batch_output) how search indexes, recommendation systems, and other derived data systems
might be created using batch processes. 
If periodic full database dumps are too slow, an alternative that is sometimes used is dual
writes, in which the application code explicitly writes to each of the systems when data changes:
for example, first writing to the database, then updating the search index, then invalidating the
cache entries (or even performing those writes concurrently).