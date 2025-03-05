*  Due to the integrity property, messages are not duplicated. *  Due to the validity property, messages are not corrupted and not fabricated out of thin air. *  Due to the termination property, messages are not lost. 
Viewstamped Replication, Raft, and Zab implement total order broadcast directly, because that is more
efficient than doing repeated rounds of one-value-at-a-time consensus. In the case of Paxos, this
optimization is known as Multi-Paxos. ### Single-leader replication and consensus 
In [Chapter 5](ch05.html#ch_replication) we discussed single-leader replication (see [“Leaders and Followers”](ch05.html#sec_replication_leader)), which
takes all the writes to the leader and applies them to the followers in the same order, thus keeping
replicas up to date. Isn’t this essentially total order broadcast? How come we didn’t have to worry
about consensus in [Chapter 5](ch05.html#ch_replication)? The answer comes down to how the leader is chosen. If the leader is manually chosen and configured
by the humans in your operations team, you essentially have a “consensus algorithm” of the
dictatorial variety: only one node is allowed to accept writes (i.e., make decisions about the order
of writes in the replication log), and if that node goes down, the system becomes unavailable for
writes until the operators manually configure a different node to be the leader. Such a system can
work well in practice, but it does not satisfy the termination property of consensus because it
requires human intervention in order to make progress.