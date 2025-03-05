*  If a transaction first reads and then writes an object, it may upgrade its shared lock to an
exclusive lock. The upgrade works the same as getting an exclusive lock directly. *  After a transaction has acquired the lock, it must continue to hold the lock until the end of the
transaction (commit or abort). This is where the name “two-phase” comes from: the first phase
(while the transaction is executing) is when the locks are acquired, and the second phase (at the
end of the transaction) is when all the locks are released. 
Since so many locks are in use, it can happen quite easily that transaction A is stuck waiting for
transaction B to release its lock, and vice versa. This situation is called deadlock. The database
automatically detects deadlocks between transactions and aborts one of them so that the others can
make progress. The aborted transaction needs to be retried by the application.