Hybrid approaches are also possible, for example with a compound key: using one part of the key to
identify the partition and another part for the sort order. 
We also discussed the interaction between partitioning and secondary indexes. A secondary index also
needs to be partitioned, and there are two methods: *   Document-partitioned indexes (local indexes), where the
secondary indexes are stored in the same partition as the primary key and value. This means that
only a single partition needs to be updated on write, but a read of the secondary index requires a
scatter/gather across all partitions. *   Term-partitioned indexes (global indexes), where the secondary
indexes are partitioned separately, using the indexed values. An entry in the secondary index may
include records from all partitions of the primary key. When a document is written, several
partitions of the secondary index need to be updated; however, a read can be served from a single
partition.