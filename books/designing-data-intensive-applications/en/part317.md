*  In the case of a log-structured storage engine (see [“SSTables and LSM-Trees”](ch03.html#sec_storage_lsm_trees)), this log is the
main place for storage. Log segments are compacted and garbage-collected in the background. *  In the case of a B-tree (see [“B-Trees”](ch03.html#sec_storage_b_trees)), which overwrites individual disk blocks,
every modification is first written to a write-ahead log so that the index can be restored
to a consistent state after a crash. In either case, the log is an append-only sequence of bytes containing all writes to the database.
We can use the exact same log to build a replica on another node: besides writing the log to disk,
the leader also sends it across the network to its followers. When the follower processes this log,
it builds a copy of the exact same data structures as found on the leader. 
This method of replication is used in PostgreSQL and Oracle, among others
[[16](ch05.html#WALInternalsOfPos2012vf)].
The main disadvantage is that the log describes the data on a very low level: a WAL contains details
of which bytes were changed in which disk blocks. This makes replication closely coupled to the
storage engine. If the database changes its storage format from one version to another, it is
typically not possible to run different versions of the database software on the leader and the
followers.