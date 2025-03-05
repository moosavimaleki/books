2.  When writing to the database, you will only overwrite data that has been committed (no dirty
writes). Let’s discuss these two guarantees in more detail. ### No dirty reads 
Imagine a transaction has written some data to the database, but the transaction has not yet committed or aborted.
Can another transaction see that uncommitted data? If yes, that is called a
dirty read [[2](ch07.html#Gray1976us)]. Transactions running at the read committed isolation level must prevent dirty reads. This means that
any writes by a transaction only become visible to others when that transaction commits (and then
all of its writes become visible at once). This is illustrated in
[Figure 7-4](#fig_transactions_read_committed), where user 1 has set x = 3, but user 2’s get x still
returns the old value, 2, while user 1 has not yet committed. ![ddia 0704](assets/ddia_0704.png) ###### Figure 7-4. No dirty reads: user 2 sees the new value for x only after user 1’s transaction has committed.