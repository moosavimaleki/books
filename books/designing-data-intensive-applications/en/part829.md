
For example, imagine in the case of [Figure 10-2](#fig_batch_join_example) that the user database is small
enough to fit in memory. In this case, when a mapper starts up, it can first read the user
database from the distributed filesystem into an in-memory hash table. Once this is done, the mapper
can scan over the user activity events and simply look up the user ID for each event in the hash
table.[vi](ch10.html#idm140605757973072) There can still be several map tasks: one for each file block of the large input to the join (in
the example of [Figure 10-2](#fig_batch_join_example), the activity events are the large input). Each of these
mappers loads the small input entirely into memory. 
This simple but effective algorithm is called a broadcast hash join: the word broadcast reflects
the fact that each mapper for a partition of the large input reads the entirety of the small input
(so the small input is effectively “broadcast” to all partitions of the large input), and the word
hash reflects its use of a hash table. This join method is supported by Pig (under the name
“replicated join”), Hive (“MapJoin”), Cascading, and Crunch. It is also used in data warehouse query
engines such as Impala
[[41](ch10.html#Kornacker2015uv_ch10)].