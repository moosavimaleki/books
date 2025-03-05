*  Write throughput must be low enough to be handled on a single CPU core, or else transactions
need to be partitioned without requiring cross-partition coordination. *  Cross-partition transactions are possible, but there is a hard limit to the extent to which they
  can be used. ## Two-Phase Locking (2PL) 
For around 30 years, there was only one widely used algorithm for serializability in databases:
two-phase locking (2PL).[xi](ch07.html#idm140605761509024) # 2PL is not 2PC Note that while two-phase locking (2PL) sounds very similar to two-phase commit (2PC), they are
completely different things. We will discuss 2PC in [Chapter 9](ch09.html#ch_consistency). We saw previously that locks are often used to prevent dirty writes (see
[“No dirty writes”](#sec_transactions_dirty_write)): if two transactions concurrently try to write to the same object,
the lock ensures that the second writer must wait until the first one has finished its transaction
(aborted or committed) before it may continue. Two-phase locking is similar, but makes the lock requirements much stronger. Several transactions
are allowed to concurrently read the same object as long as nobody is writing to it. But as soon as
anyone wants to write (modify or delete) an object, exclusive access is required: