*  If transaction A has read an object and transaction B wants to write to that object, B must wait
until A commits or aborts before it can continue. (This ensures that B can’t change the object
unexpectedly behind A’s back.) *  If transaction A has written an object and transaction B wants to read that object, B must wait
until A commits or aborts before it can continue. (Reading an old version of the object, like in
[Figure 7-1](#fig_transactions_increment), is not acceptable under 2PL.) In 2PL, writers don’t just block other writers; they also block readers and vice
versa. Snapshot isolation has the mantra readers never block writers, and writers never block
readers (see [“Implementing snapshot isolation”](#sec_transactions_snapshot_impl)), which captures this key difference between
snapshot isolation and two-phase locking. On the other hand, because 2PL provides serializability,
it protects against all the race conditions discussed earlier, including lost updates and write skew.