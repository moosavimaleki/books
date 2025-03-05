
This is an instance of a more general problem called service discovery, which isn’t limited to
just databases. Any piece of software that is accessible over a network has this problem, especially
if it is aiming for high availability (running in a redundant configuration on multiple machines).
Many companies have written their own in-house service discovery tools, and many of these have been
released as open source [[30](ch06.html#Wilder2014tw)]. 
On a high level, there are a few different approaches to this problem (illustrated in
[Figure 6-7](#fig_partitioning_routing)): 1.  Allow clients to contact any node (e.g., via a round-robin load balancer). If that node
coincidentally owns the partition to which the request applies, it can handle the request
directly; otherwise, it forwards the request to the appropriate node, receives the reply, and
passes the reply along to the client. 2.  Send all requests from clients to a routing tier first, which determines the node that should
handle each request and forwards it accordingly. This routing tier does not itself handle any
requests; it only acts as a partition-aware load balancer.