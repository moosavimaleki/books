###### Note 
Database administrators and developers love to argue about normalization and denormalization, but
we will suspend judgment for now. In [Part III](part03.html#part_systems) of this book we will return to this topic and
explore systematic ways of dealing with caching, denormalization, and derived data. 
Unfortunately, normalizing this data requires many-to-one relationships (many people live in one
particular region, many people work in one particular industry), which don’t fit nicely into the
document model. In relational databases, it’s normal to refer to rows in other tables by ID, because
joins are easy. In document databases, joins are not needed for one-to-many tree structures, and
support for joins is often weak.[iii](ch02.html#idm140605782440736) If the database itself does not support joins, you have to emulate a join in application code by
making multiple queries to the database. (In this case, the lists of regions and industries are
probably small and slow-changing enough that the application can simply keep them in memory. But
nevertheless, the work of making the join is shifted from the database to the application code.)