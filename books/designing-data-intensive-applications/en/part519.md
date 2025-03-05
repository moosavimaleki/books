As the name suggests, SSI is based on snapshot isolation—that is, all reads within a transaction
are made from a consistent snapshot of the database (see [“Snapshot Isolation and Repeatable Read”](#sec_transactions_snapshot_isolation)).
This is the main difference compared to earlier optimistic concurrency control techniques. On top of
snapshot isolation, SSI adds an algorithm for detecting serialization conflicts among writes and
determining which transactions to abort. ### Decisions based on an outdated premise 
When we previously discussed write skew in snapshot isolation (see [“Write Skew and Phantoms”](#sec_transactions_write_skew)),
we observed a recurring pattern: a transaction reads some data from the database, examines the
result of the query, and decides to take some action (write to the database) based on the result
that it saw. However, under snapshot isolation, the result from the original query may no longer be
up-to-date by the time the transaction commits, because the data may have been modified in the
meantime.