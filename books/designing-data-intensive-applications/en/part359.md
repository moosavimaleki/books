## Limitations of Quorum Consistency 
If you have n replicas, and you choose w and r such that w + r > n, you can
generally expect every read to return the most recent value written for a key. This is the case because the
set of nodes to which you’ve written and the set of nodes from which you’ve read must overlap. That
is, among the nodes you read there must be at least one node with the latest value (illustrated in
[Figure 5-11](#fig_replication_quorum_overlap)). Often, r and w are chosen to be a majority (more than n/2) of nodes, because that ensures
w + r > n while still tolerating up to n/2 node failures. But quorums are
not necessarily majorities—it only matters that the sets of nodes used by the read and write
operations overlap in at least one node. Other quorum assignments are possible, which allows some
flexibility in the design of distributed algorithms
[[45](ch05.html#Howard2016tz_ch5)].