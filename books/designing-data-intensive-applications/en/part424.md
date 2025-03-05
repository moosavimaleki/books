
Such automation can be dangerous in combination with automatic failure detection. For example, say
one node is overloaded and is temporarily slow to respond to requests. The other nodes conclude that
the overloaded node is dead, and automatically rebalance the cluster to move load away from it. This
puts additional load on the overloaded node, other nodes, and the network—making the situation worse
and potentially causing a cascading failure. For that reason, it can be a good thing to have a human in the loop for rebalancing. It’s slower
than a fully automatic process, but it can help prevent operational surprises. # Request Routing 
We have now partitioned our dataset across multiple nodes running on multiple machines. But there
remains an open question: when a client wants to make a request, how does it know which node to
connect to? As partitions are rebalanced, the assignment of partitions to nodes changes. Somebody
needs to stay on top of those changes in order to answer the question: if I want to read or write
the key “foo”, which IP address and port number do I need to connect to?