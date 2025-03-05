Dynamic partitioning is not only suitable for key range–partitioned data, but can equally well be
used with hash-partitioned data. MongoDB since version 2.4 supports both key-range and hash
partitioning, and it splits partitions dynamically in either case. ### Partitioning proportionally to nodes 
With dynamic partitioning, the number of partitions is proportional to the size of the dataset,
since the splitting and merging processes keep the size of each partition between some fixed minimum
and maximum. On the other hand, with a fixed number of partitions, the size of each partition is
proportional to the size of the dataset. In both of these cases, the number of partitions is
independent of the number of nodes. 
A third option, used by Cassandra and Ketama, is to make the number of partitions proportional to
the number of nodes—in other words, to have a fixed number of partitions per node
[[23](ch06.html#RethinkingTopology2012th),
[27](ch06.html#Williams2012wz),
[28](ch06.html#Jones2007bl)].
In this case, the size of each partition grows proportionally to the dataset size while the number
of nodes remains unchanged, but when you increase the number of nodes, the partitions become smaller
again. Since a larger data volume generally requires a larger number of nodes to store, this
approach also keeps the size of each partition fairly stable.