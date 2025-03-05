*  
In [“Detecting Concurrent Writes”](ch05.html#sec_replication_concurrent) we observed that if you have two operations A and B, there are
three possibilities: either A happened before B, or B happened before A, or A and B are
concurrent. This happened before relationship is another expression of causality: if A happened
before B, that means B might have known about A, or built upon A, or depended on A. If A and B are
concurrent, there is no causal link between them; in other words, we are sure that neither knew
about the other. *  
In the context of snapshot isolation for transactions ([“Snapshot Isolation and Repeatable Read”](ch07.html#sec_transactions_snapshot_isolation)),
we said that a transaction reads from a consistent snapshot. But what does “consistent” mean in
this context? It means consistent with causality: if the snapshot contains an answer, it must
also contain the question being answered
[[48](ch09.html#Ahamad1995gl)].
Observing the entire database at a single point in time makes it consistent with causality: the
effects of all operations that happened causally before that point in time are visible, but no
operations that happened causally afterward can be seen.