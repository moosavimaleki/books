
Most consensus algorithms assume that there are no Byzantine faults, as discussed in
[“Byzantine Faults”](ch08.html#sec_distributed_byzantine). That is, if a node does not correctly follow the protocol (for
example, if it sends contradictory messages to different nodes), it may break the safety properties
of the protocol. It is possible to make consensus robust against Byzantine faults as long as fewer
than one-third of the nodes are Byzantine-faulty [[25](ch09.html#Cachin2011wt),
[93](ch09.html#Castro2002ej)],
but we don’t have space to discuss those algorithms in detail in this book. ### Consensus algorithms and total order broadcast 
The best-known fault-tolerant consensus algorithms are Viewstamped Replication (VSR)
[[94](ch09.html#Oki1988ci),
[95](ch09.html#Liskov2012ut)],
Paxos [[96](ch09.html#Lamport1998ea),
[97](ch09.html#Lamport2001ud),
[98](ch09.html#Chandra2007vp), [99](ch09.html#vanRenesse2011wu)],
Raft [[22](ch09.html#Ongaro2014wq),
[100](ch09.html#Ongaro2014wk),
[101](ch09.html#Howard2015ko)],
and Zab [[15](ch09.html#Junqueira2013wi_ch9),
[21](ch09.html#Junqueira2011jc), [102](ch09.html#Medeiros2012ur)].
There are quite a few similarities between these algorithms, but they are not the same
[[103](ch09.html#vanRenesse2014dj)].
In this book we won’t go into full details of the different algorithms: it’s sufficient to be aware
of some of the high-level ideas that they have in common, unless you’re implementing a consensus
system yourself (which is probably not advisable—it’s hard
[[98](ch09.html#Chandra2007vp), [104](ch09.html#Portnoy2012vs)]).