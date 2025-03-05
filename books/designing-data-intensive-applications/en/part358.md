*  If w < n, we can still process writes if a node is unavailable. *  If r < n, we can still process reads if a node is unavailable. *  With n = 3, w = 2, r = 2 we can tolerate one unavailable node. *  With n = 5, w = 3, r = 3 we can tolerate two unavailable nodes.
This case is illustrated in [Figure 5-11](#fig_replication_quorum_overlap). *  Normally, reads and writes are always sent to all n replicas in parallel. The parameters w and
r determine how many nodes we wait for—i.e., how many of the n nodes need to report success
before we consider the read or write to be successful. ![ddia 0511](assets/ddia_0511.png) ###### Figure 5-11. If w + r > n, at least one of the r replicas you read from must have seen the most recent successful write. If fewer than the required w or r nodes are available, writes or reads return an error. A node
could be unavailable for many reasons: because the node is down (crashed, powered down), due to an
error executing the operation (can’t write because the disk is full), due to a network interruption
between the client and the node, or for any number of other reasons. We only care whether the node
returned a successful response and don’t need to distinguish between different kinds of fault.