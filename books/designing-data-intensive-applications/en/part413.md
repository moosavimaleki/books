The advantage of a global (term-partitioned) index over a document-partitioned index is that it can
make reads more efficient: rather than doing scatter/gather over all partitions, a client only needs
to make a request to the partition containing the term that it wants. However, the downside of a
global index is that writes are slower and more complicated, because a write to a single
document may now affect multiple partitions of the index (every term in the document might be on a
different partition, on a different node). In an ideal world, the index would always be up to date, and every document written to the database
would immediately be reflected in the index. However, in a term-partitioned index, that would
require a distributed transaction across all partitions affected by a write, which is not supported
in all databases (see [Chapter 7](ch07.html#ch_transactions) and [Chapter 9](ch09.html#ch_consistency)). In practice, updates to global secondary indexes are often asynchronous (that is, if you read the
index shortly after a write, the change you just made may not yet be reflected in the index). For
example, Amazon DynamoDB states that its global secondary indexes are updated within a fraction of a
second in normal circumstances, but may experience longer propagation delays in cases of faults in
the infrastructure
[[20](ch06.html#DynamoDB2014)].