That includes decisions about declaring nodes dead. If a quorum of nodes declares another node
dead, then it must be considered dead, even if that node still very much feels alive. The individual
node must abide by the quorum decision and step down. Most commonly, the quorum is an absolute majority of more than half the nodes (although other kinds
of quorums are possible). A majority quorum allows the system to continue working if individual nodes
have failed (with three nodes, one failure can be tolerated; with five nodes, two failures can be
tolerated). However, it is still safe, because there can only be only one majority in the
system—there cannot be two majorities with conflicting decisions at the same time. We will discuss
the use of quorums in more detail when we get to consensus algorithms in [Chapter 9](ch09.html#ch_consistency). ### The leader and the lock 
Frequently, a system requires there to be only one of some thing. For example: