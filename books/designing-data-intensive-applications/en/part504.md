### Partitioning 
Executing all transactions serially makes concurrency control much simpler, but limits the
transaction throughput of the database to the speed of a single CPU core on a single machine.
Read-only transactions may execute elsewhere, using snapshot isolation, but for applications with
high write throughput, the single-threaded transaction processor can become a serious bottleneck. 
In order to scale to multiple CPU cores, and multiple nodes, you can potentially partition your data
(see [Chapter 6](ch06.html#ch_partitioning)), which is supported in VoltDB. If you can find a way of partitioning your
dataset so that each transaction only needs to read and write data within a single partition, then
each partition can have its own transaction processing thread running independently from the
others. In this case, you can give each CPU core its own partition, which allows your transaction
throughput to scale linearly with the number of CPU cores
[[47](ch07.html#Kallman2008tf)]. 
However, for any transaction that needs to access multiple partitions, the database must coordinate the
transaction across all the partitions that it touches. The stored procedure
needs to be performed in lock-step across all partitions to ensure serializability across the whole
system.