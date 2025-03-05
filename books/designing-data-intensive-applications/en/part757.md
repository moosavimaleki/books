We saw that achieving consensus means deciding something in such a way that all nodes agree on what was
decided, and such that the decision is irrevocable. With some digging, it turns out that a wide
range of problems are actually reducible to consensus and are equivalent to each other (in the sense
that if you have a solution for one of them, you can easily transform it into a solution for one of
the others). Such equivalent problems include: Linearizable compare-and-set registers 
The register needs to atomically decide whether to set its value, based on whether its current
value equals the parameter given in the operation. Atomic transaction commit A database must decide whether to commit or abort a distributed transaction. Total order broadcast The messaging system must decide on the order in which to deliver messages. Locks and leases 
When several clients are racing to grab a lock or lease, the lock decides which one successfully
acquired it.