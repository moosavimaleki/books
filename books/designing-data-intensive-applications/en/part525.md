In some cases, it’s okay for a transaction to read information that was overwritten by another
transaction: depending on what else happened, it’s sometimes possible to prove that the result of
the execution is nevertheless serializable. PostgreSQL uses this theory to reduce the number of
unnecessary aborts [[11](ch07.html#Fekete2005ee),
[41](ch07.html#Ports2012uw)]. Compared to two-phase locking, the big advantage of serializable snapshot isolation is that one
transaction doesn’t need to block waiting for locks held by another transaction. Like under snapshot
isolation, writers don’t block readers, and vice versa. This design principle makes query latency
much more predictable and less variable. In particular, read-only queries can run on a consistent
snapshot without requiring any locks, which is very appealing for read-heavy workloads. 
Compared to serial execution, serializable snapshot isolation is not limited to the throughput of a
single CPU core: FoundationDB distributes the detection of serialization conflicts across multiple
machines, allowing it to scale to very high throughput. Even though data may be partitioned across
multiple machines, transactions can read and write data in multiple partitions while ensuring
serializable isolation [[54](ch07.html#Rosenthal2014vv)].