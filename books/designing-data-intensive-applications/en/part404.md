Once you have a suitable hash function for keys, you can assign each partition a range of hashes
(rather than a range of keys), and every key whose hash falls within a partition’s range will be
stored in that partition. This is illustrated in [Figure 6-3](#fig_partitioning_hashing). ![ddia 0603](assets/ddia_0603.png) ###### Figure 6-3. Partitioning by hash of key. This technique is good at distributing keys fairly among the partitions. The partition boundaries
can be evenly spaced, or they can be chosen pseudorandomly (in which case the technique is
sometimes known as consistent hashing). ##### Consistent Hashing 
Consistent hashing, as defined by Karger et al.
[[7](ch06.html#Karger1997ko)],
is a way of evenly distributing load across an internet-wide system of caches such as a content
delivery network (CDN). It uses randomly chosen partition boundaries to avoid the need for central
control or distributed consensus. Note that consistent here has nothing to do with replica
consistency (see [Chapter 5](ch05.html#ch_replication)) or ACID consistency (see [Chapter 7](ch07.html#ch_transactions)), but rather
describes a particular approach to rebalancing.