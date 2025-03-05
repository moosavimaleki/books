Of course, if all nodes crash and none of them are running, then it is not possible for any
algorithm to decide anything. There is a limit to the number of failures that an algorithm can
tolerate: in fact, it can be proved that any consensus algorithm requires at least a majority of
nodes to be functioning correctly in order to assure termination
[[67](ch09.html#Chandra1996cp)]. That majority can safely form a quorum
(see [“Quorums for reading and writing”](ch05.html#sec_replication_quorum_condition)). 
Thus, the termination property is subject to the assumption that fewer than half of the nodes are
crashed or unreachable. However, most implementations of consensus ensure that the safety
properties—agreement, integrity, and validity—are always met, even if a majority of nodes fail or
there is a severe network problem
[[92](ch09.html#Dwork1988dr_ch9)].
Thus, a large-scale outage can stop the system from being able to process requests, but it cannot
corrupt the consensus system by causing it to make invalid decisions.