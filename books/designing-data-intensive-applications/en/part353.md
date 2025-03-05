## Writing to the Database When a Node Is Down Imagine you have a database with three replicas, and one of the replicas is currently
unavailable—perhaps it is being rebooted to install a system update. In a leader-based
configuration, if you want to continue processing writes, you may need to perform a failover (see
[“Handling Node Outages”](#sec_replication_failover)). 
On the other hand, in a leaderless configuration, failover does not exist.
[Figure 5-10](#fig_replication_quorum_node_outage) shows what happens: the client (user 1234) sends the write to
all three replicas in parallel, and the two available replicas accept the write but the unavailable
replica misses it. Let’s say that it’s sufficient for two out of three replicas to
acknowledge the write: after user 1234 has received two ok responses, we consider the write to be
successful. The client simply ignores the fact that one of the replicas missed the write. ![ddia 0510](assets/ddia_0510.png) ###### Figure 5-10. A quorum write, quorum read, and read repair after a node outage.