### Dynamic partitioning 
For databases that use key range partitioning (see [“Partitioning by Key Range”](#sec_partitioning_key_range)), a fixed number
of partitions with fixed boundaries would be very inconvenient: if you got the boundaries wrong, you
could end up with all of the data in one partition and all of the other partitions empty.
Reconfiguring the partition boundaries manually would be very tedious. 
For that reason, key range–partitioned databases such as HBase and RethinkDB create partitions
dynamically. When a partition grows to exceed a configured size (on HBase, the default is
10 GB), it is split into two partitions so that approximately half of the data ends up on each
side of the split [[26](ch06.html#Soztutar2013wv)].
Conversely, if lots of data is deleted and a partition shrinks below some threshold, it can be
merged with an adjacent partition.

This process is similar to what happens at the top level of a B-tree (see [“B-Trees”](ch03.html#sec_storage_b_trees)).