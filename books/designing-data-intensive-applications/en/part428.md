
When using a routing tier or when sending requests to a random node, clients still need to find the
IP addresses to connect to. These are not as fast-changing as the assignment of partitions to nodes,
so it is often sufficient to use DNS for this purpose. ## Parallel Query Execution 
So far we have focused on very simple queries that read or write a single key (plus scatter/gather
queries in the case of document-partitioned secondary indexes). This is about the level of access
supported by most NoSQL distributed datastores. 
However, massively parallel processing (MPP) relational database products, often used for
analytics, are much more sophisticated in the types of queries they support. A typical data
warehouse query contains several join, filtering, grouping, and aggregation operations. The MPP
query optimizer breaks this complex query into a number of execution stages and partitions, many of
which can be executed in parallel on different nodes of the database cluster. Queries that involve
scanning over large parts of the dataset particularly benefit from such parallel execution.