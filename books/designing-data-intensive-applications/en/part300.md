# Chapter 5. Replication

# Chapter 5. Replication The major difference between a thing that might go wrong and a thing that cannot possibly go wrong
is that when a thing that cannot possibly go wrong goes wrong it usually turns out to be impossible
to get at or repair. Douglas Adams, Mostly Harmless (1992) ![](assets/ch05-map.png) Replication means keeping a copy of the same data on multiple machines that are connected via a
network. As discussed in the introduction to [Part II](part02.html#part_distributed_data), there are several reasons
why you might want to replicate data: *  To keep data geographically close to your users (and thus reduce latency) *  To allow the system to continue working even if some of its parts have failed (and thus
increase availability) *  To scale out the number of machines that can serve read queries (and thus increase read
throughput) In this chapter we will assume that your dataset is so small that each machine can hold a copy of
the entire dataset. In [Chapter 6](ch06.html#ch_partitioning) we will relax that assumption and discuss partitioning
(sharding) of datasets that are too big for a single machine. In later chapters we will discuss
various kinds of faults that can occur in a replicated data system, and how to deal with them.