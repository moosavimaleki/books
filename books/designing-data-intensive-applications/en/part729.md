
If the application process crashes, or the machine on which the application is running dies, the
coordinator goes with it. Any participants with prepared but uncommitted transactions are then stuck
in doubt. Since the coordinator’s log is on the application server’s local disk, that server must be
restarted, and the coordinator library must read the log to recover the commit/abort outcome of each
transaction. Only then can the coordinator use the database driver’s XA callbacks to ask
participants to commit or abort, as appropriate. The database server cannot contact the coordinator
directly, since all communication must go via its client library. ### Holding locks while in doubt 
Why do we care so much about a transaction being stuck in doubt? Can’t the rest of the system just
get on with its work, and ignore the in-doubt transaction that will be cleaned up eventually? The problem is with locking. As discussed in [“Read Committed”](ch07.html#sec_transactions_read_committed), database
transactions usually take a row-level exclusive lock on any rows they modify, to prevent dirty
writes. In addition, if you want serializable isolation, a database using two-phase locking would also
have to take a shared lock on any rows read by the transaction (see [“Two-Phase Locking (2PL)”](ch07.html#sec_transactions_2pl)).