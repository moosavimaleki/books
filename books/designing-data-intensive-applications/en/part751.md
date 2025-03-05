Another example arises when you have some partitioned resource (database, message streams, file
storage, distributed actor system, etc.) and need to decide which partition to assign to which node.
As new nodes join the cluster, some of the partitions need to be moved from existing nodes to the
new nodes in order to rebalance the load (see [“Rebalancing Partitions”](ch06.html#sec_partitioning_rebalancing)). As nodes are
removed or fail, other nodes need to take over the failed nodes’ work. 
These kinds of tasks can be achieved by judicious use of atomic operations, ephemeral nodes, and
notifications in ZooKeeper. If done correctly, this approach allows the application to automatically
recover from faults without human intervention. It’s not easy, despite the appearance of libraries
such as Apache Curator [[17](ch09.html#ApacheCurator)] that have sprung
up to provide higher-level tools on top of the ZooKeeper client API—but it is still much better than
attempting to implement the necessary consensus algorithms from scratch, which has a poor success
record [[107](ch09.html#Kingsbury2015uk)].