If a database only needed to provide read committed isolation, but not snapshot isolation, it would
be sufficient to keep two versions of an object: the committed version and the
overwritten-but-not-yet-committed version. However, storage engines that support snapshot isolation
typically use MVCC for their read committed isolation level as well. A typical approach is that read
committed uses a separate snapshot for each query, while snapshot isolation uses the same snapshot
for an entire transaction. [Figure 7-7](#fig_transactions_mvcc) illustrates how MVCC-based snapshot isolation is implemented in PostgreSQL
[[31](ch07.html#Momjian2014vg)] (other implementations are similar).
When a transaction is started, it is given a unique,
always-increasing[vii](ch07.html#idm140605762226000)
transaction ID (txid). Whenever a transaction writes anything to the database, the data it writes
is tagged with the transaction ID of the writer. ![ddia 0707](assets/ddia_0707.png) ###### Figure 7-7. Implementing snapshot isolation using multi-version objects. Each row in a table has a created_by field, containing the ID of the transaction that inserted
this row into the table. Moreover, each row has a deleted_by field, which is initially empty. If a
transaction deletes a row, the row isn’t actually deleted from the database, but it is marked for
deletion by setting the deleted_by field to the ID of the transaction that requested the deletion.
At some later time, when it is certain that no transaction can any longer access the deleted data, a
garbage collection process in the database removes any rows marked for deletion and frees their
space.