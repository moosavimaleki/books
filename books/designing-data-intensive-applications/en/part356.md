### Quorums for reading and writing 
In the example of [Figure 5-10](#fig_replication_quorum_node_outage), we considered the write to be successful
even though it was only processed on two out of three replicas. What if only one out of three
replicas accepted the write? How far can we push this? If we know that every successful write is guaranteed to be present on at least two out of three
replicas, that means at most one replica can be stale. Thus, if we read from at least two replicas,
we can be sure that at least one of the two is up to date. If the third replica is down or slow to
respond, reads can nevertheless continue returning an up-to-date value. 
More generally, if there are n replicas, every write must be confirmed by w nodes to be
considered successful, and we must query at least r nodes for each read. (In our example,
n = 3, w = 2, r = 2.) As long as w + r >
n, we expect to get an up-to-date value when reading, because at least one of the r nodes we’re
reading from must be up to date. Reads and writes that obey these r and w values are called
quorum reads and writes
[[44](ch05.html#Gifford1979if)].[vii](ch05.html#idm140605775762224)
You can think of r and w as the minimum number of votes required for the read or write to be
valid.