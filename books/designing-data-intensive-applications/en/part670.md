In summary, it is safest to assume that a leaderless system with Dynamo-style replication does not
provide linearizability. ## The Cost of Linearizability 
As some replication methods can provide linearizability and others cannot, it is interesting to
explore the pros and cons of linearizability in more depth. 
We already discussed some use cases for different replication methods in [Chapter 5](ch05.html#ch_replication); for
example, we saw that multi-leader replication is often a good choice for multi-datacenter
replication (see [“Multi-datacenter operation”](ch05.html#sec_replication_multi_dc)). An example of such a deployment is illustrated in
[Figure 9-7](#fig_consistency_cap_availability). ![ddia 0907](assets/ddia_0907.png) ###### Figure 9-7. A network interruption forcing a choice between linearizability and availability. Consider what happens if there is a network interruption between the two datacenters. Let’s assume
that the network within each datacenter is working, and clients can reach the datacenters, but the
datacenters cannot connect to each other. With a multi-leader database, each datacenter can continue operating normally: since writes from one
datacenter are asynchronously replicated to the other, the writes are simply queued up and exchanged
when network connectivity is restored.