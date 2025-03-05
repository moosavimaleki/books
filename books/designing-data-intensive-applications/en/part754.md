Although service discovery does not require consensus, leader election does. Thus, if your consensus
system already knows who the leader is, then it can make sense to also use that information to help
other services discover who the leader is. For this purpose, some consensus systems support
read-only caching replicas. These replicas asynchronously receive the log of all decisions of the
consensus algorithm, but do not actively participate in voting. They are therefore able to serve
read requests that do not need to be linearizable. ### Membership services 
ZooKeeper and friends can be seen as part of a long history of research into membership services,
which goes back to the 1980s and has been important for building highly reliable systems, e.g., for
air traffic control [[110](ch09.html#Birman2010ct)]. A membership service determines which nodes are currently active and live members of a cluster. As
we saw throughout [Chapter 8](ch08.html#ch_distributed), due to unbounded network delays it’s not possible to reliably
detect whether another node has failed. However, if you couple failure detection with consensus,
nodes can come to an agreement about which nodes should be considered alive or not.