Most consensus algorithms assume a fixed set of nodes that participate in voting, which means that
you can’t just add or remove nodes in the cluster. Dynamic membership extensions to consensus
algorithms allow the set of nodes in the cluster to change over time, but they are much less well
understood than static membership algorithms. Consensus systems generally rely on timeouts to detect failed nodes. In environments with highly
variable network delays, especially geographically distributed systems, it often happens that a node
falsely believes the leader to have failed due to a transient network issue. Although this error does not
harm the safety properties, frequent leader elections result in terrible performance because the
system can end up spending more time choosing a leader than doing any useful work. 
Sometimes, consensus algorithms are particularly sensitive to network problems. For example, Raft
has been shown to have unpleasant edge cases
[[106](ch09.html#Howard2015cw)]:
if the entire network is working correctly except for one particular network link that is
consistently unreliable, Raft can get into situations where leadership continually bounces between
two nodes, or the current leader is continually forced to resign, so the system effectively never
makes progress. Other consensus algorithms have similar problems, and designing algorithms that are
more robust to unreliable networks is still an open research problem.