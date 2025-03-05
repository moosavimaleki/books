But if serializable isolation is so much better than the mess of weak isolation levels, then why
isn’t everyone using it? To answer this question, we need to look at the options for implementing
serializability, and how they perform. Most databases that provide serializability today use one of
three techniques, which we will explore in the rest of this chapter: *  Literally executing transactions in a serial order (see [“Actual Serial Execution”](#sec_transactions_serial)) *  Two-phase locking (see [“Two-Phase Locking (2PL)”](#sec_transactions_2pl)), which for several decades was the only viable
option *  Optimistic concurrency control techniques such as serializable snapshot isolation (see
[“Serializable Snapshot Isolation (SSI)”](#sec_transactions_ssi)) For now, we will discuss these techniques primarily in the context of single-node databases; in
[Chapter 9](ch09.html#ch_consistency) we will examine how they can be generalized to transactions that involve multiple
nodes in a distributed system. ## Actual Serial Execution 
The simplest way of avoiding concurrency problems is to remove the concurrency entirely: to
execute only one transaction at a time, in serial order, on a single thread. By doing so, we completely
sidestep the problem of detecting and preventing conflicts between transactions: the resulting
isolation is by definition serializable.