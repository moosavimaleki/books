
By contrast, serializable snapshot isolation is an optimistic concurrency control technique.
Optimistic in this context means that instead of blocking if something potentially dangerous
happens, transactions continue anyway, in the hope that everything will turn out all right. When a
transaction wants to commit, the database checks whether anything bad happened (i.e., whether
isolation was violated); if so, the transaction is aborted and has to be retried. Only transactions
that executed serializably are allowed to commit. Optimistic concurrency control is an old idea
[[52](ch07.html#Badal1979gw)],
and its advantages and disadvantages have been debated for a long time
[[53](ch07.html#Agrawal1987fr)].
It performs badly if there is high contention (many transactions trying to access the same objects),
as this leads to a high proportion of transactions needing to abort. If the system is already close
to its maximum throughput, the additional transaction load from retried transactions can make
performance worse. However, if there is enough spare capacity, and if contention between transactions is not too high,
optimistic concurrency control techniques tend to perform better than pessimistic ones. Contention
can be reduced with commutative atomic operations: for example, if several transactions concurrently
want to increment a counter, it doesn’t matter in which order the increments are applied (as long as
the counter isn’t read in the same transaction), so the concurrent increments can all be applied
without conflicting.