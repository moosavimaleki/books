![ddia 0608](assets/ddia_0608.png) ###### Figure 6-8. Using ZooKeeper to keep track of assignment of partitions to nodes. 
For example, LinkedIn’s Espresso uses Helix
[[31](ch06.html#Gopalakrishna2012fa)]
for cluster management (which in turn relies on ZooKeeper), implementing a routing tier as shown in
[Figure 6-8](#fig_partitioning_zookeeper). HBase, SolrCloud, and Kafka also use ZooKeeper to track partition
assignment. MongoDB has a similar architecture, but it relies on its own config server
implementation and mongos daemons as the routing tier. 
Cassandra and Riak take a different approach: they use a gossip protocol among the nodes to
disseminate any changes in cluster state. Requests can be sent to any node, and that node forwards
them to the appropriate node for the requested partition (approach 1 in
[Figure 6-7](#fig_partitioning_routing)). This model puts more complexity in the database nodes but avoids the
dependency on an external coordination service such as ZooKeeper. 
Couchbase does not rebalance automatically, which simplifies the design. Normally it is configured
with a routing tier called moxi, which learns about routing changes from the cluster nodes
[[32](ch06.html#MoxiManual)].