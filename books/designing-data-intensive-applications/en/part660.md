## Relying on Linearizability 
In what circumstances is linearizability useful? Viewing the final score of a sporting match is
perhaps a frivolous example: a result that is outdated by a few seconds is unlikely to cause any
real harm in this situation. However, there a few areas in which linearizability is an important
requirement for making a system work correctly. ### Locking and leader election 
A system that uses single-leader replication needs to ensure that there is indeed only one leader,
not several (split brain). One way of electing a leader is to use a lock: every node that starts up
tries to acquire the lock, and the one that succeeds becomes the leader
[[14](ch09.html#Burrows2006wz)]. No matter how this
lock is implemented, it must be linearizable: all nodes must agree which node owns the lock;
otherwise it is useless. 
Coordination services like Apache ZooKeeper
[[15](ch09.html#Junqueira2013wi_ch9)] and etcd
[[16](ch09.html#Etcd)] are often used to implement
distributed locks and leader election. They use consensus algorithms to implement linearizable
operations in a fault-tolerant way (we discuss such algorithms later in this chapter, in
[“Fault-Tolerant Consensus”](#sec_consistency_consensus_ft)).[iii](ch09.html#idm140605759949024) There are still
many subtle details to implementing locks and leader
election correctly (see for example the fencing issue in [“The leader and the lock”](ch08.html#sec_distributed_lock_fencing)), and
libraries like Apache Curator
[[17](ch09.html#ApacheCurator)]
help by providing higher-level recipes on top of ZooKeeper. However, a linearizable storage service
is the basic foundation for these coordination tasks.