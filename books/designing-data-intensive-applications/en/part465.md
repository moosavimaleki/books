*  
However, read committed does not prevent the race condition between two counter increments in
[Figure 7-1](#fig_transactions_increment). In this case, the second write happens after the first transaction
has committed, so it’s not a dirty write. It’s still incorrect, but for a different reason—in
[“Preventing Lost Updates”](#sec_transactions_lost_update) we will discuss how to make such counter increments safe. ![ddia 0705](assets/ddia_0705.png) ###### Figure 7-5. With dirty writes, conflicting writes from different transactions can be mixed up. ### Implementing read committed 
Read committed is a very popular isolation level. It is the default setting in Oracle 11g,
PostgreSQL, SQL Server 2012, MemSQL, and many other databases
[[8](ch07.html#Bailis2013tn)]. 
Most commonly, databases prevent dirty writes by using row-level locks: when a transaction wants to
modify a particular object (row or document), it must first acquire a lock on that object. It must
then hold that lock until the transaction is committed or aborted. Only one transaction can hold the
lock for any given object; if another transaction wants to write to the same object, it must wait
until the first transaction is committed or aborted before it can acquire the lock and continue.
This locking is done automatically by databases in read committed mode (or stronger isolation
levels).