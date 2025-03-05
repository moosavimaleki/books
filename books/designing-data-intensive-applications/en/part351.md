
To order these events correctly, a technique called version vectors can be used, which we will
discuss later in this chapter (see [“Detecting Concurrent Writes”](#sec_replication_concurrent)). However, conflict detection
techniques are poorly implemented in many multi-leader replication systems. For example, at the time
of writing, PostgreSQL BDR does not provide causal ordering of writes
[[27](ch05.html#PostgresBDR)],
and Tungsten Replicator for MySQL doesn’t even try to detect conflicts
[[34](ch05.html#Hodges2013vb)]. If you are using a system with multi-leader replication, it is worth being aware of these issues,
carefully reading the documentation, and thoroughly testing your database to ensure that it really
does provide the guarantees you believe it to have. # Leaderless Replication 
The replication approaches we have discussed so far in this chapter—single-leader and
multi-leader replication—are based on the idea that a client sends a write request to one node
(the leader), and the database system takes care of copying that write to the other replicas. A
leader determines the order in which writes should be processed, and followers apply the leader’s
writes in the same order.