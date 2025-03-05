3.  Require that clients be aware of the partitioning and the assignment of partitions to
nodes. In this case, a client can connect directly to the
appropriate node, without any intermediary. In all cases, the key problem is: how does the component making the routing decision (which may be
one of the nodes, or the routing tier, or the client) learn about changes in the assignment of
partitions to nodes? ![ddia 0607](assets/ddia_0607.png) ###### Figure 6-7. Three different ways of routing a request to the right node. This is a challenging problem, because it is important that all participants agree—otherwise
requests would be sent to the wrong nodes and not handled correctly. There are protocols for
achieving consensus in a distributed system, but they are hard to implement correctly (see
[Chapter 9](ch09.html#ch_consistency)). 
Many distributed data systems rely on a separate coordination service such as ZooKeeper to keep
track of this cluster metadata, as illustrated in [Figure 6-8](#fig_partitioning_zookeeper). Each node registers
itself in ZooKeeper, and ZooKeeper maintains the authoritative mapping of partitions to nodes. Other
actors, such as the routing tier or the partitioning-aware client, can subscribe to this information
in ZooKeeper. Whenever a partition changes ownership, or a node is added or removed, ZooKeeper
notifies the routing tier so that it can keep its routing information up to date.