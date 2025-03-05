
ZooKeeper and etcd are designed to hold small amounts of data that can fit entirely in memory
(although they still write to disk for durability)—so you wouldn’t want to store all of your
application’s data here. That small amount of data is replicated across all the nodes using a
fault-tolerant total order broadcast algorithm. As discussed previously, total order broadcast is
just what you need for database replication: if each message represents a write to the database,
applying the same writes in the same order keeps replicas consistent with each other. 
ZooKeeper is modeled after Google’s Chubby lock service
[[14](ch09.html#Burrows2006wz),
[98](ch09.html#Chandra2007vp)],
implementing not only total order broadcast (and hence consensus), but also an interesting set of
other features that turn out to be particularly useful when building distributed systems: Linearizable atomic operations 
Using an atomic compare-and-set operation, you can implement a lock: if several nodes concurrently
try to perform the same operation, only one of them will succeed. The consensus protocol
guarantees that the operation will be atomic and linearizable, even if a node fails or the network
is interrupted at any point. A distributed lock is usually implemented as a lease, which has an
expiry time so that it is eventually released in case the client fails (see
[“Process Pauses”](ch08.html#sec_distributed_clocks_pauses)).