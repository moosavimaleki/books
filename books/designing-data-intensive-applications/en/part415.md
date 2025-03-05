*  While rebalancing is happening, the database should continue accepting reads and writes. *  No more data than necessary should be moved between nodes, to make rebalancing fast and to
minimize the network and disk I/O load. ## Strategies for Rebalancing There are a few different ways of assigning partitions to nodes
[[23](ch06.html#RethinkingTopology2012th)].
Let’s briefly discuss each in turn. ### How not to do it: hash mod N 
When partitioning by the hash of a key, we said earlier ([Figure 6-3](#fig_partitioning_hashing)) that
it’s best to divide the possible hashes into ranges and assign each range to a partition (e.g.,
assign key to partition 0 if 0 ≤ hash(key) < b0, to
partition 1 if b0 ≤ hash(key) < b1, etc.). 
Perhaps you wondered why we don’t just use mod (the % operator in many programming languages).
For example, hash(key) mod 10 would return a number between 0 and 9 (if we write the hash
as a decimal number, the hash mod 10 would be the last digit). If we have 10 nodes, numbered 0 to
9, that seems like an easy way of assigning each key to a node.