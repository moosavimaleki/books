[iv](ch09.html#idm140605759893808-marker) Partitioning (sharding) a
single-leader database, so that there is a separate leader per partition, does not affect
linearizability, since it is only a single-object guarantee. Cross-partition transactions are a
different matter (see [“Distributed Transactions and Consensus”](#sec_consistency_consensus)). [v](ch09.html#idm140605759796128-marker) These two
choices are sometimes known as CP (consistent but not available under network partitions) and AP
(available but not consistent under network partitions), respectively. However, this classification
scheme has several flaws [[9](ch09.html#Kleppmann2015un)], so it is
best avoided. [vi](ch09.html#idm140605759746016-marker) As discussed in
[“Network Faults in Practice”](ch08.html#sec_distributed_network_faults), this book uses partitioning
to refer to deliberately breaking down a large dataset into smaller ones (sharding; see
[Chapter 6](ch06.html#ch_partitioning)). By contrast, a network partition is a particular
type of network fault, which we normally don’t consider separately from other kinds of faults.
However, since it’s the P in CAP, we can’t avoid the confusion in this case. [vii](ch09.html#idm140605759564096-marker) A total order that
is inconsistent with causality is easy to create, but not very useful. For example, you can
generate a random UUID for each operation, and compare UUIDs lexicographically to define the total
ordering of operations. This is a valid total order, but the random UUIDs tell you nothing about
which operation actually happened first, or whether the operations were concurrent.