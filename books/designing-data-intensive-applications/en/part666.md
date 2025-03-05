The most common approach to making a system fault-tolerant is to use replication. Let’s revisit the
replication methods from [Chapter 5](ch05.html#ch_replication), and compare whether they can be made linearizable: Single-leader replication (potentially linearizable) 
In a system with single-leader replication (see [“Leaders and Followers”](ch05.html#sec_replication_leader)), the leader has the
primary copy of the data that is used for writes, and the followers maintain backup copies of the
data on other nodes. If you make reads from the leader, or from synchronously updated followers,
they have the potential to be
linearizable.[iv](ch09.html#idm140605759893808)
However, not every single-leader database is actually linearizable, either by design (e.g.,
because it uses snapshot isolation) or due to concurrency bugs
[[10](ch09.html#Kingsbury2015uh)]. Using the leader for reads relies on the assumption that you know for sure who the leader is. As
discussed in [“The Truth Is Defined by the Majority”](ch08.html#sec_distributed_majority), it is quite possible for a node to think that it is the
leader, when in fact it is not—and if the delusional leader continues to serve requests, it is
likely to violate linearizability
[[20](ch09.html#Kingsbury2014vc)]. With asynchronous replication, failover may
even lose committed writes (see [“Handling Node Outages”](ch05.html#sec_replication_failover)), which violates both durability and
linearizability.