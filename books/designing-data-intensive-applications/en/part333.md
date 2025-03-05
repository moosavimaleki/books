Single-node transactions have existed for a long time. However, in the move to distributed
(replicated and partitioned) databases, many systems have abandoned them, claiming that transactions
are too expensive in terms of performance and availability, and asserting that eventual consistency
is inevitable in a scalable system. There is some truth in that statement, but it is overly
simplistic, and we will develop a more nuanced view over the course of the rest of this book. We
will return to the topic of transactions in Chapters
[7](ch07.html#ch_transactions)
and [9](ch09.html#ch_consistency),
and we will discuss some alternative mechanisms in [Part III](part03.html#part_systems). # Multi-Leader Replication 
So far in this chapter we have only considered replication architectures using a single leader.
Although that is a common approach, there are interesting alternatives. Leader-based replication has one major downside: there is only one leader, and all writes must go
through it.[iv](ch05.html#idm140605776056032) If you can’t connect to the leader for any reason, for example due to a network
interruption between you and the leader, you can’t write to the database.