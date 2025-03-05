Thus, on a single node, transaction commitment crucially depends on the order in which data is
durably written to disk: first the data, then the commit record
[[72](ch09.html#Pillai2014vx_ch9)].
The key deciding moment for whether the transaction commits or aborts is the moment at which the
disk finishes writing the commit record: before that moment, it is still possible to abort (due to a
crash), but after that moment, the transaction is committed (even if the database crashes). Thus, it
is a single device (the controller of one particular disk drive, attached to one particular node)
that makes the commit atomic. However, what if multiple nodes are involved in a transaction? For example, perhaps you have a
multi-object transaction in a partitioned database, or a term-partitioned secondary index (in which
the index entry may be on a different node from the primary data; see
[“Partitioning and Secondary Indexes”](ch06.html#sec_partitioning_secondary_indexes)). Most “NoSQL” distributed datastores do not support such
distributed transactions, but various clustered relational systems do (see
[“Distributed Transactions in Practice”](#sec_consistency_dist_trans)).