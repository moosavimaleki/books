The reduce side of the computation is also partitioned. While the number of map tasks is determined
by the number of input file blocks, the number of reduce tasks is configured by the job author (it
can be different from the number of map tasks). To ensure that all key-value pairs with the same key
end up at the same reducer, the framework uses a hash of the key to determine which reduce task
should receive a particular key-value pair (see [“Partitioning by Hash of Key”](ch06.html#sec_partitioning_hash)). The key-value pairs must be sorted, but the dataset is likely too large to be sorted with a
conventional sorting algorithm on a single machine. Instead, the sorting is performed in stages.
First, each map task partitions its output by reducer, based on the hash of the key. Each of
these partitions is written to a sorted file on the mapper’s local disk, using a technique similar
to what we discussed in [“SSTables and LSM-Trees”](ch03.html#sec_storage_lsm_trees).