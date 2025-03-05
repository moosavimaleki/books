## Replication Versus Partitioning 
There are two common ways data is distributed across multiple nodes: Replication Keeping a copy of the same data on several different nodes, potentially in different
    locations.  Replication provides redundancy: if some nodes are unavailable, the data can still
    be served from the remaining nodes. Replication can also help improve performance. We discuss
    replication in [Chapter 5](ch05.html#ch_replication). Partitioning Splitting a big database into smaller subsets called partitions so that different
    partitions can be assigned to different nodes (also known as sharding). We discuss
    partitioning in [Chapter 6](ch06.html#ch_partitioning). These are separate mechanisms, but they often go hand in hand, as illustrated in
[Figure II-1](#fig_replication_partitioning). ![ddia 08](assets/ddia_08.png) ###### Figure II-1. A database split into two partitions, with two replicas per partition. With an understanding of those concepts, we can discuss the difficult trade-offs that you need to
make in a distributed system. We’ll discuss transactions in
[Chapter 7](ch07.html#ch_transactions), as that will help you understand all the many
things that can go wrong in a data system, and what you can do about them. We’ll conclude
this part of the book by discussing the fundamental limitations of distributed systems in Chapters
[8](ch08.html#ch_distributed) and
[9](ch09.html#ch_consistency).