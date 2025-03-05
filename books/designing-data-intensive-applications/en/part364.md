There has been some research on measuring replica staleness in databases with leaderless
replication and predicting the expected percentage of stale reads depending on the parameters n,
w, and r [[48](ch05.html#Bailis2014kt)].
This is unfortunately not yet common practice, but it would be good to include staleness
measurements in the standard set of metrics for databases. Eventual consistency is a deliberately
vague guarantee, but for operability it’s important to be able to quantify “eventual.” ## Sloppy Quorums and Hinted Handoff 
Databases with appropriately configured quorums can tolerate the failure of individual nodes without
the need for failover. They can also tolerate individual nodes going slow, because requests don’t have
to wait for all n nodes to respond—they can return when w or r nodes have responded. These
characteristics make databases with leaderless replication appealing for use cases that require
high availability and low latency, and that can tolerate occasional stale reads.