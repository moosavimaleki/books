An update is internally translated into a delete and a create. For example, in
[Figure 7-7](#fig_transactions_mvcc), transaction 13 deducts $100 from account 2, changing the balance from
$500 to $400. The accounts table now actually contains two rows for account 2: a row with a balance
of $500 which was marked as deleted by transaction 13, and a row with a balance of $400 which was
created by transaction 13. ### Visibility rules for observing a consistent snapshot 
When a transaction reads from the database, transaction IDs are used to decide which objects it can
see and which are invisible. By carefully defining visibility rules, the database can present a
consistent snapshot of the database to the application. This works as follows: 1.  At the start of each transaction, the database makes a list of all the other transactions that
are in progress (not yet committed or aborted) at that time. Any writes that those
transactions have made are ignored, even if the transactions subsequently commit.