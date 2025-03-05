
Once you have an implementation of consensus, applications can use it for various purposes. For
example, say you have a database with single-leader replication. If the leader dies and you need to
fail over to another node, the remaining database nodes can use consensus to elect a new leader. As
discussed in [“Handling Node Outages”](ch05.html#sec_replication_failover), it’s important that there is only one leader, and that
all nodes agree who the leader is. If two nodes both believe that they are the leader, that
situation is called split brain, and it often leads to data loss. Correct implementations of
consensus help avoid such problems. Later in this chapter, in [“Distributed Transactions and Consensus”](#sec_consistency_consensus), we will look into
algorithms to solve consensus and related problems. But
first we first need to explore the range of guarantees and abstractions that can be provided in a
distributed system. We need to understand the scope of what can and cannot be done: in some situations, it’s possible
for the system to tolerate faults and continue working; in other situations, that is not possible.
The limits of what is and isn’t possible have been explored in depth, both in theoretical proofs and
in practical implementations. We will get an overview of those fundamental limits in this chapter.