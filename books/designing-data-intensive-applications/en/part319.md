*  For an inserted row, the log contains the new values of all columns. *  For a deleted row, the log contains enough information to uniquely identify the row that was
deleted. Typically this would be the primary key, but if there is no primary key on the table, the
old values of all columns need to be logged. *  For an updated row, the log contains enough information to uniquely identify the updated row, and
the new values of all columns (or at least the new values of all columns that changed). 
A transaction that modifies several rows generates several such log records, followed by a record
indicating that the transaction was committed. MySQL’s binlog (when configured to use row-based
replication) uses this approach
[[17](ch05.html#MySQLInternals)]. Since a logical log is decoupled from the storage engine internals, it can more easily be kept
backward compatible, allowing the leader and the follower to run different versions of the database
software, or even different storage engines.