
If a join input has hot keys, there are a few algorithms you can use to compensate. For example, the
skewed join method in Pig first runs a sampling job to determine which keys are hot
[[39](ch10.html#Manjunath2009bh)]. When performing the actual join, the mappers send any records relating to a hot key
to one of several reducers, chosen at random (in contrast to conventional MapReduce, which chooses a
reducer deterministically based on a hash of the key). For the other input to the join, records
relating to the hot key need to be replicated to all reducers handling that key
[[40](ch10.html#DeWitt1992ws)]. 
This technique spreads the work of handling the hot key over several reducers, which allows it to be
parallelized better, at the cost of having to replicate the other join input to multiple reducers.
The sharded join method in Crunch is similar, but requires the hot keys to be specified explicitly
rather than using a sampling job. This technique is also very similar to one we discussed in
[“Skewed Workloads and Relieving Hot Spots”](ch06.html#sec_partitioning_skew), using randomization to alleviate hot spots in a partitioned database.