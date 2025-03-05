In this interactive style of transaction, a lot of time is spent in network communication between
the application and the database. If you were to disallow concurrency in the database and only
process one transaction at a time, the throughput would be dreadful because the database would
spend most of its time waiting for the application to issue the next query for the current
transaction. In this kind of database, it’s necessary to process multiple transactions concurrently
in order to get reasonable performance. For this reason, systems with single-threaded serial transaction processing don’t allow interactive
multi-statement transactions. Instead, the application must submit the entire transaction code to
the database ahead of time, as a stored procedure. The differences between these approaches is
illustrated in [Figure 7-9](#fig_transactions_stored_proc). Provided that all data required by a transaction is
in memory, the stored procedure can execute very fast, without waiting for any network or disk I/O.