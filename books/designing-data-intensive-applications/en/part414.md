
Other uses of global term-partitioned indexes include Riak’s search feature
[[21](ch06.html#Klophaus2011tt)]
and the Oracle data warehouse, which lets you choose between local and global indexing
[[22](ch06.html#Burleson2000wb)].
We will return to the topic of implementing term-partitioned secondary indexes in [Chapter 12](ch12.html#ch_future). # Rebalancing Partitions 
Over time, things change in a database: *  The query throughput increases, so you want to add more CPUs to handle the load. *  The dataset size increases, so you want to add more disks and RAM to store it. *  A machine fails, and other machines need to take over the failed machine’s responsibilities. All of these changes call for data and requests to be moved from one node to another. The process of
moving load from one node in the cluster to another is called rebalancing. No matter which partitioning scheme is used, rebalancing is usually expected to meet some minimum
requirements: *  After rebalancing, the load (data storage, read and write requests) should be shared fairly
between the nodes in the cluster.