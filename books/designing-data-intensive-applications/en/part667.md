Consensus algorithms (linearizable) 
Some consensus algorithms, which we will discuss later in this chapter, bear a resemblance to
single-leader replication. However, consensus protocols contain measures to prevent split brain
and stale replicas. Thanks to these details, consensus algorithms can implement linearizable
storage safely. This is how ZooKeeper
[[21](ch09.html#Junqueira2011jc)]
and etcd
[[22](ch09.html#Ongaro2014wq)] work, for example. Multi-leader replication (not linearizable) 
Systems with multi-leader replication are generally not linearizable, because they concurrently
process writes on multiple nodes and asynchronously replicate them to other nodes. For this
reason, they can produce conflicting writes that require resolution (see
[“Handling Write Conflicts”](ch05.html#sec_replication_write_conflicts)). Such conflicts are an artifact of the lack of a single copy
of the data. Leaderless replication (probably not linearizable) For systems with leaderless replication (Dynamo-style; see [“Leaderless Replication”](ch05.html#sec_replication_leaderless)), people
sometimes claim that you can obtain “strong consistency” by requiring quorum reads and writes
(w + r > n). Depending on the exact configuration of the quorums, and
depending on how you define strong consistency, this is not quite true.