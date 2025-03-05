# Chapter 6. Partitioning

# Chapter 6. Partitioning Clearly, we must break away from the sequential and not limit the computers. We must state
definitions and provide for priorities and descriptions of data. We must state relationships, not
procedures. Grace Murray Hopper, Management and the Computer of the Future (1962) ![](assets/ch06-map-ebook.png) 
In [Chapter 5](ch05.html#ch_replication) we discussed replication—that is, having multiple copies of the same data
on different nodes. For very large datasets, or very high query throughput, that is not sufficient:
we need to break the data up into partitions, also known as
sharding.[i](ch06.html#idm140605775395856) # Terminological confusion 
What we call a partition here is called a shard in MongoDB, Elasticsearch, and SolrCloud; it’s known as a
region in HBase, a tablet in Bigtable, a vnode in Cassandra and Riak, and a vBucket in
Couchbase. However, partitioning is the most established term, so we’ll stick with that. Normally, partitions are defined in such a way that each piece of data (each record, row, or
document) belongs to exactly one partition. There are various ways of achieving this,
which we discuss in depth in this chapter. In effect, each partition is a small database of its own,
although the database may support operations that touch multiple partitions at the same time.