Without atomicity, if an error occurs partway through making multiple changes, it’s difficult to
know which changes have taken effect and which haven’t. The application could try again, but that
risks making the same change twice, leading to duplicate or incorrect data. Atomicity simplifies
this problem: if a transaction was aborted, the application can be sure that it didn’t change
anything, so it can safely be retried. The ability to abort a transaction on error and have all writes from that transaction discarded is
the defining feature of ACID atomicity. Perhaps abortability would have been a better term than
atomicity, but we will stick with atomicity since that’s the usual word. ### Consistency 
The word consistency is terribly overloaded: *  In [Chapter 5](ch05.html#ch_replication) we discussed replica consistency and the issue of eventual consistency
that arises in asynchronously replicated systems (see [“Problems with Replication Lag”](ch05.html#sec_replication_lag)). *  Consistent hashing is an approach to partitioning that some systems use for rebalancing (see
[“Consistent Hashing”](ch06.html#sidebar_consistent_hashing)).