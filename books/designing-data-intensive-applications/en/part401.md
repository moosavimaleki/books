![ddia 0602](assets/ddia_0602.png) ###### Figure 6-2. A print encyclopedia is partitioned by key range. The ranges of keys are not necessarily evenly spaced, because your data may not be evenly
distributed. For example, in [Figure 6-2](#fig_partitioning_encyclopedia), volume 1 contains words starting with
A and B, but volume 12 contains words starting with T, U, V, X, Y, and Z. Simply having one volume
per two letters of the alphabet would lead to some volumes being much bigger than others. In order
to distribute the data evenly, the partition boundaries need to adapt to the data. 
The partition boundaries might be chosen manually by an administrator, or the database can choose
them automatically (we will discuss choices of partition boundaries in more detail in [“Rebalancing Partitions”](#sec_partitioning_rebalancing)).
This partitioning strategy is used by Bigtable, its open source equivalent HBase
[[2](ch06.html#George2009ti),
[3](ch06.html#HBase2014)],
RethinkDB, and MongoDB before version 2.4 [[4](ch06.html#MongoDBInc2013uf)]. Within each partition, we can keep keys in sorted order (see [“SSTables and LSM-Trees”](ch03.html#sec_storage_lsm_trees)). This has
the advantage that range scans are easy, and you can treat the key as a concatenated index in order
to fetch several related records in one query (see [“Multi-column indexes”](ch03.html#sec_storage_index_multicolumn)). For example,
consider an application that stores data from a network of sensors, where the key is the timestamp
of the measurement (year-month-day-hour-minute-second). Range scans are very useful in this case,
because they let you easily fetch, say, all the readings from a particular month.