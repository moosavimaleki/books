
Products such as VoltDB, MemSQL, and Oracle TimesTen are in-memory databases with a relational model,
and the vendors claim that they can offer big performance improvements by removing all the overheads
associated with managing on-disk data structures
[[41](ch03.html#Stonebraker2007ub),
[42](ch03.html#VoltDB2014uj)].
RAMCloud is an open source, in-memory key-value store with durability (using a log-structured
approach for the data in memory as well as the data on disk)
[[43](ch03.html#Rumble2014vz)]. 
Redis and Couchbase provide weak durability by writing to disk asynchronously. 
Counterintuitively, the performance advantage of in-memory databases is not due to the fact that
they don’t need to read from disk. Even a disk-based storage engine may never need to read from disk
if you have enough memory, because the operating system caches recently used disk blocks in memory
anyway. Rather, they can be faster because they can avoid the overheads of encoding in-memory data
structures in a form that can be written to disk
[[44](ch03.html#Harizopoulos2008jb)].