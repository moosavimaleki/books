When a new node joins the cluster, it randomly chooses a fixed number of existing partitions to
split, and then takes ownership of one half of each of those split partitions while leaving the
other half of each partition in place. The randomization can produce unfair splits, but when
averaged over a larger number of partitions (in Cassandra, 256 partitions per node by default), the
new node ends up taking a fair share of the load from the existing nodes. Cassandra 3.0 introduced
an alternative rebalancing algorithm that avoids unfair splits
[[29](ch06.html#Lambov2016wj)]. Picking partition boundaries randomly requires that hash-based partitioning is used (so the
boundaries can be picked from the range of numbers produced by the hash function). Indeed, this
approach corresponds most closely to the original definition of consistent hashing
[[7](ch06.html#Karger1997ko)] (see [“Consistent Hashing”](#sidebar_consistent_hashing)).
Newer hash functions can achieve a similar effect with lower metadata overhead
[[8](ch06.html#Lamping2014)]. ## Operations: Automatic or Manual Rebalancing