*  
In databases with secondary indexes (almost everything except pure key-value stores), the indexes
also need to be updated every time you change a value. These indexes are different database
objects from a transaction point of view: for example, without transaction isolation, it’s
possible for a record to appear in one index but not another, because the update to the second
index hasn’t happened yet. Such applications can still be implemented without transactions. However, error handling becomes
much more complicated without atomicity, and the lack of isolation can cause concurrency problems.
We will discuss those in [“Weak Isolation Levels”](#sec_transactions_isolation_levels), and explore alternative approaches
in [Chapter 12](ch12.html#ch_future). ### Handling errors and aborts 
A key feature of a transaction is that it can be aborted and safely retried if an error occurred.
ACID databases are based on this philosophy: if the database is in danger of violating its guarantee
of atomicity, isolation, or durability, it would rather abandon the transaction entirely than allow
it to remain half-finished.