### Synchronized clocks for global snapshots 
In [“Snapshot Isolation and Repeatable Read”](ch07.html#sec_transactions_snapshot_isolation) we discussed snapshot isolation, which is a very useful
feature in databases that need to support both small, fast read-write transactions and large,
long-running read-only transactions (e.g., for backups or analytics). It allows read-only
transactions to see the database in a consistent state at a particular point in time, without
locking and interfering with read-write transactions. 
The most common implementation of snapshot isolation requires a monotonically increasing transaction
ID. If a write happened later than the snapshot (i.e., the write has a greater transaction ID than
the snapshot), that write is invisible to the snapshot transaction. On a single-node database, a
simple counter is sufficient for generating transaction IDs. 
However, when a database is distributed across many machines, potentially in multiple datacenters, a
global, monotonically increasing transaction ID (across all partitions) is difficult to generate,
because it requires coordination. The transaction ID must reflect causality: if transaction B reads
a value that was written by transaction A, then B must have a higher transaction ID than
A—otherwise, the snapshot would not be consistent. With lots of small, rapid transactions, creating
transaction IDs in a distributed system becomes an untenable
bottleneck.[vi](ch08.html#idm140605760654304)