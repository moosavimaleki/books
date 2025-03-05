2.  Any writes made by aborted transactions are ignored. 3.  Any writes made by transactions with a later transaction ID (i.e., which started after the current
transaction started) are ignored, regardless of whether those transactions have committed. 4.  All other writes are visible to the application’s queries. These rules apply to both creation and deletion of objects. In [Figure 7-7](#fig_transactions_mvcc), when
transaction 12 reads from account 2, it sees a balance of $500 because the deletion of the $500
balance was made by transaction 13 (according to rule 3, transaction 12 cannot see a deletion made
by transaction 13), and the creation of the $400 balance is not yet visible (by the same rule). Put another way, an object is visible if both of the following conditions are true: *  At the time when the reader’s transaction started, the transaction that created the object had
already committed. *  The object is not marked for deletion, or if it is, the transaction that requested deletion had
not yet committed at the time when the reader’s transaction started.