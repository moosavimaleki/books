A long-running transaction may continue using a snapshot for a long time, continuing to read values
that (from other transactions’ point of view) have long been overwritten or deleted. By never
updating values in place but instead creating a new version every time a value is changed, the
database can provide a consistent snapshot while incurring only a small overhead. ### Indexes and snapshot isolation 
How do indexes work in a multi-version database? One option is to have the index simply point to all
versions of an object and require an index query to filter out any object versions that are not
visible to the current transaction. When garbage collection removes old object versions that are no
longer visible to any transaction, the corresponding index entries can also be removed. 
In practice, many implementation details determine the performance of multi-version concurrency
control. For example, PostgreSQL has optimizations for avoiding index updates if different versions
of the same object can fit on the same page
[[31](ch07.html#Momjian2014vg)].