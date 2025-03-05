
Unless you have some additional concurrency detection mechanism, such as the version vectors we
discussed in [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent), you will not even notice that concurrent writes
occurred—one value will simply silently overwrite another value. 
Another problem with dual writes is that one of the writes may fail while the other succeeds. This
is a fault-tolerance problem rather than a concurrency problem, but it also has the effect of the
two systems becoming inconsistent with each other. Ensuring that they either both succeed or both
fail is a case of the atomic commit problem, which is expensive to solve (see
[“Atomic Commit and Two-Phase Commit (2PC)”](ch09.html#sec_consistency_2pc)). 
If you only have one replicated database with a single leader, then that leader determines the order
of writes, so the state machine replication approach works among replicas of the database. However,
in [Figure 11-4](#fig_stream_write_order) there isn’t a single leader: the database may have a leader and the
search index may have a leader, but neither follows the other, and so conflicts can occur (see
[“Multi-Leader Replication”](ch05.html#sec_replication_multi_leader)).