Finally, we discussed techniques for routing queries to the appropriate partition, which range from
simple partition-aware load balancing to sophisticated parallel query execution engines. By design, every partition operates mostly independently—that’s what allows a partitioned
database to scale to multiple machines. However, operations that need to write to several partitions
can be difficult to reason about: for example, what happens if the write to one partition succeeds,
but another fails? We will address that question in the following chapters. ##### Footnotes [i](ch06.html#idm140605775395856-marker) Partitioning, as discussed in this
chapter, is a way of intentionally breaking a large database down into smaller ones. It has nothing
to do with network partitions (netsplits), a type of fault in the network between nodes. We
will discuss such faults in [Chapter 8](ch08.html#ch_distributed). [ii](ch06.html#idm140605775218496-marker) If your database
only supports a key-value model, you might be tempted to implement a secondary index yourself by
creating a mapping from values to document IDs in application code. If you go down this route, you need to
take great care to ensure your indexes remain consistent with the underlying data. Race conditions
and intermittent write failures (where some changes were saved but others weren’t) can very easily
cause the data to go out of sync—see [“The need for multi-object transactions”](ch07.html#sec_transactions_need).