How does the database know if a query result might have changed? There are two cases to consider: *  Detecting reads of a stale MVCC object version (uncommitted write occurred before the read) *  Detecting writes that affect prior reads (the write occurs after the read) ### Detecting stale MVCC reads 
Recall that snapshot isolation is usually implemented by multi-version concurrency control (MVCC;
see [Figure 7-10](#fig_transactions_detect_mvcc)). When a transaction reads from a consistent snapshot in an
MVCC database, it ignores writes that were made by any other transactions that hadn’t yet committed
at the time when the snapshot was taken. In [Figure 7-10](#fig_transactions_detect_mvcc), transaction 43 sees
Alice as having on_call = true, because transaction 42 (which modified Alice’s on-call status) is
uncommitted. However, by the time transaction 43 wants to commit, transaction 42 has already
committed. This means that the write that was ignored when reading from the consistent snapshot has
now taken effect, and transaction 43’s premise is no longer true.