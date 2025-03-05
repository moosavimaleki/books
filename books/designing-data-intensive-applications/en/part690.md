
In particular, we can create sequence numbers in a total order that is
consistent with causality:[vii](ch09.html#idm140605759564096)
we promise that if operation A causally happened before B, then A occurs before B in the total
order (A has a lower sequence number than B). Concurrent operations may be ordered arbitrarily. Such
a total order captures all the causality information, but also imposes more ordering than strictly
required by causality. In a database with single-leader replication (see [“Leaders and Followers”](ch05.html#sec_replication_leader)), the replication log
defines a total order of write operations that is consistent with causality. The leader can simply
increment a counter for each operation, and thus assign a monotonically increasing sequence number
to each operation in the replication log. If a follower applies the writes in the order they appear
in the replication log, the state of the follower is always causally consistent (even if it is
lagging behind the leader).