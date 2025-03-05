When a transaction writes to the database, it must look in the indexes for any other transactions
that have recently read the affected data. This process is similar to acquiring a write lock on the affected
key range, but rather than blocking until the readers have committed, the lock acts as a tripwire:
it simply notifies the transactions that the data they read may no longer be up to date. In [Figure 7-11](#fig_transactions_detect_index_range), transaction 43 notifies transaction 42 that its prior
read is outdated, and vice versa. Transaction 42 is first to commit, and it is successful: although
transaction 43’s write affected 42, 43 hasn’t yet committed, so the write has not yet taken effect.
However, when transaction 43 wants to commit, the conflicting write from 42 has already been
committed, so 43 must abort. ### Performance of serializable snapshot isolation 
As always, many engineering details affect how well an algorithm works in practice. For example, one
trade-off is the granularity at which transactions’ reads and writes are tracked. If the database
keeps track of each transaction’s activity in great detail, it can be precise about which
transactions need to abort, but the bookkeeping overhead can become significant. Less detailed
tracking is faster, but may lead to more transactions being aborted than strictly necessary.