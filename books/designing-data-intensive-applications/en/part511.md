
For this reason, databases running 2PL can have quite unstable latencies, and they can be very slow at
high percentiles (see [“Describing Performance”](ch01.html#sec_introduction_percentiles)) if there is contention in the workload. It
may take just one slow transaction, or one transaction that accesses a lot of data and acquires many
locks, to cause the rest of the system to grind to a halt. This instability is problematic when
robust operation is required. Although deadlocks can happen with the lock-based read committed isolation level, they occur much
more frequently under 2PL serializable isolation (depending on the access patterns of your
transaction). This can be an additional performance problem: when a transaction is aborted due to
deadlock and is retried, it needs to do its work all over again. If deadlocks are frequent, this can
mean significant wasted effort. ### Predicate locks 
In the preceding description of locks, we glossed over a subtle but important detail. In
[“Phantoms causing write skew”](#sec_transactions_phantom) we discussed the problem of phantoms—that is, one transaction
changing the results of another transaction’s search query. A database with serializable isolation
must prevent phantoms.