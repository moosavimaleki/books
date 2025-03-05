
Atomicity prevents failed transactions from littering the database with half-finished results and
half-updated state. This is especially important for multi-object transactions (see
[“Single-Object and Multi-Object Operations”](ch07.html#sec_transactions_multi_object)) and databases that maintain secondary indexes. Each secondary
index is a separate data structure from the primary data—thus, if you modify some data, the
corresponding change needs to also be made in the secondary index. Atomicity ensures that the
secondary index stays consistent with the primary data (if the index became inconsistent with the
primary data, it would not be very useful). ### From single-node to distributed atomic commit For transactions that execute at a single database node, atomicity is commonly implemented by the
storage engine. When the client asks the database node to commit the transaction, the database makes
the transaction’s writes durable (typically in a write-ahead log; see [“Making B-trees reliable”](ch03.html#sec_storage_btree_wal)) and
then appends a commit record to the log on disk. If the database crashes in the middle of this
process, the transaction is recovered from the log when the node restarts: if the commit record was
successfully written to disk before the crash, the transaction is considered committed; if not, any
writes from that transaction are rolled back.