Since cross-partition transactions have additional coordination overhead, they are vastly slower
than single-partition transactions. VoltDB reports a throughput of about 1,000 cross-partition
writes per second, which is orders of magnitude below its single-partition throughput and cannot be
increased by adding more machines [[49](ch07.html#Hugg2014ua)]. Whether transactions can be single-partition depends very much on the structure of the data used by
the application. Simple key-value data can often be partitioned very easily, but data with multiple
secondary indexes is likely to require a lot of cross-partition coordination (see
[“Partitioning and Secondary Indexes”](ch06.html#sec_partitioning_secondary_indexes)). ### Summary of serial execution Serial execution of transactions has become a viable way of achieving serializable isolation within
certain constraints: *  Every transaction must be small and fast, because it takes only one slow transaction to stall all
transaction processing. *  It is limited to use cases where the active dataset can fit in memory. Rarely accessed data could
potentially be moved to disk, but if it needed to be accessed in a single-threaded transaction,
the system would get very slow.[x](ch07.html#idm140605761528448)