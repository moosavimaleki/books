### Using total order broadcast 
Consensus services such as ZooKeeper and etcd actually implement total order broadcast. This fact is a
hint that there is a strong connection between total order broadcast and consensus, which we will
explore later in this chapter. 
Total order broadcast is exactly what you need for database replication: if every message represents
a write to the database, and every replica processes the same writes in the same order, then the
replicas will remain consistent with each other (aside from any temporary replication lag). This
principle is known as state machine replication
[[60](ch09.html#Schneider1990vy)], and we will return to it in [Chapter 11](ch11.html#ch_stream). 
Similarly, total order broadcast can be used to implement serializable transactions: as discussed in
[“Actual Serial Execution”](ch07.html#sec_transactions_serial), if every message represents a deterministic transaction to be executed
as a stored procedure, and if every node processes those messages in the same order, then the
partitions and replicas of the database are kept consistent with each other
[[61](ch09.html#Thomson2012tx)].