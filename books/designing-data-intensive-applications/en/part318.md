That may seem like a minor implementation detail, but it can have a big operational impact. If the
replication protocol allows the follower to use a newer software version than the leader, you can
perform a zero-downtime upgrade of the database software by first upgrading the followers and then
performing a failover to make one of the upgraded nodes the new leader. If the replication protocol
does not allow this version mismatch, as is often the case with WAL shipping, such upgrades require
downtime. ### Logical (row-based) log replication 
An alternative is to use different log formats for replication and for the storage engine, which
allows the replication log to be decoupled from the storage engine internals. This kind of
replication log is called a logical log, to distinguish it from the storage engine’s (physical)
data representation. 
A logical log for a relational database is usually a sequence of records describing writes to
database tables at the granularity of a row: