Without transactions, various error scenarios (processes crashing, network interruptions, power
outages, disk full, unexpected concurrency, etc.) mean that data can become inconsistent in various
ways. For example, denormalized data can easily go out of sync with the source data. Without
transactions, it becomes very difficult to reason about the effects that complex interacting accesses
can have on the database. In this chapter, we went particularly deep into the topic of concurrency control. We discussed
several widely used isolation levels, in particular read committed, snapshot isolation
(sometimes called repeatable read), and serializable. We characterized those isolation levels by
discussing various examples of race conditions: Dirty reads One client reads another client’s writes before they have been committed. The read committed
isolation level and stronger levels prevent dirty reads. Dirty writes One client overwrites data that another client has written, but not yet committed. Almost all
transaction implementations prevent dirty writes. Read skew (nonrepeatable reads)