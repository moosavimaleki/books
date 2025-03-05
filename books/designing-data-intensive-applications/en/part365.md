However, quorums (as described so far) are not as fault-tolerant as they could be. A network
interruption can easily cut off a client from a large number of database nodes. Although those nodes
are alive, and other clients may be able to connect to them, to a client that is cut off from the
database nodes, they might as well be dead. In this situation, it’s likely that fewer than w or r
reachable nodes remain, so the client can no longer reach a quorum. In a large cluster (with significantly more than n nodes) it’s likely that the client can connect
to some database nodes during the network interruption, just not to the nodes that it needs to
assemble a quorum for a particular value. In that case, database designers face a trade-off: *  Is it better to return errors to all requests for which we cannot reach a quorum of w or r
nodes?