
Even though the writes don’t have a natural ordering, we can force an arbitrary order on them. For
example, we can attach a timestamp to each write, pick the biggest timestamp as the most “recent,”
and discard any writes with an earlier timestamp. This conflict resolution algorithm, called last
write wins (LWW), is the only supported conflict resolution method in Cassandra
[[53](ch05.html#Ellis2013ug)],
and an optional feature in Riak [[35](ch05.html#Daily2013te_ch5)]. LWW achieves the goal of eventual convergence, but at the cost of durability: if there are several
concurrent writes to the same key, even if they were all reported as successful to the client
(because they were written to w replicas), only one of the writes will survive and the others will
be silently discarded. Moreover, LWW may even drop writes that are not concurrent, as we shall
discuss in [“Timestamps for ordering events”](ch08.html#sec_distributed_lww). There are some situations, such as caching, in which lost writes are perhaps acceptable. If losing
data is not acceptable, LWW is a poor choice for conflict resolution.