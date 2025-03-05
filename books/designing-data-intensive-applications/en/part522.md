![ddia 0710](assets/ddia_0710.png) ###### Figure 7-10. Detecting when a transaction reads outdated values from an MVCC snapshot. In order to prevent this anomaly, the database needs to track when a transaction ignores another
transaction’s writes due to MVCC visibility rules. When the transaction wants to commit, the
database checks whether any of the ignored writes have now been committed. If so, the transaction
must be aborted. Why wait until committing? Why not abort transaction 43 immediately when the stale read is detected?
Well, if transaction 43 was a read-only transaction, it wouldn’t need to be aborted, because there
is no risk of write skew. At the time when transaction 43 makes its read, the database doesn’t yet
know whether that transaction is going to later perform a write. Moreover, transaction 42 may yet
abort or may still be uncommitted at the time when transaction 43 is committed, and so the read may
turn out not to have been stale after all. By avoiding unnecessary aborts, SSI preserves snapshot
isolation’s support for long-running reads from a consistent snapshot.