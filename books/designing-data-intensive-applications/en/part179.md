If write throughput is high and compaction is not configured carefully, it can happen that
compaction cannot keep up with the rate of incoming writes. In this case, the number of unmerged
segments on disk keeps growing until you run out of disk space, and reads also slow down because
they need to check more segment files. Typically, SSTable-based storage engines do not throttle the
rate of incoming writes, even if compaction cannot keep up, so you need explicit monitoring to
detect this situation [[29](ch03.html#Cassandra1608),
[30](ch03.html#RocksDBTuning)]. An advantage of B-trees is that each key exists in exactly one place in the index, whereas a
log-structured storage engine may have multiple copies of the same key in different segments. This
aspect makes B-trees attractive in databases that want to offer strong transactional semantics: in
many relational databases, transaction isolation is implemented using locks on ranges of keys, and
in a B-tree index, those locks can be directly attached to the tree
[[5](ch03.html#Graefe2011kk)]. In
[Chapter 7](ch07.html#ch_transactions) we will discuss this point in more detail.