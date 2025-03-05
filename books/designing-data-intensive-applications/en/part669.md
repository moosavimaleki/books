The quorum condition is met (w + r > n), but this execution is nevertheless not
linearizable: B’s request begins after A’s request completes, but B returns the old value while A
returns the new value. (It’s once again the Alice and Bob situation from
[Figure 9-1](#fig_consistency_linearizability_0).) 
Interestingly, it is possible to make Dynamo-style quorums linearizable at the cost of reduced
performance: a reader must perform read repair (see [“Read repair and anti-entropy”](ch05.html#sec_replication_read_repair)) synchronously,
before returning results to the application
[[23](ch09.html#Attiya1995bm)],
and a writer must read the latest state of a quorum of nodes before sending its writes
[[24](ch09.html#Lynch1997gr),
[25](ch09.html#Cachin2011wt)].
However, Riak does not perform synchronous read repair due to the performance penalty
[[26](ch09.html#Elliott2015zg)].
Cassandra does wait for read repair to complete on quorum reads
[[27](ch09.html#Ekstrom2012ix)],
but it loses linearizability if there are multiple concurrent writes to the same key, due to its use
of last-write-wins conflict resolution. 
Moreover, only linearizable read and write operations can be implemented in this way; a
linearizable compare-and-set operation cannot, because it requires a consensus algorithm
[[28](ch09.html#Herlihy1991gk)].