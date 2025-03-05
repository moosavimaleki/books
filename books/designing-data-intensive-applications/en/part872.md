
This fault tolerance is achieved by periodically checkpointing the state of all vertices at the end
of an iteration—i.e., writing their full state to durable storage. If a node fails and its in-memory
state is lost, the simplest solution is to roll back the entire graph computation to the last
checkpoint and restart the computation. If the algorithm is deterministic and messages are
logged, it is also possible to selectively recover only the partition that was lost (like we
previously discussed for dataflow engines) [[72](ch10.html#Malewicz2010jq)]. ### Parallel execution 
A vertex does not need to know on which physical machine it is executing; when it sends messages to
other vertices, it simply sends them to a vertex ID. It is up to the framework to partition the
graph—i.e., to decide which vertex runs on which machine, and how to route messages over the
network so that they end up in the right place.