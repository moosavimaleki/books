In circular and star topologies, a write may need to pass through several nodes before it reaches
all replicas. Therefore, nodes need to forward data changes they receive from other nodes. To
prevent infinite replication loops, each node is given a unique identifier, and in the replication
log, each write is tagged with the identifiers of all the nodes it has passed through
[[43](ch05.html#HBase7709)].
When a node receives a data change that is tagged with its own identifier, that data change is
ignored, because the node knows that it has already been processed. A problem with circular and star topologies is that if just one node fails, it can interrupt the
flow of replication messages between other nodes, causing them to be unable to communicate until the
node is fixed. The topology could be reconfigured to work around the failed node, but in most
deployments such reconfiguration would have to be done manually. The fault tolerance of a more
densely connected topology (such as all-to-all) is better because it allows messages to travel
along different paths, avoiding a single point of failure.