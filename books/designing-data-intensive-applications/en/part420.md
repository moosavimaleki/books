
Each partition is assigned to one node, and each node can handle multiple partitions, like in the
case of a fixed number of partitions. After a large partition has been split, one of its two halves
can be transferred to another node in order to balance the load. In the case of HBase, the transfer
of partition files happens through HDFS, the underlying distributed filesystem
[[3](ch06.html#HBase2014)]. An advantage of dynamic partitioning is that the number of partitions adapts to the total data
volume. If there is only a small amount of data, a small number of partitions is sufficient, so
overheads are small; if there is a huge amount of data, the size of each individual partition is
limited to a configurable maximum
[[23](ch06.html#RethinkingTopology2012th)]. 
However, a caveat is that an empty database starts off with a single partition, since there is no a
priori information about where to draw the partition boundaries. While the dataset is small—until
it hits the point at which the first partition is split—all writes have to be processed by a single
node while the other nodes sit idle. To mitigate this issue, HBase and MongoDB allow an initial set
of partitions to be configured on an empty database (this is called pre-splitting). In the case of
key-range partitioning, pre-splitting requires that you already know what the key distribution is
going to look like [[4](ch06.html#MongoDBInc2013uf),
[26](ch06.html#Soztutar2013wv)].