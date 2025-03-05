We discussed three main approaches to replication: *Single-leader replication* Clients send all writes to a single node (the leader), which sends a
stream of data change events to the other replicas (followers). Reads can be performed on any
replica, but reads from followers might be stale. *Multi-leader replication* Clients send each write to one of several leader nodes, any of which
can accept writes. The leaders send streams of data change events to each other and to any
follower nodes. *Leaderless replication* Clients send each write to several nodes, and read from several nodes
in parallel in order to detect and correct nodes with stale data. Each approach has advantages and disadvantages. Single-leader replication is popular because it is fairly
easy to understand and there is no conflict resolution to worry about. Multi-leader and
leaderless replication can be more robust in the presence of faulty nodes, network interruptions,
and latency spikes—at the cost of being harder to reason about and providing only very weak
consistency guarantees.