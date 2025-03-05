[xi](ch09.html#idm140605759417392-marker) If you don’t wait, but acknowledge the
write immediately after it has been enqueued, you get something similar to the memory consistency model
of multi-core x86 processors [[43](ch09.html#Sewell2010fj)]. That
model is neither linearizable nor sequentially consistent. [xii](ch09.html#idm140605759344208-marker) Atomic commit is
formalized slightly differently from consensus: an atomic transaction can commit only if
all participants vote to commit, and must abort if any participant needs to abort.
Consensus is allowed to decide on any value that is proposed by one of the participants.
However, atomic commit and consensus are reducible to each other
[[70](ch09.html#Gray2006cu),
[71](ch09.html#Guerraoui1995bi)]. Nonblocking atomic commit is
harder than consensus—see [“Three-phase commit”](#sec_consistency_3pc). [xiii](ch09.html#idm140605759010832-marker) This
particular variant of consensus is called uniform consensus, which is equivalent to regular
consensus in asynchronous systems with unreliable failure detectors
[[71](ch09.html#Guerraoui1995bi)]. The academic literature usually
refers to processes rather than nodes, but we use nodes here for
consistency with the rest of this book.