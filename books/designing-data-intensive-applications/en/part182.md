When updating a value without changing the key, the heap file approach can be quite efficient: the
record can be overwritten in place, provided that the new value is not larger than the old value.
The situation is more complicated if the new value is larger, as it probably needs to be moved to a
new location in the heap where there is enough space. In that case, either all indexes need to be
updated to point at the new heap location of the record, or a forwarding pointer is left behind in
the old heap location [[5](ch03.html#Graefe2011kk)]. 
In some situations, the extra hop from the index to the heap file is too much of a performance
penalty for reads, so it can be desirable to store the indexed row directly within an index. This is
known as a clustered index. For example, in MySQL’s InnoDB storage engine, the primary key of a
table is always a clustered index, and secondary indexes refer to the primary key (rather than a
heap file location)
[[31](ch03.html#MySQL2014)].
In SQL Server, you can specify one clustered index per table
[[32](ch03.html#SQLServer2012)].