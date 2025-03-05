Tolerance of network problems Traffic between datacenters usually goes over the public internet, 
which may be less reliable than the local network within a datacenter. A single-leader
configuration is very sensitive to problems in this inter-datacenter link, because writes are made
synchronously over this link. A multi-leader configuration with asynchronous replication can
usually tolerate network problems better: a temporary network interruption does not prevent writes
being processed. 
Some databases support multi-leader configurations by default, but it is also often implemented with
external tools, such as Tungsten Replicator for MySQL
[[26](ch05.html#TungstenReplicator)], BDR for PostgreSQL
[[27](ch05.html#PostgresBDR)],
and GoldenGate for Oracle [[19](ch05.html#Oracle2013ub)]. Although multi-leader replication has advantages, it also has a big downside: the same data may be
concurrently modified in two different datacenters, and those write conflicts must be resolved
(indicated as “conflict resolution” in [Figure 5-6](#fig_replication_multi_dc)). We will discuss this issue in
[“Handling Write Conflicts”](#sec_replication_write_conflicts). As multi-leader replication is a somewhat retrofitted feature in many databases, there are often
subtle configuration pitfalls and surprising interactions with other database features. For example,
autoincrementing keys, triggers, and integrity constraints can be problematic. For this reason,
multi-leader replication is often considered dangerous territory that should be avoided if possible
[[28](ch05.html#Hodges2012ue)].