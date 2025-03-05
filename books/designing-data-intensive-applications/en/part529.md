Weak isolation levels protect against some of those anomalies but leave you, the application
developer, to handle others manually (e.g., using explicit locking). Only serializable isolation
protects against all of these issues. We discussed three different approaches to implementing
serializable transactions: Literally executing transactions in a serial order If you can make each transaction very fast to execute, and the transaction throughput is low
enough to process on a single CPU core, this is a simple and effective option. Two-phase locking For decades this has been the standard way of implementing serializability, but many applications
avoid using it because of its performance characteristics. Serializable snapshot isolation (SSI) A fairly new algorithm that avoids most of the downsides of the previous approaches. It uses an
optimistic approach, allowing transactions to proceed without blocking. When a transaction wants
to commit, it is checked, and it is aborted if the execution was not serializable.