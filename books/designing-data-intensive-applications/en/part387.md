Finally, we discussed the concurrency issues that are inherent in multi-leader and leaderless
replication approaches: because they allow multiple writes to happen concurrently, conflicts may
occur. We examined an algorithm that a database might use to determine whether one operation
happened before another, or whether they happened concurrently. We also touched on methods for
resolving conflicts by merging together concurrent updates. In the next chapter we will continue looking at data that is distributed across multiple machines,
through the counterpart of replication: splitting a large dataset into partitions. ##### Footnotes [i](ch05.html#idm140605776424400-marker) Different people have
different definitions for hot, warm, and cold standby servers. In
PostgreSQL, for example, hot standby is used to refer to a replica that accepts reads
from clients, whereas a warm standby processes changes from the leader but doesn’t
process any queries from clients. For purposes of this book, the difference isn’t
important. [ii](ch05.html#idm140605776275968-marker) This approach is known as
fencing or, more emphatically, Shoot The Other Node In The Head (STONITH). We
will discuss fencing in more detail in [“The leader and the lock”](ch08.html#sec_distributed_lock_fencing).