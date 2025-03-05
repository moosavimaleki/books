*  Key range partitioning, where keys are sorted, and a partition owns all the keys from some
minimum up to some maximum. Sorting has the advantage that efficient range queries are possible,
but there is a risk of hot spots if the application often accesses keys that are close together in
the sorted order. In this approach, partitions are typically rebalanced dynamically by splitting the range into two
subranges when a partition gets too big. *  Hash partitioning, where a hash function is applied to each key, and a partition owns a range of
hashes. This method destroys the ordering of keys, making range queries inefficient, but may distribute
load more evenly. When partitioning by hash, it is common to create a fixed number of partitions in advance, to assign
several partitions to each node, and to move entire partitions from one node to another when nodes
are added or removed. Dynamic partitioning can also be used.