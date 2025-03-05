### Implementation of two-phase locking 
2PL is used by the serializable isolation level in MySQL (InnoDB) and SQL Server, and the
repeatable read isolation level in DB2
[[23](ch07.html#Kleppmann2014ut),
[36](ch07.html#Mukherjee2013uw)]. 
The blocking of readers and writers is implemented by a having a lock on each object in the
database. The lock can either be in shared mode or in exclusive mode. The lock is used as
follows: *  
If a transaction wants to read an object, it must first acquire the lock in shared mode. Several
transactions are allowed to hold the lock in shared mode simultaneously, but if another
transaction already has an exclusive lock on the object, these transactions must wait. *  If a transaction wants to write to an object, it must first acquire the lock in exclusive mode. No
other transaction may hold the lock at the same time (either in shared or in exclusive mode), so
if there is any existing lock on the object, the transaction must wait.