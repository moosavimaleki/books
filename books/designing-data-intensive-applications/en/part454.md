
Some databases also provide more complex atomic
operations,[iv](ch07.html#idm140605774682240) such as an increment operation, which removes the
need for a read-modify-write cycle like that in [Figure 7-1](#fig_transactions_increment). Similarly popular is a
compare-and-set operation, which allows a write to happen only if the value has not been
concurrently changed by someone else (see [“Compare-and-set”](#sec_transactions_compare_and_set)). These single-object operations are useful, as they can prevent lost updates when several clients try
to write to the same object concurrently (see [“Preventing Lost Updates”](#sec_transactions_lost_update)). However, they are
not transactions in the usual sense of the word. Compare-and-set and other
single-object operations have been dubbed “lightweight transactions” or even “ACID” for marketing
purposes [[20](ch07.html#Scherer2013vz),
[21](ch07.html#Kingsbury2013ti_ch7),
[22](ch07.html#Aerospike2014wa)],
but that terminology is misleading. A transaction is usually understood as a mechanism for grouping
multiple operations on multiple objects into one unit of execution. ### The need for multi-object transactions 
Many distributed datastores have abandoned multi-object transactions because they are difficult to
implement across partitions, and they can get in the way in some scenarios where very high
availability or performance is required. However, there is nothing that fundamentally prevents
transactions in a distributed database, and we will discuss implementations of distributed
transactions in [Chapter 9](ch09.html#ch_consistency).