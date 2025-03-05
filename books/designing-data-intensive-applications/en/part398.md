In this chapter we will first look at different approaches for partitioning large datasets and
observe how the indexing of data interacts with partitioning. We’ll then talk about rebalancing,
which is necessary if you want to add or remove nodes in your cluster. Finally, we’ll get an
overview of how databases route requests to the right partitions and execute queries. # Partitioning and Replication 
Partitioning is usually combined with replication so that copies of each partition are stored on
multiple nodes. This means that, even though each record belongs to exactly one partition, it may
still be stored on several different nodes for fault tolerance. A node may store more than one partition. If a leader–follower replication model is used, the
combination of partitioning and replication can look like [Figure 6-1](#fig_partitioning_replicas).
Each partition’s leader is assigned to one node, and its followers are assigned to other nodes. Each
node may be the leader for some partitions and a follower for other partitions.