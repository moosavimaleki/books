
As a third scenario, imagine a node that experiences a long stop-the-world garbage collection pause.
All of the node’s threads are preempted by the GC and paused for one minute, and consequently, no
requests are processed and no responses are sent. The other nodes wait, retry, grow impatient, and
eventually declare the node dead and load it onto the hearse. Finally, the GC finishes and the
node’s threads continue as if nothing had happened. The other nodes are surprised as the supposedly
dead node suddenly raises its head out of the coffin, in full health, and starts cheerfully chatting
with bystanders. At first, the GCing node doesn’t even realize that an entire minute has passed and
that it was declared dead—from its perspective, hardly any time has passed since it was last talking
to the other nodes. 
The moral of these stories is that a node cannot necessarily trust its own judgment of a situation.
A distributed system cannot exclusively rely on a single node, because a node may fail at any time,
potentially leaving the system stuck and unable to recover. Instead, many distributed algorithms
rely on a quorum, that is, voting among the nodes (see [“Quorums for reading and writing”](ch05.html#sec_replication_quorum_condition)):
decisions require some minimum number of votes from several nodes in order to reduce the dependence
on any one particular node.