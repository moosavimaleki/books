# Ordering Guarantees 
We said previously that a linearizable register behaves as if there is only a single copy of the
data, and that every operation appears to take effect atomically at one point in time. This
definition implies that operations are executed in some well-defined order. We illustrated the
ordering in [Figure 9-4](#fig_consistency_linearizability_3) by joining up the operations in the order in which
they seem to have executed. Ordering has been a recurring theme in this book, which suggests that it might be an important
fundamental idea. Let’s briefly recap some of the other contexts in which we have discussed
ordering: *  
In [Chapter 5](ch05.html#ch_replication) we saw that the main purpose of the leader in single-leader replication is
to determine the order of writes in the replication log—that is, the order in which followers
apply those writes. If there is no single leader, conflicts can occur due to concurrent operations
(see [“Handling Write Conflicts”](ch05.html#sec_replication_write_conflicts)).