![ddia 0505](assets/ddia_0505.png) ###### Figure 5-5. If some partitions are replicated slower than others, an observer may see the answer before they see the question. Preventing this kind of anomaly requires another type of guarantee: consistent prefix reads
[[23](ch05.html#Terry2011vp)]. This guarantee says that if a sequence of
writes happens in a certain order, then anyone reading those writes will see them appear in the same
order. This is a particular problem in partitioned (sharded) databases, which we will discuss in
[Chapter 6](ch06.html#ch_partitioning). If the database always applies writes in the same order, reads always see a
consistent prefix, so this anomaly cannot happen. However, in many distributed databases, different
partitions operate independently, so there is no global ordering of writes: when a user reads from
the database, they may see some parts of the database in an older state and some in a newer state. One solution is to make sure that any writes that are causally related to each other are written to
the same partition—but in some applications that cannot be done efficiently. There are also
algorithms that explicitly keep track of causal dependencies, a topic that we will return to in
[“The “happens-before” relationship and concurrency”](#sec_replication_happens_before).