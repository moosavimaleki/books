Linearizability is not the only way of avoiding this race condition, but it’s the simplest to
understand. If you control the additional communication channel (like in the case of the message
queue, but not in the case of Alice and Bob), you can use alternative approaches similar to what we
discussed in [“Reading Your Own Writes”](ch05.html#sec_replication_ryw), at the cost of additional complexity. ## Implementing Linearizable Systems 
Now that we’ve looked at a few examples in which linearizability is useful, let’s think about how we
might implement a system that offers linearizable semantics. Since linearizability essentially means “behave as though there is only a single copy of the data,
and all operations on it are atomic,” the simplest answer would be to really only use a single copy
of the data. However, that approach would not be able to tolerate faults: if the node holding that
one copy failed, the data would be lost, or at least inaccessible until the node was brought up
again.