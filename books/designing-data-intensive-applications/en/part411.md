
This approach to querying a partitioned database is sometimes known as scatter/gather, and it can
make read queries on secondary indexes quite expensive. Even if you query the partitions in
parallel, scatter/gather is prone to tail latency amplification (see [“Percentiles in Practice”](ch01.html#sidebar_percentiles)).
Nevertheless, it is widely used: MongoDB,
Riak [[15](ch06.html#Riak2014)],
Cassandra [[16](ch06.html#Low2013ud)],
Elasticsearch [[17](ch06.html#Tong2013vh)], SolrCloud
[[18](ch06.html#Solr2014)],
and VoltDB [[19](ch06.html#Pavlo2013ug)]
all use document-partitioned secondary indexes. Most database vendors recommend that you structure
your partitioning scheme so that secondary index queries can be served from a single partition, but
that is not always possible, especially when you’re using multiple secondary indexes in a single
query (such as filtering cars by color and by make at the same time). ![ddia 0605](assets/ddia_0605.png) ###### Figure 6-5. Partitioning secondary indexes by term. ## Partitioning Secondary Indexes by Term 
Rather than each partition having its own secondary index (a local index), we can construct a
global index that covers data in all partitions. However, we can’t just store that index on one
node, since it would likely become a bottleneck and defeat the purpose of partitioning. A global
index must also be partitioned, but it can be partitioned differently from the primary key index.