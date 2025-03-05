
In distributed actor frameworks, this programming model is used to scale an application across
multiple nodes. The same message-passing mechanism is used, no matter whether the sender and recipient
are on the same node or different nodes. If they are on different nodes, the message is
transparently encoded into a byte sequence, sent over the network, and decoded on the other side. 
Location transparency works better in the actor model than in RPC, because the actor model already
assumes that messages may be lost, even within a single process. Although latency over the network
is likely higher than within the same process, there is less of a fundamental mismatch between local
and remote communication when using the actor model. A distributed actor framework essentially integrates a message broker and the actor programming
model into a single framework. However, if you want to perform rolling upgrades of your actor-based
application, you still have to worry about forward and backward compatibility, as messages may be
sent from a node running the new version to a node running the old version, and vice versa.