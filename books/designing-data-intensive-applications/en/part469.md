Analytic queries and integrity checks 
Sometimes, you may want to run a query that scans over large parts of the database. Such queries
are common in analytics (see [“Transaction Processing or Analytics?”](ch03.html#sec_storage_analytics)), or may be part of a periodic integrity
check that everything is in order (monitoring for data corruption). These queries are likely to
return nonsensical results if they observe parts of the database at different points in time. Snapshot isolation [[28](ch07.html#Berenson1995kj)] is the most common
solution to this problem. The idea is that each transaction reads from a consistent snapshot of
the database—that is, the transaction sees all the data that was committed in the database at the
start of the transaction. Even if the data is subsequently changed by another transaction, each
transaction sees only the old data from that particular point in time. Snapshot isolation is a boon for long-running, read-only queries such as backups and analytics. It
is very hard to reason about the meaning of a query if the data on which it operates is changing at
the same time as the query is executing. When a transaction can see a consistent snapshot of the
database, frozen at a particular point in time, it is much easier to understand.