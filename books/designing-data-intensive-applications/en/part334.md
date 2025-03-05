A natural extension of the leader-based replication model is to allow more than one node to accept
writes. Replication still happens in the same way: each node that processes a write must forward
that data change to all the other nodes. We call this a multi-leader configuration (also known as
master–master or active/active replication). In this setup, each leader simultaneously acts as a
follower to the other leaders. ## Use Cases for Multi-Leader Replication 
It rarely makes sense to use a multi-leader setup within a single datacenter, because the benefits
rarely outweigh the added complexity. However, there are some situations in which this configuration
is reasonable. ### Multi-datacenter operation 
Imagine you have a database with replicas in several different datacenters (perhaps so that you can
tolerate failure of an entire datacenter, or perhaps in order to be closer to your users). With a
normal leader-based replication setup, the leader has to be in one of the datacenters, and all
writes must go through that datacenter.