Let’s dig into the definitions of atomicity, consistency, isolation, and durability, as this will let
us refine our idea of transactions. ### Atomicity 
In general, atomic refers to something that cannot be broken down into smaller parts. The word
means similar but subtly different things in different branches of computing. For example, in
multi-threaded programming, if one thread executes an atomic operation, that means there is no way
that another thread could see the half-finished result of the operation. The system can only be in
the state it was before the operation or after the operation, not something in between. By contrast, in the context of ACID, atomicity is not about concurrency. It does not describe
what happens if several processes try to access the same data at the same time, because that is
covered under the letter I, for isolation (see [“Isolation”](#sec_transactions_acid_isolation)). Rather, ACID atomicity describes what happens if a client wants to make several writes, but a fault
occurs after some of the writes have been processed—for example, a process crashes, a network
connection is interrupted, a disk becomes full, or some integrity constraint is violated.

If the writes are grouped together into an atomic transaction, and the transaction cannot be
completed (committed) due to a fault, then the transaction is aborted and the database must
discard or undo any writes it has made so far in that transaction.