Instead, it must collect votes from a quorum of nodes (see [“Quorums for reading and writing”](ch05.html#sec_replication_quorum_condition)).
For every decision that a leader wants to make, it must send the proposed value to the other nodes
and wait for a quorum of nodes to respond in favor of the proposal. The quorum typically, but not
always, consists of a majority of nodes
[[105](ch09.html#Howard2016tz_ch9)]. A node votes in favor of a proposal only if it
is not aware of any other leader with a higher epoch. Thus, we have two rounds of voting: once to choose a leader, and a second time to vote on a leader’s
proposal. The key insight is that the quorums for those two votes must overlap: if a vote on a
proposal succeeds, at least one of the nodes that voted for it must have also participated in the
most recent leader election [[105](ch09.html#Howard2016tz_ch9)]. Thus, if
the vote on a proposal does not reveal any higher-numbered epoch, the current leader can conclude
that no leader election with a higher epoch number has happened, and therefore be sure that it still
holds the leadership. It can then safely decide the proposed value.