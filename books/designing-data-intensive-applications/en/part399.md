Everything we discussed in [Chapter 5](ch05.html#ch_replication) about replication of databases applies equally to
replication of partitions. The choice of partitioning scheme is mostly independent of the choice of
replication scheme, so we will keep things simple and ignore replication in this chapter. ![ddia 0601](assets/ddia_0601.png) ###### Figure 6-1. Combining replication and partitioning: each node acts as leader for some partitions and follower for other partitions. # Partitioning of Key-Value Data 
Say you have a large amount of data, and you want to partition it. How do you decide which records
to store on which nodes? Our goal with partitioning is to spread the data and the query load evenly across nodes. If every
node takes a fair share, then—in theory—10 nodes should be able to handle 10 times as much
data and 10 times the read and write throughput of a single node (ignoring replication for now). 
If the partitioning is unfair, so that some partitions have more data or queries than others, we
call it skewed. The presence of skew makes partitioning much less effective. In an extreme case, all the load
could end up on one partition, so 9 out of 10 nodes are idle and your bottleneck is the
single busy node. A partition with disproportionately high load is called a hot spot.