
In replicated databases (see [Chapter 5](ch05.html#ch_replication)), preventing lost updates takes on another
dimension: since they have copies of the data on multiple nodes, and the data can potentially be
modified concurrently on different nodes, some additional steps need to be taken to prevent lost
updates. Locks and compare-and-set operations assume that there is a single up-to-date copy of the data.
However, databases with multi-leader or leaderless replication usually allow several writes to
happen concurrently and replicate them asynchronously, so they cannot guarantee that there is a
single up-to-date copy of the data. Thus, techniques based on locks or compare-and-set do not apply
in this context. (We will revisit this issue in more detail in [“Linearizability”](ch09.html#sec_consistency_linearizability).) 
Instead, as discussed in [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent), a common approach in such replicated
databases is to allow concurrent writes to create several conflicting versions of a value (also
known as siblings), and to use application code or special data structures to resolve and merge
these versions after the fact.