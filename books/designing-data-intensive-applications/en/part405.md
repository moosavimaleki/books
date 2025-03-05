As we shall see in [“Rebalancing Partitions”](#sec_partitioning_rebalancing),
this particular approach actually doesn’t work very well for databases
[[8](ch06.html#Lamping2014)],
so it is rarely used in practice (the documentation of some databases still refers to consistent
hashing, but it is often inaccurate). Because this is so confusing, it’s best to avoid the term
consistent hashing and just call it hash partitioning instead. 
Unfortunately however, by using the hash of the key for partitioning we lose a nice property of
key-range partitioning: the ability to do efficient range queries. Keys that were once adjacent are
now scattered across all the partitions, so their sort order is lost. In MongoDB, if you have
enabled hash-based sharding mode, any range query has to be sent to all partitions
[[4](ch06.html#MongoDBInc2013uf)]. Range queries on the primary key are
not supported by Riak [[9](ch06.html#Redmond2013ws)], Couchbase
[[10](ch06.html#CouchbaseAdmin)], or Voldemort. 
Cassandra achieves a compromise between the two partitioning strategies
[[11](ch06.html#Lakshman2009tz),
[12](ch06.html#Ellis2013vb),
[13](ch06.html#Cassandra2014vj)].
A table in Cassandra can be declared with a compound primary key consisting of several columns.
Only the first part of that key is hashed to determine the partition, but the other columns are used
as a concatenated index for sorting the data in Cassandra’s SSTables. A query therefore cannot
search for a range of values within the first column of a compound key, but if it specifies a fixed
value for the first column, it can perform an efficient range scan over the other columns of the
key.