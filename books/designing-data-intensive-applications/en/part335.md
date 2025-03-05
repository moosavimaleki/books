In a multi-leader configuration, you can have a leader in each datacenter.
[Figure 5-6](#fig_replication_multi_dc) shows what this architecture might look like. Within each datacenter,
regular leader–follower replication is used; between datacenters, each datacenter’s leader
replicates its changes to the leaders in other datacenters. ![ddia 0506](assets/ddia_0506.png) ###### Figure 5-6. Multi-leader replication across multiple datacenters. 
Let’s compare how the single-leader and multi-leader configurations fare in a multi-datacenter
deployment: Performance In a single-leader configuration, every write must go over the internet to the datacenter with the
leader. This can add significant latency to
writes and might contravene the purpose of having multiple datacenters in the first place. In a
multi-leader configuration, every write can be processed in the local datacenter and is replicated
asynchronously to the other datacenters. Thus, the inter-datacenter network delay is hidden from
users, which means the perceived performance may be better. Tolerance of datacenter outages In a single-leader configuration, if the datacenter with the leader fails, failover can promote a
follower in another datacenter to be leader. In a multi-leader configuration, each datacenter can
continue operating independently of the others, and replication catches up when the failed
datacenter comes back online.