
Today SSI is used both in single-node databases (the serializable isolation level
in PostgreSQL since version 9.1 [[41](ch07.html#Ports2012uw)]) and
distributed databases (FoundationDB uses a similar algorithm).
As SSI is so young compared to other concurrency control mechanisms, it is still proving its
performance in practice, but it has the possibility of being fast enough to become the new default in
the future. ### Pessimistic versus optimistic concurrency control 
Two-phase locking is a so-called pessimistic concurrency control mechanism: it is based on the
principle that if anything might possibly go wrong (as indicated by a lock held by another
transaction), it’s better to wait until the situation is safe again before doing anything. It is
like mutual exclusion, which is used to protect data structures in multi-threaded programming. Serial execution is, in a sense, pessimistic to the extreme: it is essentially equivalent to each
transaction having an exclusive lock on the entire database (or one partition of the database) for
the duration of the transaction. We compensate for the pessimism by making each transaction very
fast to execute, so it only needs to hold the “lock” for a short time.