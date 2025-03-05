Some databases perform automatic leader election and failover, promoting a follower to be the new
leader if the old leader fails (see [“Handling Node Outages”](ch05.html#sec_replication_failover)). This brings us closer to
fault-tolerant total order broadcast, and thus to solving consensus. 
However, there is a problem. We previously discussed the problem of split brain, and said that all
nodes need to agree who the leader is—otherwise two different nodes could each believe themselves to
be the leader, and consequently get the database into an inconsistent state. Thus, we need consensus
in order to elect a leader. But if the consensus algorithms described here are actually total order
broadcast algorithms, and total order broadcast is like single-leader replication, and single-leader
replication requires a leader, then… It seems that in order to elect a leader, we first need a leader. In order to solve consensus, we
must first solve consensus. How do we break out of this conundrum?