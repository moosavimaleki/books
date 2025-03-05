*  If a node carrying a new value fails, and its data is restored from a replica carrying an old
value, the number of replicas storing the new value may fall below w, breaking the quorum
condition. *  Even if everything is working correctly, there are edge cases in which you can get unlucky with
the timing, as we shall see in [“Linearizability and quorums”](ch09.html#sec_consistency_quorum_linearizable). Thus, although quorums appear to guarantee that a read returns the latest written value, in practice
it is not so simple. Dynamo-style databases are generally optimized for use cases that can tolerate
eventual consistency. The parameters w and r allow you to adjust the probability of stale values
being read, but it’s wise to not take them as absolute guarantees. In particular, you usually do not get the guarantees discussed in [“Problems with Replication Lag”](#sec_replication_lag) (reading
your writes, monotonic reads, or consistent prefix reads), so the previously mentioned anomalies can
occur in applications. Stronger guarantees generally require transactions or consensus. We will
return to these topics in [Chapter 7](ch07.html#ch_transactions) and [Chapter 9](ch09.html#ch_consistency).