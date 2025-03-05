*  A database is often much more performance-sensitive than an application server, because a single
database instance is often shared by many application servers. A badly written stored procedure
(e.g., using a lot of memory or CPU time) in a database can cause much more trouble than equivalent
badly written code in an application server. 
However, those issues can be overcome. Modern implementations of stored procedures have abandoned
PL/SQL and use existing general-purpose programming languages instead: VoltDB uses Java or Groovy,
Datomic uses Java or Clojure, and Redis uses Lua. With stored procedures and in-memory data, executing all transactions on a single thread becomes
feasible. As they don’t need to wait for I/O and they avoid the overhead of other concurrency control
mechanisms, they can achieve quite good throughput on a single thread. 
VoltDB also uses stored procedures for replication: instead of copying a transaction’s writes from
one node to another, it executes the same stored procedure on each replica. VoltDB therefore
requires that stored procedures are deterministic (when run on different nodes, they must produce
the same result). If a transaction needs to use the current date and time, for example, it must do
so through special deterministic APIs.