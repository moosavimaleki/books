Thus, although the FLP result about the impossibility of consensus is of great theoretical
importance, distributed systems can usually achieve consensus in practice. 
In this section we will first examine the atomic commit problem in more detail. In particular, we
will discuss the two-phase commit (2PC) algorithm, which is the most common way of solving atomic
commit and which is implemented in various databases, messaging systems, and application servers. It
turns out that 2PC is a kind of consensus algorithm—but not a very good one
[[70](ch09.html#Gray2006cu),
[71](ch09.html#Guerraoui1995bi)]. 
By learning from 2PC we will then work our way toward better consensus algorithms, such as those
used in ZooKeeper (Zab) and etcd (Raft). ## Atomic Commit and Two-Phase Commit (2PC) 
In [Chapter 7](ch07.html#ch_transactions) we learned that the purpose of transaction atomicity is to provide simple
semantics in the case where something goes wrong in the middle of making several writes. The outcome
of a transaction is either a successful commit, in which case all of the transaction’s writes are
made durable, or an abort, in which case all of the transaction’s writes are rolled back (i.e.,
undone or discarded).