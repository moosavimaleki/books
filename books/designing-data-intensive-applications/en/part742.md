### Epoch numbering and quorums 
All of the consensus protocols discussed so far internally use a leader in some form or another, but
they don’t guarantee that the leader is unique. Instead, they can make a weaker guarantee: the
protocols define an epoch number (called the ballot number in Paxos, view number in
Viewstamped Replication, and term number in Raft) and guarantee that within each epoch, the leader
is unique. 
Every time the current leader is thought to be dead, a vote is started among the nodes to elect a
new leader. This election is given an incremented epoch number, and thus epoch numbers are totally
ordered and monotonically increasing. If there is a conflict between two different leaders in two
different epochs (perhaps because the previous leader actually wasn’t dead after all), then the
leader with the higher epoch number prevails. Before a leader is allowed to decide anything, it must first check that there isn’t some other
leader with a higher epoch number which might take a conflicting decision. How does a leader know
that it hasn’t been ousted by another node? Recall [“The Truth Is Defined by the Majority”](ch08.html#sec_distributed_majority): a node cannot
necessarily trust its own judgment—just because a node thinks that it is the leader, that does not
necessarily mean the other nodes accept it as their leader.