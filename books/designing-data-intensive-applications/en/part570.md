Latency guarantees are achievable in certain environments, if resources are statically partitioned
(e.g., dedicated hardware and exclusive bandwidth allocations). However, it comes at the cost of
reduced utilization—in other words, it is more expensive. On the other hand, multi-tenancy with
dynamic resource partitioning provides better utilization, so it is cheaper, but it has the downside
of variable delays. Variable delays in networks are not a law of nature, but simply the result of a cost/benefit
trade-off. However, such quality of service is currently not enabled in multi-tenant datacenters and public
clouds, or when communicating via the internet.[iv](ch08.html#idm140605760878336)
Currently deployed technology does not allow us to make any guarantees about delays or reliability
of the network: we have to assume that network congestion, queueing, and unbounded delays will
happen. Consequently, there’s no “correct” value for timeouts—they need to be determined
experimentally. # Unreliable Clocks 
Clocks and time are important. Applications depend on clocks in various ways to answer questions
like the following: