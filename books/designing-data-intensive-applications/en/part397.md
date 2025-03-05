
The main reason for wanting to partition data is scalability. Different partitions can be placed
on different nodes in a shared-nothing cluster (see the introduction to [Part II](part02.html#part_distributed_data)
for a definition of shared nothing). Thus, a large dataset can be distributed across many disks,
and the query load can be distributed across many processors. For queries that operate on a single partition, each node can independently execute the
queries for its own partition, so query throughput can be scaled by adding more nodes. Large,
complex queries can potentially be parallelized across many nodes, although this gets significantly
harder. 
Partitioned databases were pioneered in the 1980s by products such as Teradata and Tandem NonStop
SQL [[1](ch06.html#DeWitt1992fn_ch6)],
and more recently rediscovered by NoSQL databases and Hadoop-based data warehouses. Some systems are
designed for transactional workloads, and others for analytics (see [“Transaction Processing or Analytics?”](ch03.html#sec_storage_analytics)): this
difference affects how the system is tuned, but the fundamentals of partitioning apply to both kinds
of workloads.