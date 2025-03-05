On the OLTP side, we saw storage engines from two main schools of thought: *  The log-structured school, which only permits appending to files and deleting obsolete files, but
never updates a file that has been written. Bitcask, SSTables, LSM-trees, LevelDB, Cassandra,
HBase, Lucene, and others belong to this group. *  The update-in-place school, which treats the disk as a set of fixed-size pages that can be overwritten.
B-trees are the biggest example of this philosophy, being used in all major relational databases
and also many nonrelational ones. Log-structured storage engines are a comparatively recent development. Their key idea is that they
systematically turn random-access writes into sequential writes on disk, which enables higher write
throughput due to the performance characteristics of hard drives and SSDs. Finishing off the OLTP side, we did a brief tour through some more complicated indexing structures,
and databases that are optimized for keeping all data in memory.