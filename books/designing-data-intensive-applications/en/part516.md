If there is no suitable index where a range lock can be attached, the database can fall back to a
shared lock on the entire table. This will not be good for performance, since it will stop all
other transactions writing to the table, but it’s a safe fallback position. ## Serializable Snapshot Isolation (SSI) 
This chapter has painted a bleak picture of concurrency control in databases. On the one hand, we
have implementations of serializability that don’t perform well (two-phase locking) or don’t scale
well (serial execution). On the other hand, we have weak isolation levels that have good
performance, but are prone to various race conditions (lost updates, write skew, phantoms, etc.). Are
serializable isolation and good performance fundamentally at odds with each other? Perhaps not: an algorithm called serializable snapshot isolation (SSI) is very promising. It
provides full serializability, but has only a small performance penalty compared to snapshot
isolation. SSI is fairly new: it was first described in 2008
[[40](ch07.html#Cahill2008eg)] and is the subject of Michael Cahill’s
PhD thesis
[[51](ch07.html#Cahill2009us)].