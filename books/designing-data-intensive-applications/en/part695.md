As long as the maximum counter value is carried along with every operation, this scheme ensures that
the ordering from the Lamport timestamps is consistent with causality, because every causal
dependency results in an increased timestamp. Lamport timestamps are sometimes confused with version vectors, which we saw in
[“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent). Although there are some similarities, they have a different purpose:
version vectors can distinguish whether two operations are concurrent or whether one is causally
dependent on the other, whereas Lamport timestamps always enforce a total ordering. From the total
ordering of Lamport timestamps, you cannot tell whether two operations are concurrent or whether
they are causally dependent. The advantage of Lamport timestamps over version vectors is that they
are more compact. ### Timestamp ordering is not sufficient 
Although Lamport timestamps define a total order of operations that is consistent with causality,
they are not quite sufficient to solve many common problems in distributed systems.